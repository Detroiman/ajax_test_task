import subprocess
import time

import pytest
from appium import webdriver

from tests.page.page_manager import PagesManager
from utils.android_utils import android_get_desired_cap


@pytest.fixture(scope='session')
def setup_appium():

    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.yield_fixture(autouse=True, scope='session')
def driver(setup_appium):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_cap())

    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def page_manager(driver):
    return PagesManager(driver)
