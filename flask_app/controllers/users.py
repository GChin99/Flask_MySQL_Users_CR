from flask_app import app
from flask import Flask, render_template, request, redirect#, session
from flask_app.models.user import User #from the models folder, we are importing our Animal class 

@app.route("/")
def groot():
    return redirect("/users")

@app.route("/users")
def all_users():
    # call the query to get all the users from the get_all classmethod in the models folder 
    all_users = User.get_all()
    return render_template("index.html", all_the_users = all_users)

@app.route("/users/new")
def new_user():
    return render_template("new_user.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "uemail" : request.form["uemail"]
    }
    # We pass the data dictionary into the save method from the User class.
    User.save(data)
    # Don't forget to redirect after saving to the database. We do not render_templates on a post method
    return redirect('/users')


