from flask import Flask, render_template, request
from db import add_student
import sqlite3

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/students/<id>")
def student(id):
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT name, matric FROM students WHERE id = ?""",
        (id,),
    )
    student = cursor.fetchone()
    conn.close()

    return render_template(
        "student.html", name=student["name"], matric=student["matric"]
    )


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        matric = request.form.get("matric")
        add_student(name, matric)
        return "Submitted successfully"

    return render_template("form.html", success=True)


app.run(debug=True)
