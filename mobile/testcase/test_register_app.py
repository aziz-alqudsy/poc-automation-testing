import names
import time
from libs.config_mobile import config, emulator
from libs.generated_data import email, random_string
from mobile.pageobject.login_page import LoginPage
from mobile.pageobject.register_page import RegisterPage
from mobile.library.register_user import RegisterUser
from mobile.pageobject.dashboard import Dashboard

# initiate values
USERNAME = names.get_full_name()
USER_EMAIL = email(name=USERNAME)
PASSWORD = random_string(size=6)

def test_fail_empty_registration(emulator):
    # Given login page is displayed
    assert 'VERSION - V4' in emulator.page_source

    # When user click Create One link
    LoginPage(emulator).click_register_link()

    # Then user see Already Member? Login link
    emulator.swipe(470, 1400, 470, 1000, 400)
    assert RegisterPage(emulator).login_link().text in emulator.page_source

    # When user submit registration form with all empty field
    RegisterPage(emulator).submit_registration()

    # Then showing error
    assert 'Enter Full Name' in emulator.page_source

def test_fail_empty_fullname(emulator):
    # Given login page is displayed
    assert 'VERSION - V4' in emulator.page_source

    # When user click Create One link
    LoginPage(emulator).click_register_link()

    # Then user see Already Member? Login link
    emulator.swipe(470, 1400, 470, 1000, 400)
    assert RegisterPage(emulator).login_link().text in emulator.page_source

    # When user submit registration form with all empty field
    RegisterPage(emulator).submit_registration()

    # Then showing error
    assert 'Enter Full Name' in emulator.page_source

def test_fail_empty_email(emulator):
    # Given login page is displayed
    assert 'VERSION - V4' in emulator.page_source

    # When user click Create One link
    LoginPage(emulator).click_register_link()

    # Then user see Already Member? Login link
    emulator.swipe(470, 1400, 470, 1000, 400)
    assert RegisterPage(emulator).login_link().text in emulator.page_source

    # When user fill and submit registration form
    RegisterPage(emulator).input_register_form(username=USERNAME, user_email='', password=PASSWORD, confirm_password=PASSWORD)
    RegisterPage(emulator).submit_registration()

    # Then showing error
    assert 'Enter Valid Email' in emulator.page_source

def test_fail_invalid_email(emulator):
    # Given login page is displayed
    assert 'VERSION - V4' in emulator.page_source

    # When user click Create One link
    LoginPage(emulator).click_register_link()

    # Then user see Already Member? Login link
    emulator.swipe(470, 1400, 470, 1000, 400)
    assert RegisterPage(emulator).login_link().text in emulator.page_source

    # When user fill and submit registration form
    RegisterPage(emulator).input_register_form(username=USERNAME, user_email=USERNAME, password=PASSWORD, confirm_password=PASSWORD)
    RegisterPage(emulator).submit_registration()

    # Then showing error
    assert 'Enter Valid Email' in emulator.page_source

def test_fail_empty_password(emulator):
    # Given login page is displayed
    assert 'VERSION - V4' in emulator.page_source

    # When user click Create One link
    LoginPage(emulator).click_register_link()

    # Then user see Already Member? Login link
    emulator.swipe(470, 1400, 470, 1000, 400)
    assert RegisterPage(emulator).login_link().text in emulator.page_source

    # When user fill and submit registration form
    RegisterPage(emulator).input_register_form(username=USERNAME, user_email=USER_EMAIL, password='', confirm_password=PASSWORD)
    RegisterPage(emulator).submit_registration()

    # Then showing error
    assert 'Enter Password' in emulator.page_source

def test_fail_empty_confirm_password(emulator):
    # Given login page is displayed
    assert 'VERSION - V4' in emulator.page_source

    # When user click Create One link
    LoginPage(emulator).click_register_link()

    # Then user see Already Member? Login link
    emulator.swipe(470, 1400, 470, 1000, 400)
    assert RegisterPage(emulator).login_link().text in emulator.page_source

    # When user fill and submit registration form
    RegisterPage(emulator).input_register_form(username=USERNAME, user_email=USER_EMAIL, password=PASSWORD, confirm_password='')
    RegisterPage(emulator).submit_registration()

    # Then showing error
    assert 'Password Does Not Matches' in emulator.page_source

def test_fail_not_match_password(emulator):
    # Given login page is displayed
    assert 'VERSION - V4' in emulator.page_source

    # When user click Create One link
    LoginPage(emulator).click_register_link()

    # Then user see Already Member? Login link
    emulator.swipe(470, 1400, 470, 1000, 400)
    assert RegisterPage(emulator).login_link().text in emulator.page_source

    # When user fill and submit registration form
    RegisterPage(emulator).input_register_form(username=USERNAME, user_email=USER_EMAIL, password=PASSWORD, confirm_password='test')
    RegisterPage(emulator).submit_registration()

    # Then showing error
    assert 'Password Does Not Matches' in emulator.page_source

def test_fail_register_using_registered_email(emulator):
    # Given user register successfully
    RegisterUser(emulator).succesfully_registered(username=USERNAME, user_email=USER_EMAIL, password=PASSWORD, confirm_password=PASSWORD)

    # When user register again using same email
    time.sleep(3)
    RegisterPage(emulator).input_register_form(username=USERNAME, user_email=USER_EMAIL, password=PASSWORD, confirm_password=PASSWORD)
    RegisterPage(emulator).submit_registration()

    # Then showing snackbar Email Already Exists
    emulator.implicitly_wait(2)
    assert RegisterPage(emulator).snackbar() in emulator.page_source
    assert RegisterPage(emulator).snackbar() == 'Email Already Exists'

def test_success_registration(emulator):
    # different value
    NEW_USERNAME = names.get_full_name()
    NEW_USER_EMAIL = email(name=NEW_USERNAME)

    # Given user register successfully
    RegisterUser(emulator).succesfully_registered(username=NEW_USERNAME, user_email=NEW_USER_EMAIL, password=PASSWORD, confirm_password=PASSWORD)

    # When user click Login link
    time.sleep(3)
    RegisterPage(emulator).login_link().click()

    # Then user see VERSION - V4 text
    time.sleep(3)
    assert 'VERSION - V4' in emulator.page_source

    # When user fill and submit login form
    LoginPage(emulator).input_login_form(user_email=NEW_USER_EMAIL, password=PASSWORD)

    # Then user will direct to dashboard and see Android NewLine Learning title, his username on header and his data profile
    assert Dashboard(emulator).header_email() in emulator.page_source
    assert Dashboard(emulator).username() == NEW_USERNAME
    assert Dashboard(emulator).email() == NEW_USER_EMAIL
    assert Dashboard(emulator).password() == PASSWORD
    assert 'Android NewLine Learning' in emulator.page_source
