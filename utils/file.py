import json

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