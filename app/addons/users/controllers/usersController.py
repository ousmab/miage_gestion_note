from app.addons.users import users_module
from flask import render_template


@users_module.route("/merci")
def users():
    return render_template("index.html")
