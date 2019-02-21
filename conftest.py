import pytest
from selenium import webdriver

from config import BASE_URL


@pytest.yield_fixture()
def browser(request):
    driver = webdriver.Chrome()
    driver.get('{}/login/'.format(BASE_URL))
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
