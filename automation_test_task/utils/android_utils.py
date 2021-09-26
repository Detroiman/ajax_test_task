
DEVICE_CAPS_ANDROID_TEMPLATE = {
     "autoGrantPermissions": True,
     "automationName": "uiautomator2",
     "newCommandTimeout": 500,
     "noSign": True,
     "platformName": "Android",
     "platformVersion": "10",
     "resetKeyboard": True,
     "systemPort": 8301,
     "takesScreenshot": True,
     "udid": "emulator-5554",
     "appPackage": "com.ajaxsystems",
     "appActivity": "com.ajaxsystems.ui.activity.LauncherActivity",
}


def android_get_desired_cap():
    return DEVICE_CAPS_ANDROID_TEMPLATE
