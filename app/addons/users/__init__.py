from flask import Blueprint

users_module = Blueprint('users', __name__, template_folder="views")
