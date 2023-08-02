# arquivo: appium_driver.py

from appium import webdriver

class AppiumDriver:
    @staticmethod
    def get_driver():
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "14.0",
            "deviceName": "Pixel_3a_API_34_extension_level_7_x86_64",
            "udid": "emulator-5554",
            #"appPackage": "com.example.app",
            #"appActivity": "com.example.app.MainActivity",
            "app": "/home/diegomachado/Temp/PreciseUnitConversion.apk",
            "noReset": True
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        return driver
