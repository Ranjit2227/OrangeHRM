from Pages.LoginPage import LoginPage
from Pages.dashboardPage import DashboardPage



def test_dashboard_page(setup):
    driver= setup

    login=LoginPage(driver)
    login.do_login("admin","admin123")

    dashboard= DashboardPage(driver)

    assert dashboard.is_displayed_dashboard()
    assert dashboard.is_quick_launch_visible()
    assert dashboard.get_widget_count()>0