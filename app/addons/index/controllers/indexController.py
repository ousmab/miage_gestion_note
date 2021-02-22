from app.addons.index import index_module


@index_module.route("/index")
def index():
    return "index  blueprint oooy"
