from flask import Blueprint

index_module = Blueprint('index', __name__, template_folder="views")
