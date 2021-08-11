import json
import pytest
import appium.webdriver

@pytest.fixture
def config():
    # read config file json
    with open('libs/config_mobile.json') as config_file:
        config = json.load(config_file)

    # assert value that acceptable
    assert config['platformName'] in ['Android', 'iOS']
    assert config['deviceName'] in ['emulator-5554', 'iPhone 7']
    assert config['version'] in ['11.0.0', '11.4']
    assert config['app'] is not ''
    assert config['runnerURL'] is not ''

    return config

@pytest.fixture
def emulator(config):
    # setup webdriver instance
    if config['platformName'] == 'Android':
        config['deviceName'] == 'emulator-5554'
        config['version'] == '11.0.0'
        config['app'] == config['app']
        config['runnerURL'] == config['runnerURL']
        driver = appium.webdriver.Remote(config['runnerURL'], config)
    elif config['platformName'] == 'iOS':
        config['deviceName'] == 'iPhone 7'
        config['version'] == '11.4'
        config['app'] == config['app']
        config['runnerURL'] == config['runnerURL']
        driver = appium.webdriver.Remote(config['runnerURL'], config)
    else:
        raise Exception('Emulator {0} is not supported'.format(config['platformName']))

    yield driver

    # teardown
    driver.quit()
