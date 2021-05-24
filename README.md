## Description

A simple API built in Python (Flask) with a single endpoint that logs requests (with a key-value pair of the request timestamp and a unique UUID) in a file and returns all the previous requests made with their timestamps UUID.


## Setup

### Requirements

Python3.6 and above
Pytest (for tests)


### Clone the repository

    git clone https://github.com/reptofrank/uuid_gen

### change into the project folder, create a virtual environment and activate it

    cd uuid_gen
    python3 -m venv venv
    source venv/bin/activate

### Install dependencies

    pip install -r requirements.txt

### setup environment variables

    export FLASK_APP=application.py
    export FLASK_ENV=development

### Run server

    flask run


## Tests

    ### Run tests

    pytest