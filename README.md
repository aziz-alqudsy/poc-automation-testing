# poc-automation-testing
the proof of concept automation testing for api, web, and mobile using python.

## Prerequisite
- **install latest pyton.** Usually python was built-in on your computer. Setup your python with newest python version using `pyenv`. Pyenv is python manager to install multiple python version and set default python version, so you shouldn't uninstalll your older one. Read tutorial here: https://realpython.com/intro-to-pyenv/

- **activate virtual environment.** Tool that separates the dependencies of different projects by creating a separate isolated environment for each project.
```
$ python -m venv venv
$ source venv/bin/activate
```

- **install requirements.** Install required modules to run automation testing.
```
$ pip install -r requirements.txt -U
```

## How to run
### API
```
python -m pytest -sv --html reports/report.html
```
