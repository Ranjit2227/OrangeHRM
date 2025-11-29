from Pages.PimPage import PIMPage
from Pages.LoginPage import LoginPage
from Utilities.config_reader import get_username,get_password



def test_add_employee(setup):
    driver= setup

    login= LoginPage(driver)
    login.do_login(get_username(),get_password())

    pim= PIMPage(driver)
    pim.open_add_employee()
    pim.add_employee("Ranjit","Pandurange","Dhanwade")

    person_text= pim.get_person_text()
    assert person_text == "Personal Details"
    print("Person_Text:",person_text)



