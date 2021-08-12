from appium.webdriver.common.mobileby import MobileBy

class Dashboard():
    # locators
    HEADER_EMAIL = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.TextView[3]')
    NAME = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]')
    EMAIL = (MobileBy.ID, 'textViewEmail')
    PASSWORD = (MobileBy.ID, 'textViewPassword')

    def __init__(self, emulator):
        self.emulator = emulator

    def header_email(self):
        # get email on header dashboard
        user_email = self.emulator.find_element(*self.HEADER_EMAIL)
        email = user_email.text
        return email

    def username(self):
        # get name on dashboard
        user_name = self.emulator.find_element(*self.NAME)
        name = user_name.text
        return name

    def email(self):
        # get email on dahsboard
        user_email = self.emulator.find_element(*self.EMAIL)
        email = user_email.text
        return email

    def password(self):
        # get password on dahsboard
        user_password = self.emulator.find_element(*self.PASSWORD)
        password = user_password.text
        return password
