from flask import Flask
from app.addons.index import index_module
from app.addons.users import users_module
import app.addons.index.controllers.indexController
import app.addons.users.controllers.usersController

app = Flask(__name__, static_folder="core/static", template_folder="core/templates")

# CONFIGURATION

# EXTENTION FLASK


# ENREGISTREMENT DES MODULES

# IMPORT DES CONTROLLEURS
app.register_blueprint(index_module)  # bluprint
app.register_blueprint(users_module, url_prefix="/users")
"""
@app.route("/")
def home():
    return "merci"
"""
