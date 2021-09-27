from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(object):

    def __init__(self, driver):

        self.driver = driver
        self.button_back_id = 'com.ajaxsystems:id/back'
        self.button_login_id = 'com.ajaxsystems:id/next'
        self.field_email_id = 'com.ajaxsystems:id/login'
        self.field_password_id = 'com.ajaxsystems:id/password'
        self.alert_window_id = 'com.ajaxsystems:id/snackbar_text'
        self.user_page_id = 'com.ajaxsystems:id/spaceControl'
        self.user_menu_id = 'com.ajaxsystems:id/menuDrawer'
        self.button_settings_id = 'com.ajaxsystems:id/settings'
        self.button_logout_id = 'com.ajaxsystems:id/logout'

    # Analog WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located
    def visibility_element_located(self, object_id):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(('id', object_id)))

    # Function for find element on page
    def find_object(self, object_id):
        self.driver.find_element('id', object_id)

    # Function for find and click on object on page
    def find_click_on_object(self, object_id):
        self.driver.find_element('id', object_id).click()

    # Function for clear field
    def clear_fields(self, object_id):
        self.driver.find_element("id", object_id).clear()

    # Function for send key in field
    def send_keys(self, object_id, keys):
        self.driver.find_element("id", object_id).send_keys(keys)

    # Analog WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable
    def wait_clickable(self, object_id):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(("id", object_id)))

    # Function for open page with login fields
    def open_login_page(self):
        self.visibility_element_located(self.field_email_id)
        self.find_click_on_object(self.field_email_id)

    # Function for fill fields in login page
    def fill_fields(self, email, password):
        self.visibility_element_located(self.field_email_id)
        self.clear_fields(self.field_email_id)
        self.send_keys(self.field_email_id, email)

        self.visibility_element_located(self.field_password_id)
        self.clear_fields(self.field_password_id)
        self.send_keys(self.field_password_id, password)

    # Function for login user
    def click_login_button(self):
        self.wait_clickable(self.button_login_id)
        self.find_click_on_object(self.button_login_id)

    # Function for click on button back in login page
    def click_back_button(self):
        self.wait_clickable(self.button_back_id)
        self.find_click_on_object(self.button_back_id)

    # Function that return alert message in login page
    def get_alert_message(self):
        return (self.visibility_element_located(self.alert_window_id)).text

    # Function for check on logined
    def check_on_login(self):
        self.wait_clickable(self.user_page_id)
        self.find_object(self.user_page_id)
        try:
            self.find_object(self.user_page_id)
        except NoSuchElementException:
            return False
        return True

    # Function for logout user
    def logout(self):
        self.wait_clickable(self.user_menu_id)
        self.find_click_on_object(self.user_menu_id)
        self.wait_clickable(self.button_settings_id)
        self.find_click_on_object(self.button_settings_id)
        self.wait_clickable(self.button_logout_id)
        self.find_click_on_object(self.button_logout_id)
        self.open_login_page()


