from app.addons.index import index_module
from flask import  render_template

_route = index_module


@_route.route("/")
def index():
    return render_template("index.html")
