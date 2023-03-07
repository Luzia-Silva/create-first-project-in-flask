from flask import render_template
from app import app, db

from app.models.tables import User
from app.models.forms import LoginForm

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    login = LoginForm()
    if login.validate_on_submit():
       login_user(user)
    else :
        print(login.errors)
    return render_template("login.html", login=login)   

# CRUD
# Create 
@app.route("/createuser/<info>")
@app.route("/createuser", defaults={"info": None})
def createUser(info):
    if info: 
        create_user = User("anajulisxy", "1234", "Ana Júlia",  "anajulisxy@gmail.com")
        db.session.add(create_user)
        db.session.commit()
        return "CREATE USER SUCESS!"
    else: 
        return "<a href='/login'>This user already exists in our database, login</a>"

#Read
@app.route("/readuser/<info>")
@app.route("/readuser", defaults={"info": None})
def readUser(info):
        read_user = User.query.filter_by(password="1234").all()
        print(read_user)
        return "READ USER SUCESS! LOOK AT THE TERMINAL"
    
#Update
@app.route("/update/<info>")
@app.route("/update", defaults={"info": None})
def updateUser(info):
        update_user = User.query.filter_by(id = 1).first()
        update_user.name = "Sabrina Abreu da Silva Santos"
        db.session.add(update_user)
        db.session.commit()
        return "UPDATE USER SUCESS!"
    
#Delete
@app.route("/delete/<info>")
@app.route("/delete", defaults={"info": None})
def deleteUser(info):
        delete_user = User.query.filter_by(id = 1).first()
        db.session.delete(delete_user)
        db.session.commit()
        return "DELETE USER SUCESS!"