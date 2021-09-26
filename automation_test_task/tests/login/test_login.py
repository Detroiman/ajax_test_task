import json
import time

from tests.page.login_page import LoginPage


test_result = {}
json_name = "test_result.json"


def write_json(file_name, data_dict):
    with open(file_name, 'w') as file:
        json.dump(data_dict, file)


# Check login page on negative result
# Different combinations of Username and Password
# Check on wrong password

def check_wrong_pass(page):
    page.fill_fields('qa.ajax.app.automation@gmail.com', 'qa_automation_password1')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "Wrong login or password":
        test_result.update({'First test': {"Check on wrong password": "OK"}})
    else:
        test_result.update({'First test': {"Check on wrong password"
                                           : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})

# Check on wrong email


def check_wrong_email(page):
    page.fill_fields('qa.ajax.app.automation@gmail.c', 'qa_automation_password')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "Wrong login or password":
        test_result.update({'Second test': {"Check on wrong email": "OK"}})
    else:
        test_result.update({'Second test': {"Check on wrong email"
                                            : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})

# Check on not entered password


def check_not_entered_pass(page):
    page.fill_fields('qa.ajax.app.automation@gmail.c', '')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "Please fill all of the required fields.":
        test_result.update({'Third test': {"Check on not entered password": "OK"}})
    else:
        test_result.update({'Third test': {"Check on not entered password"
                                           : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})

# Check on no email and password


def check_no_email_pass(page):
    page.fill_fields('', '')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "Please fill all of the required fields.":
        test_result.update({'Fourth test': {"Check on no email and password": "OK"}})
    else:
        test_result.update({'Fourth test': {"Check on no email and password"
                                            : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})

# Check on not reg account


def check_not_reg_account(page):
    page.fill_fields('denefimov2001@gmail.com', 'qwerty123')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "User is not registered.":
        test_result.update({'Fifth test': {"Check on not reg account": "OK"}})
    else:
        test_result.update({'Fifth test': {"Check on not reg account"
                                           : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})

# Check on space before right email


def check_onSpace_beforeEmail(page):
    page.fill_fields('     qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    page.click_login_button()
    check_login = page.check_on_login()
    if check_login:
        test_result.update({'Sixth test': {"Check on space before right email": "Error, user is logined"}})
    else:
        test_result.update({'Sixth test': {"Check on space before right email"
                                           : "OK"}})
    page.logout()

# Check on space after right email


def check_onSpace_afterEmail(page):
    page.fill_fields('qa.ajax.app.automation@gmail.com      ', 'qa_automation_password')
    page.click_login_button()
    check_login = page.check_on_login()
    if check_login:
        test_result.update({'Seventh test': {"Check on space after right email": "Error, user is logined"}})
    else:
        test_result.update({'Seventh test': {"Check on space after right email"
                                             : f"OK"}})
    page.logout()


# Check on email with mixed case


def check_mixed_case_inEmail(page):
    page.fill_fields('Qa.ajax.aPp.aUtomation@gMail.coM', 'qa_automation_password')
    page.click_login_button()
    check_login = page.check_on_login()
    if check_login:
        test_result.update({'Eighth test': {"Check on email with mixed case": "Error, user is logined"}})
    else:
        test_result.update({'Eighth test': {"Check on email with mixed case"
                                           : "OK"}})
    page.logout()

# Check on email with symbol <, >


def check_email_withSymbols(page):
    page.fill_fields('<qa.ajax.app.automation@gmail.com>', 'qa_automation_password')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "Wrong login or password":
        test_result.update({'Ninth test': {"Check on email with symbol <, >": "OK"}})
    else:
        test_result.update({'Ninth test': {"Check on email with symbol <, >"
                                           : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})

# Check right email and pass


def check_right_email_pass(page):
    page.fill_fields('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    page.click_login_button()
    time.sleep(3)
    check_login = page.check_on_login()
    if check_login:
        test_result.update({'Tenth test': {"Check on right email and password": "OK"}})
    else:
        test_result.update({'Tenth test': {"Check on right email and password"
                                              : f"Not on main page, {check_login}, account was not logined"}})
    page.logout()


def test_login(page_manager):
    try:
        pm = page_manager
        page = pm.create_page(LoginPage)
        page.open_login_page()
        check_wrong_pass(page)
        check_wrong_email(page)
        check_not_entered_pass(page)
        check_no_email_pass(page)

        check_onSpace_beforeEmail(page)
        check_onSpace_afterEmail(page)
        check_mixed_case_inEmail(page)

        check_email_withSymbols(page)
        check_right_email_pass(page)

    finally:
        time.sleep(5)
        write_json(json_name, test_result)


