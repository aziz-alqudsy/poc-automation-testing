from appium.webdriver.common.mobileby import MobileBy

class RegisterPage():
    # locators
    INPUT_NAME = (MobileBy.ID, 'textInputEditTextName')
    INPUT_EMAIL = (MobileBy.ID, 'textInputEditTextEmail')
    INPUT_PASSWORD = (MobileBy.ID, 'textInputEditTextPassword')
    INPUT_CONFIRM_PASSWORD = (MobileBy.ID, 'textInputEditTextConfirmPassword')
    REGISTER_BUTTON = (MobileBy.ID, 'appCompatButtonRegister')
    LOGIN_LINK = (MobileBy.ID, 'appCompatTextViewLoginLink')
    SNACKBAR = (MobileBy.ID, 'snackbar_text')

    def __init__(self, emulator):
        self.emulator = emulator

    def input_register_form(self, username, user_email, password, confirm_password):
        # fill register form
        name_field = self.emulator.find_element(*self.INPUT_NAME)
        name_field.send_keys(username)
        email_field = self.emulator.find_element(*self.INPUT_EMAIL)
        email_field.send_keys(user_email)
        password_field = self.emulator.find_element(*self.INPUT_PASSWORD)
        password_field.send_keys(password)
        confirm_password_field = self.emulator.find_element(*self.INPUT_CONFIRM_PASSWORD)
        confirm_password_field.send_keys(confirm_password)

    def submit_registration(self):
        # click button register
        register_button = self.emulator.find_element(*self.REGISTER_BUTTON)
        register_button.click()

    def login_link(self):
        # cek login link
        return self.emulator.find_element(*self.LOGIN_LINK)

    def snackbar(self):
        # cek snackbar
        return self.emulator.find_element(*self.SNACKBAR).text
