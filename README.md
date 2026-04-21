# URL Shortener System

A premium Flask-based URL shortener with authentication, click tracking, QR codes, and a modern dashboard.

## Features

- Shorten long URLs into unique short links
- Redirect short links to the original destination
- Track click counts
- User registration and login
- Session-based dashboard access
- QR code generation for each link
- Copy button with success alert
- Responsive glassmorphism UI
- Chart.js analytics bar chart

## Tech Stack

- Python
- Flask
- SQLite
- HTML, CSS, JavaScript
- qrcode
- Pillow
- Chart.js

## Folder Structure

```text
URL Shortener System/
├── app.py
├── requirements.txt
├── README.md
├── PROJECT_REPORT.md
├── templates/
├── static/
└── database.db (created automatically)
```

## Setup Instructions

1. Open Terminal inside the project folder.
2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python3 app.py
```

5. Open the local server URL shown in Terminal.

## Common Error Fixes

### 1. `ModuleNotFoundError: No module named 'qrcode'`

This means the required package is not installed in your current Python environment.

Run:

```bash
pip install qrcode[pil] Pillow Flask
```

Or install everything from the requirements file:

```bash
pip install -r requirements.txt
```

If you are using a virtual environment, make sure it is activated first.

### 2. `ModuleNotFoundError: No module named 'flask'`

Install Flask:

```bash
pip install Flask
```

### 3. QR code folder or database not created

The app creates them automatically when you run it, but make sure the project has write permission.

### 4. Port already in use

If another app is using the Flask port, stop that app or change the port in `app.py`.

## How It Works

1. Register or log in.
2. Paste a long URL into the form.
3. The app generates a unique short code.
4. The short link opens the original URL.
5. Each click increases the counter.
6. The dashboard shows all saved URLs and analytics.

## Notes

- The app uses SQLite, so no separate database server is required.
- QR images are saved inside `static/qr/`.
- Short URLs are only manageable by the logged-in owner.

