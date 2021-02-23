from flask import Flask
from importlib import import_module


app = Flask(__name__, static_folder="core/static", template_folder="core/templates")

# load the config file

try:
    app.config.from_pyfile("config.py")
except IOError as e:
    raise IOError("Configuration error : config.py not found ! ", e)

# import different blueprint and controllers
for addon in app.config["ADDONS"]:
    module = import_module(addon['path'], package='app')
    if addon['url']:
        app.register_blueprint(getattr(module, "__route"), url_prefix=addon['url'])
    else:
        app.register_blueprint(getattr(module, "__route"))

# app configuration

# extensions configuration

