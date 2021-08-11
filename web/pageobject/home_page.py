from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage():
    # url
    URL = 'https://www.bukalapak.com/'

    # locators
    SEARCH_INPUT = (By.ID, 'v-omnisearch__input')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        # access home url
        self.browser.get(self.URL)

    def search_product(self, productname):
        # click login button on home
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(productname + Keys.RETURN)
