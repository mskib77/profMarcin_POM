import os
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By

from pages.info_activity_page import InfoActivity
from pages.main_activity_page import MainActivity
from pages.settings_activity_page import SettingsActivity
from tests.helpers.auxiliaries import Auxiliaries

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """

    def setUp(self):
        print("setUp z BaseTest")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-554'
        # desired_caps['deviceName'] = '5210f505ea6b8467' # moj nowy telefon
        desired_caps['app'] = PATH('ProfMarcin.apk')
        desired_caps['appPackage'] = 'autyzmsoft.pl.profmarcin'
        desired_caps['appActivity'] = 'autyzmsoft.pl.profmarcin.MainActivity'
        desired_caps['autoGrantPermissions'] = 'true'

        desired_caps['automationName'] = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.update_settings({"allowInvisibleElements": True})
        self.driver.implicitly_wait(Auxiliaries.WAIT_TIME)
        self.driver.find_element(By.ID, "autyzmsoft.pl.profmarcin:id/btn_OK").click()
        '''
        SUT objects (=activities) creation:
        '''
        self.ma = MainActivity(self.driver)
        self.sa = SettingsActivity(self.driver)
        self.ia = InfoActivity(self.driver)

    def tearDown(self):
        print("tearDown z BaseTest")
        self.driver.quit()
