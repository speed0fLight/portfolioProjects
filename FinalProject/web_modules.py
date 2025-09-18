from flask import redirect, render_template, session
from functools import wraps

def login_required(f):
    """
    CS50 function that asserts the user is logged in.
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

def a_error(errorType, errorMessage):
    # should redirect the user to a page that has a error header and a error message
    return render_template("error.html", Error = errorType, ErrorMessage = errorMessage)
