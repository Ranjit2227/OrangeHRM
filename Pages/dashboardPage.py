from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class DashboardPage(BasePage):
    """find required locators"""
    dashboard_header=(By.XPATH,"//h6[text()='Dashboard']")
    widgets=(By.XPATH,"//div[@class='oxd-grid-item oxd-grid-item--gutters orangehrm-dashboard-widget']")
    quick_launch=(By.XPATH,"//p[text()='Quick Launch']")

    """action methods"""

    def is_displayed_dashboard(self):
        return self.wait_for_visibility(self.dashboard_header).is_displayed()

    def is_quick_launch_visible(self):
        return self.wait_for_visibility(self.quick_launch).is_displayed()

    def get_widget_count(self):
        return len(self.driver.find_elements(*self.widgets))

