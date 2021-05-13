# -*- coding: utf-8" -*
import unittest
from tests.tests_on_main_activity import MainActivityTest
from tests.tests_on_settings_page import SettingsPageTest
from tests.tests_on_info_page import InfoPageTest


MA_tests = unittest.TestLoader().loadTestsFromTestCase(MainActivityTest)
SP_tests = unittest.TestLoader().loadTestsFromTestCase(SettingsPageTest)
IA_tests = unittest.TestLoader().loadTestsFromTestCase(InfoPageTest)

# Creating test suit that contains all the tests:
test_suite = unittest.TestSuite([MA_tests, SP_tests, IA_tests])

# Running tests:
unittest.TextTestRunner(verbosity=2).run(test_suite)
