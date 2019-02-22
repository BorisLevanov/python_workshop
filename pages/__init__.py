from selenium.webdriver.support.wait import WebDriverWait
from config import BASE_URL, CLIENT


class Page(object):
    """Model of generic page"""

    # overridden when set in subclass
    BASE_PATH = None

    def __init__(self, driver, force_load=False, **url_args):
        self.driver = driver

        if force_load:
            self.url = '{}/{}'.format(
                BASE_URL,
                self.BASE_PATH.format(**url_args)
            )
            import ipdb
            ipdb.set_trace()
            self.driver.get(self.url)

    def get_page_title(self):
        title_css_path = self.driver.find_element_by_css_selector(
            'h1[class*="Header"]')
        return title_css_path.text


class FTBPage(Page):
    BASE_PATH = 'www/FixTheBasics'

    def wait_until_loaded(self):
        WebDriverWait(self.driver, 10).until(
            lambda _: len(self.get_page_title) > 0
        )

    @property
    def page_title(self):
        return self.get_page_title()

    def sku_counter(self):
        pass


class LoginPage(Page):

    def wait_until_loaded(self):
        WebDriverWait(self.driver, 5).until(
            lambda _: self.welcomebtn.is_displayed()
        )

    @property
    def welcomebtn(self):
        return self.driver.find_element_by_css_selector('#btnFormat')

    @property
    def emailtxt(self):
        return self.driver.find_element_by_css_selector("input[name='email']")

    @property
    def passwordtxt(self):
        return self.driver.find_element_by_css_selector("input[name='password']")

    @property
    def loginbtn(self):
        return self.driver.find_element_by_css_selector("input[value='Login'")

    def enter_details(self, password):
        client = CLIENT
        self.welcomebtn.click()
        WebDriverWait(self.driver, 20).until(
            lambda _: self.loginbtn.is_displayed()
        )

        # Set values within Local Storage to bypass the "get_started" and "seen new feature" screens
        self.driver.execute_script(
            "window.localStorage.setItem('user','app@{}.ef.uk.com')".format(client))
        self.driver.execute_script(
            "window.localStorage.setItem('seenNewFeature','0')")

        # The following string was split up to bypass the IE browserstack bug, where "@" is entered as "2"
        self.emailtxt.send_keys('app@{}.ef.uk.com'.format(client))

        self.passwordtxt.send_keys(password)
        self.loginbtn.click()
