# Flask Documentation: https://flask.palletsprojects.com/en/stable/ 
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
