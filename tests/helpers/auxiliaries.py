import os
from datetime import datetime


class Auxiliaries:
    WAIT_TIME = 10  # implicit wait

    @classmethod
    def screen_shot(cls, driver, file_name):
        time_now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        store_file = f'{os.getcwd()}/screenshots/' + time_now + '_' + file_name + '.png'
        print(f"Sciezka: {store_file}")
        driver.get_screenshot_as_file(store_file)
