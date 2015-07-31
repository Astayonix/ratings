"""Movie Ratings."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import User, Rating, Movie, connect_to_db, db


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/', methods=["POST", "GET"])
def index():
    """Homepage."""

    return render_template('homepage.html')

@app.route("/users")
def user_list():
    """Show all users."""


    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/login", methods = ['POST', "GET"])
def login():
    """Login form handling"""

    if request.method == 'POST':
        flash("You're In Like Flynn!")
        return render_template("homepage.html")
    return render_template("login.html")

    email = request.form.get("email")
    password = request.form.get("password")
    zipcode = request.form.get("zipcode")
    age = request.form.get("age")

    # if 
    # new_user = User(first = first,  age = age, zipcode = zipcode, email = email, password = password)
    #     db.session.add(new_user)
    # db.session.commit()

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()