from flask import Flask, render_template, request, redirect
from database import insert_users
from dotenv import load_dotenv
import os
from email_service import init_mail, send_email

load_dotenv() 

app = Flask(__name__)

app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = int(os.getenv("MAIL_PORT"))
app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS") == "True"
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")

init_mail(app)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        category = request.form["category"]
        email = request.form["email"]

        insert_users(email,category)

        return redirect("/")

    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)


