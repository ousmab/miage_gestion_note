from flask import Flask
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.env import ENV


app = Flask(__name__, static_folder="core/static", template_folder="core/templates")

# app configuration
app.config["SQLALCHEMY_DATABASE_URI"] = ENV["DATABASE_URI"]
app.config["SECRET_KEY"] = ENV["SECRET_KEY"]

# load the config file

try:
    app.config.from_pyfile("config.py")
except IOError as e:
    raise IOError("Configuration error : config.py not found ! ", e)

# import different blueprint and controllers
for addon in app.config["ADDONS"]:
    module = import_module(addon['path'], package='app')
    if addon['url']:
        app.register_blueprint(getattr(module, "_route"), url_prefix=addon['url'])
    else:
        app.register_blueprint(getattr(module, "_route"))


# app extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

