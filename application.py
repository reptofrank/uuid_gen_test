import os
from datetime import datetime
from uuid import uuid4
from flask import Flask

from utils import file_handler

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

data_file = "data.json"


@app.route("/")
def index():
    filepath = os.path.join(os.getcwd(), data_file)

    data = file_handler.read_data_file(filepath)
    format = "%Y-%m-%d %H:%M:%S.%f"
    now = datetime.now().strftime(format)
    new_uuid = uuid4().hex

    updated_data = {now: new_uuid, **data}

    file_handler.write_data_file(filepath, updated_data)
        
    return updated_data


@app.errorhandler(404)
def page_not_found(error):
    return {"error": "Not Found"}, 404

    