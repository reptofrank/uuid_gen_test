from flask import Flask

app = Flask(__name__)

data_file = "data.json"

@app.route("/")
def index():
    return "Welcome to Cowrywise"