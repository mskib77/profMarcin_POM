import unittest
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainActivityLocators as MAL, InfoActivityLocators as IAL
from tests.base_test import BaseTest
from tests.test_utils import TestUtils


class InfoPageTest(BaseTest):

    def setUp(self):
        """Going to Info Activity before each test"""
        super().setUp()
        self._go_to_info_page(self.driver)

    def _go_to_info_page(self, driver):
        """ Auxiliary; brings up the Info activity. Starts from SettingsActivity """
        """ Called by setUp() """
        # Going to Settings page:
        self.ma.long_touch_on_image_area()
        # Going to Info page:
        self.sa.get_info_button().click()
        WebDriverWait(driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(IAL.ACTION_BAR_TITLE))

    # No 11 test case in documentation
    # @unittest.skip
    def test_switching_to_main_activity(self):
        """Can we switch to Main Activity while on Info page?"""
        bstart = self.ia.get_start_button()
        bstart.click()
        test_ok = False
        try:
            WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.IMAGE))
            WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(EC.presence_of_element_located(MAL.WORD_BUTTONS_LIST))
            test_ok = True
        except TimeoutException:
            test_ok = False
        finally:
            sleep(2)
        self.assertTrue(test_ok, "Main Activity did not appear!")


if __name__ == '__main__':
    unittest.main()
