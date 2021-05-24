import os
import tempfile
import pytest
import json
from utils import file


def test_read_empty_file():
    fh, filepath = tempfile.mkstemp()
    data = file.read_data_file(filepath)

    assert data == {}

    os.close(fh)
    os.unlink(filepath)


def test_read_file_with_json_data():
    fh, filepath = tempfile.mkstemp()
    with open(filepath, "w") as f:
        f.write('{"name": "Cowrywise"}')
    
    data = file.read_data_file(filepath)

    assert data['name'] == "Cowrywise"

    os.close(fh)
    os.unlink(filepath)


def test_read_file_with_invalid_json_data():
    fh, filepath = tempfile.mkstemp()
    with open(filepath, "w") as f:
        f.write('hello')
    with pytest.raises(json.decoder.JSONDecodeError) as error:
        data = file.read_data_file(filepath)
        assert data['name'] == "Cowrywise"

    os.close(fh)
    os.unlink(filepath)


def test_file_not_found_exception():
    with pytest.raises(FileNotFoundError) as error:
        filepath = os.path.join(os.path.dirname(__file__), "../notfound.json")
        data = file.read_data_file(filepath)