from concurrent.futures import ThreadPoolExecutor
from flask import Flask, render_template, request, send_file
import pandas as pd
import os
from concurrent.futures import ThreadPoolExecutor
from verifier import verify_email

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    if file.filename == "":
        return "No file selected"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Read CSV
    df = pd.read_csv(filepath)

    # Get first column as email list
    emails = df.iloc[:, 0].astype(str).tolist()

    # Verify emails using multithreading
    with ThreadPoolExecutor(max_workers=20) as executor:
        statuses = list(executor.map(verify_email, emails))

    results = []

    valid = 0
    bounce = 0
    unknown = 0

    for email, status in zip(emails, statuses):

        if status == "Valid":
            valid += 1

        elif status == "Bounce":
            bounce += 1

        else:
            unknown += 1

        results.append({
            "email": email,
            "status": status
        })

    total = len(results)

    # Save results CSV
    output_df = pd.DataFrame(results)

    output_path = os.path.join(
        RESULT_FOLDER,
        "results.csv"
    )

    output_df.to_csv(output_path, index=False)

    return render_template(
        "index.html",
        results=results,
        total=total,
        valid=valid,
        bounce=bounce,
        unknown=unknown
    )


@app.route("/download")
def download():

    return send_file(
        os.path.join(RESULT_FOLDER, "results.csv"),
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)