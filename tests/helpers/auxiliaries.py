import os
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainActivityLocators, SettingsActivityLocators, InfoActivityLocators


class Auxiliaries:
    WAIT_TIME = 10  # system-wide implicit wait

    @classmethod
    def screen_shot(cls, driver, file_name):
        time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        store_file = f'{os.getcwd()}/screenshots/' + time_now + '_' + file_name + '.png'
        # print(f"Sciezka: {store_file}")
        driver.get_screenshot_as_file(store_file)

    @classmethod
    def go_to_settings_page(cls, driver, from_activity):
        """ Auxiliary; brings up the Settings activity. Starts from from_activity """
        WebDriverWait(driver, cls.WAIT_TIME).until(EC.presence_of_element_located(MainActivityLocators.IMAGE_AREA))
        from_activity.long_touch_on_image()
        WebDriverWait(driver, cls.WAIT_TIME).until(EC.presence_of_element_located(SettingsActivityLocators.POZIOM))

    @classmethod
    def go_to_info_page(cls, driver, from_activity_1, from_activity_2):
        """ Auxiliary; brings up the Info activity. Starts from from_activity_1 """
        cls.go_to_settings_page(driver, from_activity_1)
        from_activity_2.get_info_button().click()  # while calling the method, actual 'from_activity_2' should be an instance of MainActivity
        WebDriverWait(driver, cls.WAIT_TIME).until(EC.presence_of_element_located(InfoActivityLocators.ACTION_BAR_TITLE))

    @classmethod
    def get_screen_dimensions(cls, driver):
        """ Used before we start scrolling """
        size: dict = driver.get_window_size()
        x = size['width']
        y = size['height']
        return x, y


