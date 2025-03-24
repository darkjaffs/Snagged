from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/jobs", methods=["POST"])
def jobs():
    selected_category = request.form.get("category")
    user_email = request.form.get("email")
    return selected_category, user_email


if __name__ == "__main__":
    app.run(debug=True)


