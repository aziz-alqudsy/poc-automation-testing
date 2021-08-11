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

- **install webdriver.** Webdriver will open web and run your step automation. I test using Chromdriver which chrome's webdriver that you can donwload here: https://chromedriver.chromium.org/. In order to install firefox geckodriver, visi here: https://github.com/mozilla/geckodriver/releases/. Then, move installer to `/usr/local/bin` to excutable.
```
$ mv ~/Downloads/chromedriver /usr/local/bin
```

## How to run
### Local
#### API and Web
sequensial run:
```
python -m pytest -sv --html reports/report.html
```

paralel run:
```
python -m pytest -n <number> -sv --html reports/report.html
```
