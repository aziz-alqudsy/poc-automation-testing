from appium.webdriver.common.mobileby import MobileBy

class LoginPage():
    # locators
    INPUT_EMAIL = (MobileBy.ID, 'textInputEditTextEmail')
    INPUT_PASSWORD = (MobileBy.ID, 'textInputEditTextPassword')
    LOGIN_BUTTON = (MobileBy.ID, 'appCompatButtonLogin')
    REGISTER_LINK = (MobileBy.ID, 'textViewLinkRegister')

    def __init__(self, emulator):
        self.emulator = emulator

    def click_register_link(self):
        # click register link
        register_link = self.emulator.find_element(*self.REGISTER_LINK)
        register_link.click()

    def input_login_form(self, user_email, password):
        # initiate value
        input_field = self.emulator.find_element(*self.INPUT_EMAIL)
        input_field.send_keys(user_email)
        input_password = self.emulator.find_element(*self.INPUT_PASSWORD)
        input_password.send_keys(password)
        login_button = self.emulator.find_element(*self.LOGIN_BUTTON)
        login_button.click()

