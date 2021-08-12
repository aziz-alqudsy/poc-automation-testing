from mobile.pageobject.login_page import LoginPage
from mobile.pageobject.register_page import RegisterPage

class RegisterUser():
    def __init__(self, emulator):
        self.emulator = emulator

    def succesfully_registered(self, username, user_email, password, confirm_password):
        # Given login page is displayed
        assert 'VERSION - V4' in self.emulator.page_source

        # When user click Create One link
        LoginPage(self.emulator).click_register_link()

        # Then user see Already Member? Login link
        self.emulator.swipe(470, 1400, 470, 1000, 400)
        assert RegisterPage(self.emulator).login_link().text in self.emulator.page_source

        # When user fill and submit registration form
        RegisterPage(self.emulator).input_register_form(username=username, user_email=user_email, password=password, confirm_password=confirm_password)
        RegisterPage(self.emulator).submit_registration()

        # Then showing snackbar Register Successful
        self.emulator.implicitly_wait(2)
        assert RegisterPage(self.emulator).snackbar() in self.emulator.page_source
        assert RegisterPage(self.emulator).snackbar() == 'Registration Successful'
