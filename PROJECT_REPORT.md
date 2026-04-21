# URL Shortener System Project Report

## 1. Abstract
The URL Shortener System is a full-stack web application developed using Flask, SQLite, HTML, CSS, JavaScript, qrcode, and Pillow. The system converts long URLs into short, shareable links and provides secure user authentication so that each user can manage only their own shortened links. The application also tracks click counts, generates QR codes, and presents analytics in a modern dashboard with an interactive bar chart. The project is designed to be beginner-friendly while still looking professional enough for college submission and portfolio presentation.

## 2. Problem Statement
Long URLs are difficult to share, visually unappealing, and inconvenient for printing or posting on social media. Users need a secure system that can shorten URLs, store them for later access, track usage statistics, and provide a visually polished interface. The challenge is to build this system with a lightweight stack that is easy to understand and deploy.

## 3. Objectives
1. Build a URL shortening service with unique short codes.
2. Provide user registration, login, and session-based authentication.
3. Allow logged-in users to create and manage saved short URLs.
4. Track click counts for every shortened link.
5. Display analytics using a bar chart.
6. Generate QR codes for every link.
7. Deliver a modern, responsive, and professional UI.

## 4. Methodology
The project follows a simple web application workflow:
1. User registers and logs in.
2. The application stores user credentials securely using password hashing.
3. When a URL is submitted, the system validates it and generates a unique short code.
4. The mapping between the original URL and short code is saved in SQLite.
5. When the short URL is visited, the system increments the click count and redirects the user.
6. The dashboard fetches the user’s URLs and visualizes the click data using Chart.js.
7. A QR code is generated for each shortened link and stored in the static folder.

## 5. System Design
### 5.1 Architecture
The system uses a simple three-layer structure:
- Presentation layer: HTML templates, CSS, and JavaScript
- Application layer: Flask routes and business logic
- Data layer: SQLite database

### 5.2 Modules
- Authentication module
- URL shortening module
- Redirection module
- Dashboard and analytics module
- QR code generation module

### 5.3 Database Design
Two main tables are used:
- `users`: stores user profile information, email, password hash, and creation date
- `urls`: stores original URLs, short codes, click counts, user ownership, and timestamps

## 6. Implementation
### 6.1 Backend
The backend is built with Flask. It includes routes for:
- Home page
- Registration
- Login
- Logout
- URL shortening
- URL redirection
- Dashboard
- QR code serving
- JSON analytics API

### 6.2 Authentication
The system uses session management to keep users logged in. Passwords are never stored in plain text. Instead, Werkzeug password hashing is used for secure storage.

### 6.3 URL Shortening Logic
Short codes are generated using secure random character selection. If a custom short code is entered, the system checks that it is unique before saving it.

### 6.4 Click Tracking
Whenever a short URL is accessed, the system locates the associated record in the database and increases the click count by one before redirecting to the destination URL.

### 6.5 QR Code Generation
Each newly created short link gets a QR code image generated using the `qrcode` library and Pillow. The QR code is saved as a PNG file in the static QR folder.

### 6.6 Frontend Design
The interface uses glassmorphism, gradient backgrounds, rounded cards, hover effects, and responsive layouts. The dashboard includes a Chart.js bar chart to show click analytics.

## 7. Results and Analysis
The final application successfully performs all required tasks:
- It shortens URLs reliably.
- It redirects users to the correct destination.
- It tracks the number of clicks for each short link.
- It supports authenticated access to personal dashboards.
- It generates QR codes and displays analytics visually.

The system is lightweight, easy to run locally, and suitable for academic demonstrations. Since SQLite is used, the project remains portable and requires minimal setup.

## 8. Applications
The system can be used in:
- College projects and demonstrations
- Personal branding and portfolio use
- Small businesses for link sharing
- Event promotions and printed posters
- Social media campaigns

## 9. Future Scope
Possible improvements include:
- Custom domain support
- Link expiration dates
- Password-protected links
- Email verification
- Detailed analytics such as geolocation and browser tracking
- Admin panel for system-wide monitoring
- API-based URL creation

## 10. Conclusion
The URL Shortener System is a complete, practical, and visually polished web application built with Flask and SQLite. It demonstrates core web development concepts such as authentication, database integration, route handling, analytics, and UI design. The project is suitable for college submission, learning, and portfolio showcase.

## 11. References
1. Flask Official Documentation
2. Python Official Documentation
3. SQLite Official Documentation
4. Chart.js Documentation
5. qrcode Python Library Documentation
6. Pillow Documentation

## 12. Annexure
### 12.1 File Structure
- `app.py`
- `requirements.txt`
- `templates/base.html`
- `templates/index.html`
- `templates/login.html`
- `templates/register.html`
- `templates/dashboard.html`
- `static/style.css`
- `static/script.js`
- `static/dashboard.js`

### 12.2 Sample Run Steps
1. Install dependencies using `pip install -r requirements.txt`
2. Run the application with `python app.py`
3. Open the local server in the browser
4. Register a new user
5. Login and create short URLs
6. View analytics and QR codes on the dashboard

### 12.3 Notes
- The project uses SQLite for simplicity.
- The UI is responsive and suitable for desktop and mobile.
- All major code blocks include comments or clear structure for beginner understanding.
