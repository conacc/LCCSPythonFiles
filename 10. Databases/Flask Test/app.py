# app.py
from flask import Flask, render_template, request, Response, send_file
import csv
 
app = Flask(__name__)
 
# Sample data for demonstration
users = []
 
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        users.append({"name": name, "email": email})
     
    return render_template("index.html", csv_data=users)
 
@app.route("/generate_csv")
def generate_csv():
    if len(users) == 0:
        return "No data to generate CSV."
 
    # Create a CSV string from the user data
    csv_data = "Name,Email\n"
    for user in users:
        csv_data += f"{user['name']},{user['email']}\n"
 
    return render_template("index.html", csv_data=csv_data)
 
@app.route("/download_csv")
def download_csv():
    if len(users) == 0:
        return "No data to download."
 
    # Create a CSV string from the user data
    csv_data = "Name,Email\n"
    for user in users:
        csv_data += f"{user['name']},{user['email']}\n"
 
    # Create a temporary CSV file and serve it for download
    with open("users.csv", "w") as csv_file:
        csv_file.write(csv_data)
 
    return send_file("users.csv", as_attachment=True, download_name="users.csv")
 
@app.route("/download_csv_direct")
def download_csv_direct():
    if len(users) == 0:
        return "No data to download."
 
    # Create a CSV string from the user data
    csv_data = "Name,Email\n"
    for user in users:
        csv_data += f"{user['name']},{user['email']}\n"
 
    # Create a direct download response with the CSV data and appropriate headers
    response = Response(csv_data, content_type="text/csv")
    response.headers["Content-Disposition"] = "attachment; filename=users.csv"
 
    return response
 
if __name__ == "__main__":
    app.run(host = "localhost", port = 8010)