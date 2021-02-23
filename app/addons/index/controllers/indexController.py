from app.addons.index import index_module

_route = index_module


@_route.route("/index")
def index():
    return "index  blueprint oooy"
