from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from web_modules import login_required, a_error
from cs50 import SQL
import random

# Create a Flask application instance
app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Credits  --^ cs50

db = SQL("sqlite:///notes.db")

# Boilerplate code for the session, non persisting cookies and such.
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/', methods=["GET"])
@login_required
def index():
    return render_template("index.html")

@app.route('/help', methods=["GET"])
@login_required
def help():
    return render_template("help.html")

@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return a_error("Bad request","Form information not found")

        # Check if account exists
        rows = db.execute(
        "SELECT * FROM users WHERE username = ?;",
        username,
        )
        if rows and check_password_hash(rows[0]["hash"], password):
            session["user_id"] = rows[0]["id"]
            return redirect("/")
        else:
            return a_error("400","Account not found.") # Implement flash soon.
            #return render_template("login.html")

    return render_template("login.html")

@app.route('/credits', methods=["GET"])
def credits():
    return render_template("credits.html")

@app.route('/register', methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        check = request.form.get('confirm') # confirm password
        if not username or not password or not check:
            return a_error("Bad request","Form information not found")

        if password != check:
            return a_error("400","Password and confirm password dont match") # Change this to JS later

        # Proceed to account creation

        # check if account exists
        rows = db.execute("SELECT * FROM users WHERE username = ?;", username)
        if rows:
            return a_error("400","Username already taken")
            #return redirect("/login")

        p_hash = generate_password_hash(password)
        # create the account
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?);", username, p_hash)
        return redirect("/login")

    return render_template("register.html")

@app.route('/logout', methods=["GET","POST"])
def logout():
    session.clear() # Removes the current session in memory
    return redirect("/")

def getNotes():
    return db.execute("SELECT * FROM user_notes WHERE user_id = ?", session["user_id"])

@app.route('/notes', methods=["GET","POST"])
@login_required
def notes():
    # render the notes under the users profile
    if request.method == "POST": # User is saving/creating note
        data = request.get_json()
        action = data.get("actionType")
        noteName = data.get("NoteName")
        newName = data.get("NewName")
        entry = data.get("Entry")

        if action == "CREATE":
            db.execute("INSERT INTO user_notes (user_id, name, entry) VALUES(?, ?, ?)", session["user_id"], "Unnamed Note_" + str(random.randint(1,999999999)), "Empty")

        elif action == "SAVE":
            if not noteName or not newName or not entry:
                return a_error("400", "Bad Request")

            nameIsTaken = any( (note.get("name") == newName)  for note in getNotes() ) # 'Any' Checks for at least one truth in a list.

            if nameIsTaken: # Does not change the name at all, but changes the entry value.
                db.execute("UPDATE user_notes SET name = ?, entry = ? WHERE user_id = ? AND name = ?", noteName, entry, session["user_id"], noteName )
            else:
                db.execute("UPDATE user_notes SET name = ?, entry = ? WHERE user_id = ? AND name = ?", newName, entry, session["user_id"], noteName )

        elif action == "DELETE":

            if not noteName:
                return a_error("400", "Bad Request")

            db.execute("DELETE FROM user_notes WHERE user_id = ? AND name = ?", session["user_id"], noteName)

    return render_template("notes.html", Notes = getNotes())
