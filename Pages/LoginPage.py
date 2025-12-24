from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoginPage(BasePage):
    """find required locators"""
    username_input= (By.NAME,"username")
    password_input= (By.NAME,"password")
    login_btn= (By.XPATH,"//button[@type='submit']")
    dashboard_text= (By.XPATH,"//h6[text()='Dashboard']")

    """ error message"""
    error_message= (By.XPATH,"//p[text()='Invalid credentials']")

    """ write method """
    def do_login(self,username,password):
        self.do_send_keys(self.username_input,username)
        self.do_send_keys(self.password_input,password)
        self.do_click(self.login_btn)

    def get_dashboard_text(self):
        return self.get_text(self.dashboard_text)






