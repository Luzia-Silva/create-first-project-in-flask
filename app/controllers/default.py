from flask import render_template
from app import app

from app.models.forms import LoginForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    login = LoginForm()
    if login.validate_on_submit():
        print(login.username.data)
    else :
        print(login.form_errors)
    return render_template("login.html", login=login)   