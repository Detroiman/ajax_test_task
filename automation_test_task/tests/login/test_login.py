import json
import logging
import time

import pytest

from tests.page.login_page import LoginPage


test_result = {}
json_name = "test_result.json"


def write_json(file_name, data_dict):
    with open(file_name, 'w') as file:
        json.dump(data_dict, file)


@pytest.fixture()
def check_wrong_pass(page):
    page.fill_fields('qa.ajax.app.automation@gmail.com', 'qa_automation_password1')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "Wrong login or password":
        test_result.update({'First test': {"Check on wrong password": "OK"}})
    else:
        test_result.update({'First test': {"Check on wrong password"
                                           : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})
    return alert_text


def test1():
    logging.info('Test function check_wrong_pass')
    assert check_wrong_pass != "Wrong login or password", "Must be Wrong login or password"


@pytest.fixture()
def check_wrong_email(page):
    page.fill_fields('qa.ajax.app.automation@gmail.c', 'qa_automation_password')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "Wrong login or password":
        test_result.update({'Second test': {"Check on wrong email": "OK"}})
    else:
        test_result.update({'Second test': {"Check on wrong email"
                                            : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})
    return alert_text


def test2():
    logging.info('Test function check_wrong_email')
    assert check_wrong_email != "Wrong login or password", "Must be Wrong login or password"


@pytest.fixture()
def check_not_entered_pass(page):
    page.fill_fields('qa.ajax.app.automation@gmail.c', '')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "Please fill all of the required fields.":
        test_result.update({'Third test': {"Check on not entered password": "OK"}})
    else:
        test_result.update({'Third test': {"Check on not entered password"
                                           : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})
    return alert_text


def test3():
    logging.info('Test function check_not_entered_pass')
    assert check_not_entered_pass != "Please fill all of the required fields.", \
        "Must be Please fill all of the required fields."


@pytest.fixture()
def check_no_email_pass(page):
    page.fill_fields('', '')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "Please fill all of the required fields.":
        test_result.update({'Fourth test': {"Check on no email and password": "OK"}})
    else:
        test_result.update({'Fourth test': {"Check on no email and password"
                                            : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})
    return alert_text


def test4():
    logging.info('Test function check_no_email_pass')
    assert check_no_email_pass != "Please fill all of the required fields.",\
        "Must be Please fill all of the required fields."


@pytest.fixture()
def check_not_reg_account(page):
    page.fill_fields('denefimov2001@gmail.com', 'qwerty123')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "User is not registered.":
        test_result.update({'Fifth test': {"Check on not reg account": "OK"}})
    else:
        test_result.update({'Fifth test': {"Check on not reg account"
                                           : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})
    return alert_text


def test5():
    logging.info('Test function check_not_reg_account')
    assert check_not_reg_account == "Wrong login or password", "Must be Not reg"


@pytest.fixture()
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
    return check_login


def test6():
    logging.info('Test function check_onSpace_beforeEmail')
    assert check_onSpace_beforeEmail is True, "User must be unlogined"


@pytest.fixture()
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
    return check_login


def test7():
    logging.info('Test function check_onSpace_afterEmail')
    assert check_onSpace_afterEmail is True, "User must be unlogined"


@pytest.fixture()
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
    return check_login


def test8():
    logging.info('Test function check_mixed_case_inEmail')
    assert check_mixed_case_inEmail is True, "User must be unlogined"


@pytest.fixture()
def check_email_withSymbols(page):
    page.fill_fields('<qa.ajax.app.automation@gmail.com>', 'qa_automation_password')
    page.click_login_button()
    alert_text = page.get_alert_message()
    if alert_text == "Wrong login or password":
        test_result.update({'Ninth test': {"Check on email with symbol <, >": "OK"}})
    else:
        test_result.update({'Ninth test': {"Check on email with symbol <, >"
                                           : f"Wrong answer, got {alert_text} instead of 'Wrong login or password'"}})
    return alert_text


def test9():
    logging.info('Test function check_email_withSymbols')
    assert check_email_withSymbols != "Wrong login or password", "Must be Wrong login or password"


@pytest.fixture()
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
    return 1 if check_login else 0


def test10():
    logging.info('Test function check_right_email_pass')
    assert check_right_email_pass != 1, "User must be logined"


@pytest.fixture()
def check_right_email_pass_buttonBack(page):
    page.fill_fields('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    page.click_back_button()
    page.open_login_page()
    page.click_login_button()
    time.sleep(3)
    check_login = page.check_on_login()
    if check_login:
        test_result.update({'Tenth test': {"Check on right email and password after press back button": "OK"}})
    else:
        test_result.update({'Tenth test': {"Check on right email and password after press back button"
                                              : f"Not on main page, {check_login}, account was not logined"}})
    page.logout()
    return 1 if check_login else 0


def test11():
    logging.info('Test function check_right_email_pass_buttonBack')
    assert check_right_email_pass_buttonBack != 1, "User must be logined"


def loginPageTest():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()


def threatDown(pm):
    pm.quit()


def test_login(page_manager):
    pm = page_manager
    page = pm.create_page(LoginPage)
    page.open_login_page()
    loginPageTest()
    threatDown(pm)





