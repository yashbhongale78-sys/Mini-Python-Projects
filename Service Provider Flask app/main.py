
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact")
def contacts():
    return render_template("contacts.html")

@app.route("/about")
def about():
    return render_template("about.html")


app.run(debug=True)