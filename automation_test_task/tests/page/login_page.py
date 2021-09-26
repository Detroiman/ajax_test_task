from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(object):

    def __init__(self, driver):

        self.driver = driver

    def open_login_page(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(('id', 'com.ajaxsystems:id/login')))
        self.driver.find_element('id', 'com.ajaxsystems:id/login').click()

    def fill_fields(self, email, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(("id", 'com.ajaxsystems:id/login')))
        self.driver.find_element("id", 'com.ajaxsystems:id/login').clear()
        self.driver.find_element("id", 'com.ajaxsystems:id/login').send_keys(email)

        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(("id", 'com.ajaxsystems:id/password')))
        self.driver.find_element("id", 'com.ajaxsystems:id/password').clear()
        self.driver.find_element("id", 'com.ajaxsystems:id/password').send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(("id", 'com.ajaxsystems:id/next')))
        self.driver.find_element("id", 'com.ajaxsystems:id/next').click()

    def click_back_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(("id", 'com.ajaxsystems:id/back')))
        self.driver.find_element("id", 'com.ajaxsystems:id/back').click()

    def get_alert_message(self):
        return (WebDriverWait(self.driver, 20).\
            until(EC.visibility_of_element_located(("id", 'com.ajaxsystems:id/snackbar_text')))).text

    def check_on_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(("id", 'com.ajaxsystems:id/spaceControl')))
        self.driver.find_element("id", 'com.ajaxsystems:id/spaceControl')
        try:
            self.driver.find_element("id", 'com.ajaxsystems:id/spaceControl')
        except NoSuchElementException:
            return False
        return True

    def logout(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(("id", 'com.ajaxsystems:id/menuDrawer')))
        self.driver.find_element("id", 'com.ajaxsystems:id/menuDrawer').click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(("id", 'com.ajaxsystems:id/settings')))
        self.driver.find_element("id", 'com.ajaxsystems:id/settings').click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(("id", 'com.ajaxsystems:id/logout')))
        self.driver.find_element("id", 'com.ajaxsystems:id/logout').click()
        self.open_login_page()


