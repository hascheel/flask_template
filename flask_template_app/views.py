from flask import Flask
from flask import render_template
from . import app

@app.route("/")
def home():
    return render_template("home.html", title="Flask Template",)

@app.route("/camera")
def camera():
    return render_template("camera.html")

@app.route("/about/")
def about():
    return render_template("about.html")