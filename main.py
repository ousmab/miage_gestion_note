from app import app
from flask import render_template
from flask_login import LoginManager
from app.addons.users.models.userModel import UserModel


@app.errorhandler(404)
def error():
    return render_template("404.html"), 404


# handling user connections
login_manager = LoginManager()
login_manager.init_app(app=app)


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(int(user_id))


