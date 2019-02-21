
from pages import LoginPage, FTBPage


def test_ftb(browser):
    login_page = LoginPage(browser)
    assert login_page.welcomebtn.text == 'Log in'

    login_page.enter_details('')
    ftb_page = FTBPage(browser, force_load=True)

    # assert the presence of SKU counter
