import os
import json
from flask import Flask

app = Flask(__name__)

data_file = "data.json"

@app.route("/")
def index():
    filepath = os.path.join(os.getcwd(), data_file)

    file_content = read_data_file(filepath)


def read_data_file(filepath):
    """
    Reads the content of the file handler passed in,
    deserializes it into a python object and returns the object
    """
    with open(filepath, "r") as fh:
        content = fh.read()
        if len(content) > 0:
            json_content = json.loads(content)
        else:
            json_content = {}

    return json_content