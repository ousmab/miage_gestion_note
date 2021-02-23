from app.addons.users import users_module
from flask import render_template

__route = users_module


@__route.route("/merci")
def users():
    return render_template("index.html")
