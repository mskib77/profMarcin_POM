# import HtmlTestRunner
import os
import unittest

from HtmlTestRunner import HTMLTestRunner

from tests.tests_on_main_activity import MainActivityTest
from tests.tests_on_settings_page import SettingsPageTest
from tests.tests_on_info_page import InfoPageTest


MA_tests = unittest.TestLoader().loadTestsFromTestCase(MainActivityTest)
SP_tests = unittest.TestLoader().loadTestsFromTestCase(SettingsPageTest)
IA_tests = unittest.TestLoader().loadTestsFromTestCase(InfoPageTest)

# where test results should be written:
default_dir = os.getcwd()

# Creating the suit that contains all the tests:
# test_suite = unittest.TestSuite([IA_tests])
test_suite = unittest.TestSuite([MA_tests, SP_tests, IA_tests])

# Uruchomenie suite:
if __name__ == "__main__":
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='tests_results', verbosity=2)) -> problemy....
    wyniki = f"{default_dir}/test_results"
    runner = HTMLTestRunner(output=wyniki, verbosity=2)
    runner.run(test_suite)