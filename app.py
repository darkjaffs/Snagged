from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/jobs", methods=["POST"])
def jobs():
    selected_category = request.form.get("category")
    return f"{selected_category}"


if __name__ == "__main__":
    app.run(debug=True)


