import os
import sqlite3
import secrets
from datetime import datetime

import qrcode
from flask import (
    Flask,
    flash,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")
QR_DIR = os.path.join(BASE_DIR, "static", "qr")

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")
app.config["PUBLIC_BASE_URL"] = os.environ.get("PUBLIC_BASE_URL", "").strip().rstrip("/")


def init_dirs():
    os.makedirs(QR_DIR, exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "static"), exist_ok=True)
    os.makedirs(os.path.join(BASE_DIR, "templates"), exist_ok=True)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            original_url TEXT NOT NULL,
            short_code TEXT NOT NULL UNIQUE,
            click_count INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        );
        """
    )
    db.commit()


def login_required(view):
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    wrapped.__name__ = view.__name__
    return wrapped


def create_short_code(length=6):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(secrets.choice(alphabet) for _ in range(length))


def is_valid_url(url):
    return url.startswith(("http://", "https://"))


def generate_unique_code():
    db = get_db()
    while True:
        code = create_short_code()
        existing = db.execute("SELECT id FROM urls WHERE short_code = ?", (code,)).fetchone()
        if not existing:
            return code


def current_user():
    if "user_id" not in session:
        return None
    db = get_db()
    return db.execute("SELECT * FROM users WHERE id = ?", (session["user_id"],)).fetchone()


def get_public_base_url():
    configured_url = app.config.get("PUBLIC_BASE_URL")
    if configured_url:
        return configured_url
    return request.url_root.rstrip("/")


@app.context_processor
def inject_user():
    return {"current_user": current_user()}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            flash("All fields are required.", "danger")
            return render_template("register.html")

        db = get_db()
        existing = db.execute("SELECT id FROM users WHERE email = ?", (email,)).fetchone()
        if existing:
            flash("Email already registered.", "warning")
            return render_template("register.html")

        db.execute(
            "INSERT INTO users (name, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
            (name, email, generate_password_hash(password), datetime.utcnow().isoformat()),
        )
        db.commit()
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        db = get_db()
        user = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            flash("Welcome back!", "success")
            return redirect(url_for("dashboard"))

        flash("Invalid email or password.", "danger")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))


@app.route("/shorten", methods=["POST"])
@login_required
def shorten_url():
    original_url = request.form.get("original_url", "").strip()
    custom_code = request.form.get("custom_code", "").strip()

    if not original_url:
        flash("Please enter a URL.", "danger")
        return redirect(url_for("dashboard"))

    if not is_valid_url(original_url):
        flash("URL must start with http:// or https://", "warning")
        return redirect(url_for("dashboard"))

    db = get_db()
    if custom_code:
        existing = db.execute("SELECT id FROM urls WHERE short_code = ?", (custom_code,)).fetchone()
        if existing:
            flash("Custom short code already exists.", "warning")
            return redirect(url_for("dashboard"))
        short_code = custom_code
    else:
        short_code = generate_unique_code()

    db.execute(
        """
        INSERT INTO urls (user_id, original_url, short_code, click_count, created_at)
        VALUES (?, ?, ?, 0, ?)
        """,
        (session["user_id"], original_url, short_code, datetime.utcnow().isoformat()),
    )
    db.commit()

    qr_path = os.path.join(QR_DIR, f"{short_code}.png")
    short_url = f"{get_public_base_url()}/{short_code}"
    img = qrcode.make(short_url)
    img.save(qr_path)

    flash("Short URL created successfully.", "success")
    return redirect(url_for("dashboard"))


@app.route("/<short_code>")
def redirect_short_url(short_code):
    db = get_db()
    row = db.execute("SELECT * FROM urls WHERE short_code = ?", (short_code,)).fetchone()
    if not row:
        flash("Short URL not found.", "danger")
        return redirect(url_for("index"))

    db.execute("UPDATE urls SET click_count = click_count + 1 WHERE id = ?", (row["id"],))
    db.commit()
    return redirect(row["original_url"])


@app.route("/dashboard")
@login_required
def dashboard():
    db = get_db()
    urls = db.execute(
        """
        SELECT * FROM urls
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (session["user_id"],),
    ).fetchall()

    labels = [row["short_code"] for row in reversed(urls)]
    data = [row["click_count"] for row in reversed(urls)]
    return render_template("dashboard.html", urls=urls, labels=labels, data=data)


@app.route("/qr/<filename>")
@login_required
def qr_image(filename):
    return send_from_directory(QR_DIR, filename)


@app.route("/api/dashboard-data")
@login_required
def dashboard_data():
    db = get_db()
    urls = db.execute(
        "SELECT short_code, click_count FROM urls WHERE user_id = ? ORDER BY created_at DESC",
        (session["user_id"],),
    ).fetchall()
    return jsonify(
        {
            "labels": [row["short_code"] for row in reversed(urls)],
            "data": [row["click_count"] for row in reversed(urls)],
        }
    )


if __name__ == "__main__":
    init_dirs()
    with app.app_context():
        init_db()
    app.run(debug=True)
