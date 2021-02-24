from app.addons.users import users_module
from flask import render_template
from ..models.userModel import UserModel
from flask_login import login_user, logout_user, login_required

_route = users_module


@_route.route("/")
def home():
    user = UserModel.query.filter_by(email="aboousmane@gmail").first()
    login_user(user)
    return render_template("home.html", user=user)


@_route.route("/dashboard")
@login_required
def dash():
    return "your a logged in dash"


@_route.route("/logout")
def logout():
    logout_user()
    return "logout out"
