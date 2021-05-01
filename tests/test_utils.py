import os
from datetime import datetime


class TestUtils:
    WAIT_TIME = 10  # system-wide implicit wait

    @classmethod
    def screen_shot(cls, driver, file_name):
        time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        store_file = f'{os.getcwd()}/screenshots/' + time_now + '_' + file_name + '.png'
        # print(f"Sciezka: {store_file}")
        driver.get_screenshot_as_file(store_file)

    @classmethod
    def get_screen_dimensions(cls, driver):
        """ Used before we start scrolling """
        size: dict = driver.get_window_size()
        x = size['width']
        y = size['height']
        return x, y
