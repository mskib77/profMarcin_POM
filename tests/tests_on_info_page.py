from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainActivityLocators
from tests.base_test import BaseTest
from tests.test_utils import TestUtils


class InfoPageTest(BaseTest):

    def setUp(self):
        """Going to Info Activity before each test"""
        super().setUp()
        TestUtils.go_to_info_page(self.driver, self.ma, self.sa)

    def test_switching_to_main_activity(self):
        """Can we switch to Main Activity while on Info page?"""
        bstart = self.ia.get_start_button()
        bstart.click()
        test_ok = False
        try:
            WebDriverWait(self.driver, TestUtils.WAIT_TIME).until(
                EC.presence_of_element_located(MainActivityLocators.WORD_BUTTONS_LIST))
            test_ok = True
        except NoSuchElementException:
            test_ok = False
        finally:
            sleep(2)

        self.assertTrue(test_ok, "Main Activity did not appear!")
