
from Pages.LoginPage import LoginPage
from Utilities.config_reader import get_username,get_password


def test_do_login(setup):
    driver=setup
    login= LoginPage(driver)
    login.do_login(get_username(),get_password())

    title= login.get_title()
    assert title == "OrangeHRM"
    print("\nTitle:", title)

    dash_text= login.get_dashboard_text()
    assert dash_text == "Dashboard"
    print("Dashboard Text:",dash_text)






