import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape


OUTPUT = Path("URL_Shortener_PBL_Report.docx")


def paragraph(text="", style=None, align=None, bold=False, size=None, page_break=False):
    props = []
    if style:
        props.append(f"<w:pStyle w:val=\"{style}\"/>")
    if align:
        props.append(f"<w:jc w:val=\"{align}\"/>")
    if page_break:
        run = "<w:r><w:br w:type=\"page\"/></w:r>"
    else:
        run_props = []
        if bold:
            run_props.append("<w:b/>")
        if size:
            run_props.append(f"<w:sz w:val=\"{size}\"/><w:szCs w:val=\"{size}\"/>")
        run_prop_xml = f"<w:rPr>{''.join(run_props)}</w:rPr>" if run_props else ""
        run = f"<w:r>{run_prop_xml}<w:t xml:space=\"preserve\">{escape(text)}</w:t></w:r>"
    prop_xml = f"<w:pPr>{''.join(props)}</w:pPr>" if props else ""
    return f"<w:p>{prop_xml}{run}</w:p>"


def bullet(text):
    return (
        "<w:p><w:pPr><w:pStyle w:val=\"Normal\"/><w:numPr><w:ilvl w:val=\"0\"/>"
        "<w:numId w:val=\"1\"/></w:numPr></w:pPr>"
        f"<w:r><w:t xml:space=\"preserve\">{escape(text)}</w:t></w:r></w:p>"
    )


def number(text):
    return (
        "<w:p><w:pPr><w:pStyle w:val=\"Normal\"/><w:numPr><w:ilvl w:val=\"0\"/>"
        "<w:numId w:val=\"2\"/></w:numPr></w:pPr>"
        f"<w:r><w:t xml:space=\"preserve\">{escape(text)}</w:t></w:r></w:p>"
    )


content = []

content += [
    paragraph("ITS ENGINEERING COLLEGE, GREATER NOIDA", "Heading1", "center"),
    paragraph("Department of Computer Science and Engineering", "Heading2", "center"),
    paragraph(""),
    paragraph(""),
    paragraph("Project Based Learning Report", "Heading2", "center"),
    paragraph("on", None, "center", bold=True),
    paragraph("URL SHORTENER SYSTEM", "Title", "center"),
    paragraph(""),
    paragraph("Submitted By", "Heading2", "center"),
    paragraph("Student 1 Name (Roll No.)", None, "center"),
    paragraph("Student 2 Name (Roll No.)", None, "center"),
    paragraph("Student 3 Name (Roll No.)", None, "center"),
    paragraph("Student 4 Name (Roll No.)", None, "center"),
    paragraph(""),
    paragraph("COURSE : B.Tech. (CSE)", None, "center", bold=True),
    paragraph("SEMESTER : III", None, "center", bold=True),
    paragraph("SUBJECT : Python Programming", None, "center", bold=True),
    paragraph("SUBJECT CODE : BCC302", None, "center", bold=True),
    paragraph("FACULTY NAME : ____________________", None, "center", bold=True),
    paragraph(""),
    paragraph("(2025-2026)", None, "center", bold=True),
    paragraph(page_break=True),
    paragraph("Certificate", "Heading1", "center"),
    paragraph(
        "This is to certify that the Project Based Learning (PBL) report entitled "
        "\"URL Shortener System\" has been successfully carried out by the following "
        "students of B.Tech. (Computer Science and Engineering), Semester III, as a "
        "part of the Project Based Learning during the academic session 2025-2026."
    ),
    paragraph("Submitted by:", bold=True),
    bullet("Name: ____________________    Roll No.: __________"),
    bullet("Name: ____________________    Roll No.: __________"),
    bullet("Name: ____________________    Roll No.: __________"),
    bullet("Name: ____________________    Roll No.: __________"),
    paragraph(
        "The work has been completed under the guidance of ____________________. "
        "The project is a part of continuous internal assessment under the PBL "
        "framework and reflects the students' effort in applying theoretical knowledge "
        "to solve a practical real-world problem. To the best of our knowledge, this "
        "work is original and has not been submitted elsewhere for any other academic purpose."
    ),
    paragraph(""),
    paragraph("Faculty Guide", bold=True),
    paragraph("Signature: ____________________"),
    paragraph("Name: ____________________"),
    paragraph(page_break=True),
]

sections = [
    ("Abstract", [
        "The URL Shortener System is a web-based application developed to transform long and complex web addresses into short, manageable, and shareable links. In the digital environment, lengthy URLs are difficult to remember, inconvenient to share in social media posts, and unsuitable for printed resources such as posters or handouts. This project addresses that problem by providing a secure and user-friendly platform through which users can generate short URLs, monitor click counts, and manage all created links through a personal dashboard. The system is built using Python and Flask for the backend, SQLite for database management, and HTML, CSS, JavaScript, and Chart.js for the frontend interface and analytics visualization. Additional features such as QR code generation, copy-to-clipboard functionality, user authentication, and a responsive premium user interface improve the usefulness of the application. The final outcome is a beginner-friendly yet professionally structured project that demonstrates web development, database integration, session management, data tracking, and user interface design in one complete system."
    ]),
    ("1. Problem Statement", [
        "Internet users frequently work with long URLs that are difficult to share, visually unattractive, and hard to manage. These problems become more noticeable in academic work, business promotion, social media marketing, and printed communication materials. A simple and efficient system is needed to convert long URLs into short links while preserving the original destination, tracking usage, and allowing users to manage their links securely. The relevance of this problem is high because shortened links are widely used in digital campaigns, product promotions, mobile sharing, and analytics-based web applications."
    ]),
    ("2. Objectives", [
        ("number", "To design and develop a Flask-based web application for shortening long URLs."),
        ("number", "To generate unique short codes for each original URL."),
        ("number", "To implement user registration, login, and session-based authentication."),
        ("number", "To provide a dashboard for managing shortened URLs and monitoring click counts."),
        ("number", "To integrate QR code generation and graphical analytics for improved usability."),
    ]),
    ("3. Methodology", [
        ("sub", "3.1 Development Approach"),
        "The project follows an incremental development methodology. The system was first planned module by module, starting from authentication and database design, followed by core URL shortening logic, dashboard creation, analytics integration, and interface enhancement. Each module was tested individually before integration into the full application.",
        ("sub", "3.2 Step-by-Step Workflow"),
        ("number", "Study the problem and identify the functional requirements."),
        ("number", "Design the database tables for users and URL records."),
        ("number", "Develop authentication routes for user registration and login."),
        ("number", "Create the URL shortening mechanism and unique short code generation logic."),
        ("number", "Implement redirection from short URL to original URL."),
        ("number", "Track every click by incrementing the stored click count."),
        ("number", "Generate QR codes for each shortened URL."),
        ("number", "Build a modern responsive user interface for the home page and dashboard."),
        ("number", "Display click analytics using Chart.js."),
        ("number", "Test the application for correct functionality and usability."),
        ("sub", "3.3 Tools and Technologies Used"),
        "Programming Language: Python 3",
        "Web Framework: Flask",
        "Database: SQLite",
        "Frontend: HTML, CSS, JavaScript",
        "Charting Library: Chart.js",
        "QR Code Library: qrcode",
        "Image Processing: Pillow",
    ]),
    ("4. System Design / Architecture", [
        ("sub", "4.1 Architecture Overview"),
        "The URL Shortener System follows a three-layer architecture consisting of presentation layer, application layer, and data layer. The presentation layer handles user interaction through HTML templates and CSS styling. The application layer contains the Flask routes, business logic, session handling, and request processing. The data layer uses SQLite for storing registered users, original URLs, short codes, and click counts.",
        ("sub", "4.2 Block Flow"),
        "User Input -> Flask Route -> Validation -> Database Storage -> Short URL Generation -> Dashboard Display -> Redirect Route -> Click Count Update -> Analytics Chart",
        ("sub", "4.3 Workflow Explanation"),
        ("bullet", "The user first registers and logs in to the application."),
        ("bullet", "After authentication, the user enters a long URL in the dashboard form."),
        ("bullet", "The application validates the URL and generates a unique short code."),
        ("bullet", "The original URL and short code are stored in the SQLite database."),
        ("bullet", "The system creates a QR code image for the short link."),
        ("bullet", "When the short URL is visited, the system redirects to the original URL."),
        ("bullet", "The click count is updated every time the short URL is accessed."),
        ("bullet", "The dashboard displays all saved URLs and their click analytics."),
        ("sub", "4.4 Database Design"),
        "users table: id, name, email, password_hash, created_at",
        "urls table: id, user_id, original_url, short_code, click_count, created_at",
    ]),
    ("5. Implementation", [
        ("sub", "5.1 Project Structure"),
        "app.py, templates/base.html, templates/index.html, templates/login.html, templates/register.html, templates/dashboard.html, static/style.css, static/script.js, static/dashboard.js, static/qr/",
        ("sub", "5.2 Main Functional Modules"),
        ("bullet", "Authentication Module: Handles registration, login, logout, and session management."),
        ("bullet", "URL Shortening Module: Generates short codes and stores URL mappings."),
        ("bullet", "Redirection Module: Redirects the short URL to the original destination."),
        ("bullet", "Analytics Module: Displays click counts using a bar chart."),
        ("bullet", "QR Module: Generates QR code images for each shortened link."),
        ("sub", "5.3 Key Functions Used"),
        "init_db(): Creates database tables if they do not exist",
        "generate_unique_code(): Produces a unique short code for a URL",
        "shorten_url(): Saves original URL and short code in the database",
        "redirect_short_url(): Redirects a short URL and updates click count",
        "dashboard(): Displays user-created URLs and analytics data",
        ("sub", "5.4 Interface Implementation"),
        "The frontend was designed with a premium and modern look using white and light-orange color tones, layered sections, hover effects, button animations, and a responsive layout. The home page presents the project like a product landing page, while the dashboard provides a practical management view for user-created links."
    ]),
    ("6. Results and Analysis", [
        ("sub", "6.1 Results Obtained"),
        ("bullet", "Converts long URLs into short shareable links."),
        ("bullet", "Redirects the short URLs correctly to the original web pages."),
        ("bullet", "Tracks the number of clicks for each shortened link."),
        ("bullet", "Allows registered users to manage only their own links."),
        ("bullet", "Generates QR codes automatically for each short link."),
        ("bullet", "Displays graphical analytics using Chart.js."),
        ("sub", "6.2 Analysis"),
        "The system performs efficiently for small to medium-scale usage because SQLite offers fast local storage and Flask processes requests quickly for this project size. The use of session-based login improves privacy by restricting dashboard access to authenticated users only. The click count mechanism allows the user to observe link performance in real time. QR code support adds practical value by enabling offline-to-online redirection through mobile scanning.",
        ("sub", "6.3 Sample Observation Table"),
        "Create Short URL - Valid long URL - Short URL generated - Successful",
        "Custom Code Entry - Unique custom code - Custom short URL created - Successful",
        "Redirect Test - Short URL click - Open original URL - Successful",
        "Analytics Update - Repeated clicks - Click count increases - Successful",
    ]),
    ("7. Applications and Future Scope", [
        ("sub", "7.1 Applications"),
        ("bullet", "Social media and digital marketing campaigns"),
        ("bullet", "College event promotion and QR-based announcements"),
        ("bullet", "Business product links and customer engagement campaigns"),
        ("bullet", "Portfolio projects and personal branding"),
        ("bullet", "Printed posters, brochures, and presentations"),
        ("sub", "7.2 Future Scope"),
        ("bullet", "Adding custom branded domains for short links"),
        ("bullet", "Supporting link expiration dates"),
        ("bullet", "Adding edit and delete operations for URLs"),
        ("bullet", "Introducing advanced analytics such as browser, location, and device data"),
        ("bullet", "Providing an admin panel for full system monitoring"),
        ("bullet", "Deploying the application on a cloud server for permanent public access"),
    ]),
    ("8. Conclusion", [
        "The URL Shortener System successfully demonstrates how Python and Flask can be used to build a complete real-world web application. The project combines backend logic, database management, authentication, data tracking, QR generation, analytics, and modern interface design in a single integrated solution. It is educationally valuable because it helps students understand practical software development concepts and industrially relevant because URL shortening services are widely used in digital communication. The project is therefore suitable for college submission as well as portfolio presentation."
    ]),
    ("9. References", [
        ("number", "Flask Documentation. Available at: https://flask.palletsprojects.com/"),
        ("number", "Python Documentation. Available at: https://docs.python.org/3/"),
        ("number", "SQLite Documentation. Available at: https://www.sqlite.org/docs.html"),
        ("number", "Chart.js Documentation. Available at: https://www.chartjs.org/docs/latest/"),
        ("number", "qrcode Python Package Documentation. Available at: https://pypi.org/project/qrcode/"),
        ("number", "Pillow Documentation. Available at: https://pillow.readthedocs.io/"),
    ]),
    ("10. Annexure", [
        ("sub", "10.1 Software and Hardware Requirements"),
        "Operating System: Windows / macOS / Linux",
        "Programming Language: Python 3",
        "Editor / IDE: VS Code / PyCharm / Codex environment",
        "RAM: 4 GB or above",
        "Storage: 500 MB free space minimum",
        ("sub", "10.2 Project Highlights"),
        ("bullet", "Beginner-friendly implementation with professional output"),
        ("bullet", "Secure user login and session handling"),
        ("bullet", "Interactive dashboard with click analytics"),
        ("bullet", "QR code generation for every short link"),
        ("bullet", "Responsive premium interface for portfolio use"),
        ("sub", "10.3 GitHub / Deployment Link"),
        "Add your GitHub repository link here: ________________________________",
    ]),
]

for heading, items in sections:
    content.append(paragraph(heading, "Heading1"))
    for item in items:
        if isinstance(item, tuple):
            kind, value = item
            if kind == "sub":
                content.append(paragraph(value, "Heading2"))
            elif kind == "bullet":
                content.append(bullet(value))
            elif kind == "number":
                content.append(number(value))
        else:
            content.append(paragraph(item))


document_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"
 xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006"
 xmlns:o="urn:schemas-microsoft-com:office:office"
 xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
 xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math"
 xmlns:v="urn:schemas-microsoft-com:vml"
 xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing"
 xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
 xmlns:w10="urn:schemas-microsoft-com:office:word"
 xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
 xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml"
 xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup"
 xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk"
 xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml"
 xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape"
 mc:Ignorable="w14 wp14">
<w:body>
{''.join(content)}
<w:sectPr>
  <w:pgSz w:w="12240" w:h="15840"/>
  <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/>
</w:sectPr>
</w:body>
</w:document>
"""


styles_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:docDefaults>
    <w:rPrDefault>
      <w:rPr>
        <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
        <w:sz w:val="24"/>
        <w:szCs w:val="24"/>
      </w:rPr>
    </w:rPrDefault>
  </w:docDefaults>
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:line="360" w:lineRule="auto"/></w:pPr>
    <w:rPr>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:cs="Times New Roman"/>
      <w:sz w:val="24"/>
      <w:szCs w:val="24"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Title">
    <w:name w:val="Title"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:jc w:val="center"/><w:spacing w:before="160" w:after="120"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="36"/><w:szCs w:val="36"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="200" w:after="100"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="30"/><w:szCs w:val="30"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr><w:spacing w:before="160" w:after="80"/></w:pPr>
    <w:rPr><w:b/><w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr>
  </w:style>
</w:styles>
"""


numbering_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:lvl w:ilvl="0">
      <w:numFmt w:val="bullet"/>
      <w:lvlText w:val="•"/>
      <w:lvlJc w:val="left"/>
      <w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr>
    </w:lvl>
  </w:abstractNum>
  <w:abstractNum w:abstractNumId="1">
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/>
      <w:numFmt w:val="decimal"/>
      <w:lvlText w:val="%1."/>
      <w:lvlJc w:val="left"/>
      <w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr>
    </w:lvl>
  </w:abstractNum>
  <w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
  <w:num w:numId="2"><w:abstractNumId w:val="1"/></w:num>
</w:numbering>
"""


content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""


rels_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""


document_rels = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>
"""


timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

core_xml = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
 xmlns:dc="http://purl.org/dc/elements/1.1/"
 xmlns:dcterms="http://purl.org/dc/terms/"
 xmlns:dcmitype="http://purl.org/dc/dcmitype/"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>URL Shortener System PBL Report</dc:title>
  <dc:creator>Codex</dc:creator>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{timestamp}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{timestamp}</dcterms:modified>
</cp:coreProperties>
"""


app_xml = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
 xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office Word</Application>
</Properties>
"""


with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as docx:
    docx.writestr("[Content_Types].xml", content_types)
    docx.writestr("_rels/.rels", rels_xml)
    docx.writestr("docProps/core.xml", core_xml)
    docx.writestr("docProps/app.xml", app_xml)
    docx.writestr("word/document.xml", document_xml)
    docx.writestr("word/styles.xml", styles_xml)
    docx.writestr("word/numbering.xml", numbering_xml)
    docx.writestr("word/_rels/document.xml.rels", document_rels)

print(f"Created {OUTPUT}")
