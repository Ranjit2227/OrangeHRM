from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class PIMPage(BasePage):
    """Find Locators"""
    pim_click= (By.XPATH,"//span[text()='PIM']")
    add_emp_btn= (By.XPATH,"//button[normalize-space()='Add']")

    emp_first_name= (By.CSS_SELECTOR,"input[placeholder='First Name']")
    emp_middle_name= (By.CSS_SELECTOR,"input[placeholder='Middle Name']")
    emp_last_name= (By.CSS_SELECTOR,"input[placeholder='Last Name']")
    save_emp= (By.XPATH,"//button[normalize-space()='Save']")
    person_txt= (By.XPATH,"//h6[text()='Personal Details']")

    """create method"""

    def open_add_employee(self):
        self.do_click(self.pim_click)
        self.do_click(self.add_emp_btn)

    def add_employee(self,first_name,middle_name,last_name):
        self.do_send_keys(self.emp_first_name,first_name)
        self.do_send_keys(self.emp_middle_name,middle_name)
        self.do_send_keys(self.emp_last_name,last_name)
        self.do_click(self.save_emp)

    def get_person_text(self):
        return self.get_text(self.person_txt)



