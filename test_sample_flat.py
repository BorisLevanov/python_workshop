from selenium import webdriver


def test_login():
    driver = webdriver.Chrome()
    driver.get('{}/login/'.format('https://reports-dashboard-test.ef.uk.com'))
    driver.set_window_size(1920, 1080)

    assert driver.find_element_by_css_selector('#btnFormat').text == 'Log in'

    driver.quit()
