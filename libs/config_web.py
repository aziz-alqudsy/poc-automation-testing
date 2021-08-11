import selenium.webdriver
import pytest
import json

@pytest.fixture
def config(scope='session'):
    # read config file json
    with open('libs/config_web.json') as config_file:
        config = json.load(config_file)

    # assert value that acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config

@pytest.fixture
def browser(config):
    # setup webdriver instance
    if config['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opt = selenium.webdriver.ChromeOptions()
        opt.add_argument('headless')
        driver = selenium.webdriver.Chrome(options=opt)
    else:
        raise Exception('Browser {0} is not supported'.format(config['browser']))

    driver.implicitly_wait(config['implicit_wait'])

    yield driver

    # teardown
    driver.quit()
