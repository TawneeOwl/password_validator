# Password Validator

This application validates a password based on criteria set.

# Getting started

### Prerequisite

Please ensure you have a version of Python3 installed on your system.

https://www.python.org/downloads/

### Setup

Create a virtual environment and install the dependencies:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements/generated/requirements.txt
```

### Run the tool

To run the application, call password_validator.py with the password given as an arguement:

```shell
python3 app/password_validator.py Password123456_
```

### Testing

To test the application run:

```shell
pytest
```

### Linting and formatting

To run the linter on the code, run the below command:

```shell
ruff check
```

To format the code via ruff, run the below command:

```shell
ruff format
```

### Updating requirements

To update the requirements, run the below command once you've made changes to requirements/source/requirements.in:

```shell
pip-compile --output-file=requirements/generated/requirements.txt requirements/source/requirements.in
```