# poc-automation-testing
the proof of concept automation testing for api, web, and mobile using python.

## Prerequisite
- **install latest pyton.** Usually python was built-in on your computer. Setup your python with newest python version using `pyenv`. Pyenv is python manager to install multiple python version and set default python version, so you shouldn't uninstalll your older one. Read tutorial here: https://realpython.com/intro-to-pyenv/

- **activate virtual environment.** Tool that separates the dependencies of different projects by creating a separate isolated environment for each project.
```
$ python -m venv venv
$ source venv/bin/activate
```

- **install webdriver.** Webdriver will open web and run your automation steps. I test using Chromdriver which chrome's webdriver that you can donwload here: https://chromedriver.chromium.org/. In order to install firefox geckodriver, visi here: https://github.com/mozilla/geckodriver/releases/. Then, move installer to `/usr/local/bin` to excutable.
```
$ mv ~/Downloads/chromedriver /usr/local/bin
```

- **install nvm.** NVM is node version manager, designed to be installed per-user, and invoked per-shell. Install here: https://github.com/nvm-sh/nvm#install--update-script.

- **install node.js.** Nodejs is a JavaScript runtime. Install here: https://nodejs.org/en/download/.

- **download your apk.**

- **install appium via npm.** Appium will run your automation steps.
```
$ npm install -g appium
```

- **install appium-doctor.** Check your installation checklist using appium-doctor.
```
$ npm install appium-doctor -g
$ appium-doctor --android
```

- **install java jdk.** For setup preparation android.
```
$ brew install --cask adoptopenjdk
$ sudo ln -sfn /usr/local/opt/openjdk@8/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/adoptopenjdk.jdk
$ nano $HOME/.zshrc
export JAVA_HOME=$(/usr/libexec/java_home)
$ source $HOME/.zshrc
$ java --version

```

- **install android studio.** To run avd emulator here: https://developer.android.com/studio/install#mac.

- **setup android sdk path.**
```
$ nano $HOME/.zshrc
export ANDROID_HOME=$HOME/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools:$ANDROID_HOME/emulator
$ source $HOME/.zshrc
```

- **install flipper.** For selector and logging android here: https://fbflipper.com/.
After avd running, install locator plugin in Flipper.

- **install requirements.** Install required modules to run automation testing.
```
$ pip install -r requirements.txt -U
```

## How to run
### Local
#### API and Web
sequensial run:
```
$ python -m pytest -sv --html reports/report.html
```

paralel run:
```
$ python -m pytest -n <number> -sv --html reports/report.html
```

### Mobile
- run appium.
```
$ appium
```
- open avd manager and create emulator.
- install apk in emulator using drag and drop.
- run test.

sequensial run:
```
$ python -m pytest -sv --html reports/report.html
```
