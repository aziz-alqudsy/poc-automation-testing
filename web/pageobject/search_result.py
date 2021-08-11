from selenium.webdriver.common.by import By

class SearchResult():
    # locators
    SEARCH_INPUT = (By.ID, 'v-omnisearch__input')
    SEARCH_TITLE = (By.XPATH, '//h1[@data-test="title"]/b')
    PRODUCT_TITLE = (By.XPATH, '//div[@class="bl-product-card__description-name"]/p')
    NOT_FOUND_PRODUCT = (By.CLASS_NAME, 'bl-text--subheading-1')

    def __init__(self, browser):
        self.browser = browser

    def web_title_result(self):
        # verify web title result
        return self.browser.title

    def page_result_title(self):
        # verify result title same as search input
        search_title = self.browser.find_element(*self.SEARCH_TITLE)
        search_title_text = search_title.text
        return search_title_text

    def search_input_value(self):
        # verify value of search input result
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input_value = search_input.get_attribute('value')
        return search_input_value

    def product_result(self):
        # verify result product title
        product_titles = self.browser.find_elements(*self.PRODUCT_TITLE)
        title = [product_title.text for product_title in product_titles]
        return title
