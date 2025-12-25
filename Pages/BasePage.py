
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self,driver):
        self.driver= driver
        self.wait= WebDriverWait(driver,20)

    def do_click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def do_send_keys(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_title(self):
        return self.driver.title

    def wait_for_visibility(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

