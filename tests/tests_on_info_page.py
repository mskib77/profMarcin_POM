from time import sleep

from tests.base_test import BaseTest


class InfoPageTest(BaseTest):

    def setUp(self):
        """Going to Settings Activity before each test"""
        super().setUp()
        self.sa.__go_to_settings_page()

    def test_dummy(self):
        sleep(3)
        pass