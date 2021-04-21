import os
import unittest
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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

        # desired_caps['deviceName'] = 'emulator-554'
        desired_caps['deviceName'] = '5210f505ea6b8467' # moj nowy telefon

        desired_caps['app'] = PATH('ProfMarcin.apk')
        desired_caps['appPackage'] = 'autyzmsoft.pl.profmarcin'
        desired_caps['appActivity'] = 'autyzmsoft.pl.profmarcin.MainActivity'
        desired_caps['autoGrantPermissions'] = 'true'

        desired_caps['automationName'] = 'UiAutomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.update_settings({"allowInvisibleElements": True})
        self.driver.implicitly_wait(Auxiliaries.WAIT_TIME)

        self.__dismiss_splash_window()

        self.create_activities()

    def create_activities(self):
        """ SUT objects (=activities) creation """
        " These activities will/may be used by tests "
        self.ma = MainActivity(self.driver)
        self.sa = SettingsActivity(self.driver)
        self.ia = InfoActivity(self.driver)

    def __dismiss_splash_window(self):
        """ Clicks on OK to unlock Main Activity """
        """ Note: OK buttom may not be visible on some devices, therefore scrolling"""

        sleep(5)

        # screen dimensions:
        size: dict = self.driver.get_window_size()
        startx = size['width'] / 2
        starty = int(size['height'] * 0.9)
        # endx = size['width'] / 2
        endy = int(size['height'] * 0.2)


        found = False
        while not found:
            try:
                el = self.driver.find_element(By.ID, "autyzmsoft.pl.profmarcin:id/btn_OK")
                found = True
                el.click()
            except NoSuchElementException:
                # self.driver.swipe(100, 300, 100, 50, 1000)
                self.driver.swipe(startx, starty, startx, endy, 1000)


    def tearDown(self):
        print("tearDown z BaseTest")
        self.driver.quit()
