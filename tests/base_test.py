import os
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainActivityLocators as MAL
from pages.info_activity_page import InfoActivity
from pages.main_activity_page import MainActivity
from pages.settings_activity_page import SettingsActivity
from tests.test_utils import TestUtils

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """

    def setUp(self):
        print("setUp z BaseTest\n")
        desired_caps = {}
        desired_caps['platformName'] = 'Android'

        desired_caps['deviceName'] = 'emulator-554'
        # desired_caps['deviceName'] = '5210f505ea6b8467' # moj nowy telefon
        # desired_caps['deviceName'] = '5200241cea6f7523'   # moj Stary telefon

        desired_caps['app'] = PATH('ProfMarcin.apk')
        desired_caps['appPackage'] = 'autyzmsoft.pl.profmarcin'
        desired_caps['appActivity'] = 'autyzmsoft.pl.profmarcin.MainActivity'
        desired_caps['autoGrantPermissions'] = 'true'
        desired_caps['automationName'] = 'UiAutomator2'

        desired_caps['allowTestPackages'] = 'true'

        # desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.update_settings({"allowInvisibleElements": True})   # nie dziala....
        self.driver.implicitly_wait(TestUtils.WAIT_TIME)
        self._dismiss_splash_window()
        self.create_activities()

    def create_activities(self):
        """ SUT objects (=activities) creation """
        " These activities will/may be used by tests "
        self.ma = MainActivity(self.driver)
        self.sa = SettingsActivity(self.driver)
        self.ia = InfoActivity(self.driver)

    def _dismiss_splash_window(self):
        """ Clicks on Start button to unlock Main Activity """
        """ Note: Start button may not be visible on some devices, therefore scrolling """

        x, y = TestUtils.get_screen_dimensions(self.driver)
        # speeding up a little:
        self.driver.implicitly_wait(1)
        # scrolling down till OK button appears:
        found = False
        while not found:
            try:
                el = self.driver.find_element(By.ID, "autyzmsoft.pl.profmarcin:id/btn_OK")
                found = True
                # restoring timeout:
                self.driver.implicitly_wait(TestUtils.WAIT_TIME)
                el.click()
            except NoSuchElementException:
                self.driver.swipe(x/2, y/2, x/2, y/7, 500)
        WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.IMAGE_AREA))

    def tearDown(self):
        print("tearDown z BaseTest")
        self.driver.quit()
