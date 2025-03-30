from flask import Flask, render_template, request, redirect
from database import insert_users

app = Flask(__name__)

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


