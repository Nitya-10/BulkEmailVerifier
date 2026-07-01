# 📧 Bulk Email Verifier

A Flask-based web application for verifying email addresses in bulk using CSV files. The application validates email syntax, checks domain MX records, processes emails concurrently using multithreading, and generates a downloadable CSV verification report through a simple and responsive web interface.

---

# 🚀 Features

- Upload CSV files containing email addresses
- Email Syntax Validation using Regular Expressions (Regex)
- Domain & MX Record Verification using DNS
- Multi-threaded email verification using ThreadPoolExecutor
- Bulk email processing
- Verification Summary Dashboard
- Displays:
  - Total Emails
  - Valid Emails
  - Bounce Emails
  - Unknown Emails
- Download verification results as CSV
- Responsive and user-friendly web interface

---

# 🏗️ System Architecture

```
CSV Upload
     │
     ▼
Read Email Addresses
     │
     ▼
Regex Validation
     │
     ▼
MX Record Verification
     │
     ▼
Multi-threaded Processing
     │
     ▼
Generate Results CSV
     │
     ▼
Display Dashboard
```

---

# 🛠 Technologies Used

- Python 3
- Flask
- Pandas
- DNSPython
- HTML5
- CSS3
- ThreadPoolExecutor (Concurrent Futures)

---

# 📁 Project Structure

```
BulkEmailVerifier/
│
├── app.py
├── verifier.py
├── requirements.txt
├── README.md
├── Procfile
├── runtime.txt
├── .gitignore
│
├── uploads/
│
├── results/
│
├── templates/
│     └── index.html
│
└── static/
      └── style.css
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Nitya-10/BulkEmailVerifier.git
```

Navigate to the project directory:

```bash
cd BulkEmailVerifier
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 📥 Input

Upload a CSV file containing one email address per row.

Example:

```
Email
john@gmail.com
alice@yahoo.com
test@example.com
```

---

# 📤 Output

The application generates a CSV report containing two columns:

| Email Address | Status |
|---------------|--------|
| john@gmail.com | Valid |
| fake@xyz.com | Bounce |
| test@example.com | Unknown/Error |

---

# ✔ Verification Process

The application currently performs:

1. Email Syntax Validation using Regular Expressions (Regex)
2. Domain Verification
3. MX Record Verification
4. Multi-threaded Processing for faster execution

---

# 📊 Dashboard

The dashboard displays:

- Total Emails
- Valid Emails
- Bounce Emails
- Unknown Emails
- Download Results CSV button
- Email Verification Table

---

# 🚀 Deployment

This application can be deployed on cloud platforms such as:

- Render
- Railway
- Heroku

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

---

# 📦 Requirements

```
Flask
pandas
dnspython
email-validator
aiosmtplib
gunicorn
```

---

# ⚠️ Current Limitations

The current implementation performs syntax validation and MX record verification.

SMTP mailbox verification and Catch-All detection are not fully implemented because many public email providers restrict SMTP mailbox verification. These features are planned as future enhancements.

---

# 🔮 Future Enhancements

- SMTP Mailbox Verification
- Catch-All Detection
- Progress Bar
- Drag-and-Drop CSV Upload
- Excel Export Support
- User Authentication
- Email Verification API
- Docker Deployment

---

# 👨‍💻 Author

**Nitya Gupta**

B.Tech Computer Science Engineering (Cyber Security)

UPES, Dehradun

---

# 📄 License

This project is developed for educational and academic purposes only.