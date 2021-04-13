import os
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

from pages.main_activity_page import MainActivity
from pages.settings_activity_page import SettingsActivity

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):
    """
    Klasa bazowa każdego testu
    """

    def setUp(self):
        print("setUp z BaseTest")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-554'
        desired_caps['app'] = PATH('ProfMarcin.apk')
        desired_caps['appPackage'] = 'autyzmsoft.pl.profmarcin'
        desired_caps['appActivity'] = 'autyzmsoft.pl.profmarcin.MainActivity'
        desired_caps['autoGrantPermissions'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.update_settings({"allowInvisibleElements": True})
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.ID, "autyzmsoft.pl.profmarcin:id/btn_OK").click()
        '''
        SUT objects (=activities) creation:
        '''
        self.ma = MainActivity(self.driver)
        self.sa = SettingsActivity(self.driver)

    def tearDown(self):
        print("tearDown z BaseTest")
        self.driver.quit()
