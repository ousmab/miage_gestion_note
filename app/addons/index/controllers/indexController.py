from app.addons.index import index_module

__route = index_module


@__route.route("/index")
def index():
    return "index  blueprint oooy"
