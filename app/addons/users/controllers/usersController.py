from app.addons.users import users_module
from flask import render_template

_route = users_module


@_route.route("/")
def users():
    return render_template("index.html")



