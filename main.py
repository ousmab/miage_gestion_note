from app import app
from flask import  render_template



@app.errorhandler(404)
def error():
    return render_template("404.html"), 404




# extensions configuration