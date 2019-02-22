from pages import LoginPage, FTBPage
from config import PASSWORD


def test_ftb(browser):
    login_page = LoginPage(browser)
    assert login_page.welcomebtn.text == 'Log in'

    login_page.enter_details(PASSWORD)
    ftb_page = FTBPage(browser, force_load=True)

    # Introduce additional checks here
    print(ftb_page.page_title)
