# 📧 Bulk Email Verifier

A Flask-based web application that verifies bulk email addresses uploaded through a CSV file. The application validates email syntax, checks MX (Mail Exchange) records, processes emails using multithreading for better performance, and generates a downloadable CSV report.

---

## 🚀 Features

- Upload CSV files containing email addresses
- Email Syntax Validation using Regular Expressions (Regex)
- Domain & MX Record Verification using DNS
- Multi-threaded email processing using ThreadPoolExecutor
- Bulk email verification
- Verification Summary Dashboard
- Displays:
  - Total Emails
  - Valid Emails
  - Bounce Emails
  - Unknown Emails
- Download verification results as CSV
- Clean and responsive web interface

---

## 🛠 Technologies Used

- Python 3
- Flask
- Pandas
- DNSPython
- HTML5
- CSS3
- ThreadPoolExecutor (Concurrent Futures)

---

## 📁 Project Structure

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

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/BulkEmailVerifier.git
```

Go to the project folder:

```bash
cd BulkEmailVerifier
```

Install dependencies:

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

## 📥 Input

Upload a CSV file containing one email address per row.

Example:

```
Email
john@gmail.com
alice@yahoo.com
test@example.com
```

---

## 📤 Output

The application generates a CSV file containing:

| Email Address | Status |
|---------------|--------|
| john@gmail.com | Valid |
| fake@xyz.com | Bounce |
| test@example.com | Unknown |

---

## ✔ Verification Process

The application performs the following checks:

1. Email Syntax Validation using Regex
2. Domain Verification
3. MX Record Verification
4. Multi-threaded Processing for faster execution

---

## 📊 Dashboard

The web dashboard displays:

- Total Emails
- Valid Emails
- Bounce Emails
- Unknown Emails
- Download Results CSV button
- Email verification table

---

## 📸 Screenshots

Add screenshots here before submitting:

- Home Page
- CSV Upload
- Verification Dashboard
- Downloaded Results CSV

---

## 📦 requirements.txt

```
Flask
pandas
dnspython
email-validator
aiosmtplib
gunicorn
```

---

## 🚀 Deployment

This project can be deployed on:

- Render
- Railway
- Heroku
- Vercel (Frontend only)

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
gunicorn app:app
```

---

## 🔮 Future Improvements

- SMTP Mailbox Verification
- Catch-All Detection
- Progress Bar
- User Authentication
- Email Export in Excel Format
- Advanced Analytics Dashboard

---

## 👨‍💻 Author

**Nitya Gupta**

B.Tech Computer Science Engineering (Cyber Security)

UPES, Dehradun

---

## 📄 License

This project is developed for educational and academic purposes.
