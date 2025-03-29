from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        category = request.form["category"]
        email = request.form["email"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT into subscribers (email, category) VALUES (?, ?)", (email, category))
            conn.commit()
        except sqlite3.IntegrityError:
            pass
        finally:
            conn.close()

        return redirect("/")

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)


