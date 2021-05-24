import os
import json
import time
from uuid import uuid4
from flask import Flask

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

data_file = "data.json"

@app.route("/")
def index():
    filepath = os.path.join(os.getcwd(), data_file)

    data = read_data_file(filepath)

    now = time.strftime("%Y-%m-%d %H:%M:%S")
    new_uuid = uuid4().hex

    updated_data = {now: new_uuid, **data}
    print(updated_data)
    
    return updated_data


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