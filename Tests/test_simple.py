import pytest
from selenium import webdriver


class TestOne():

    def test_one(self):

        self.driver = webdriver.Chrome(executable_path='/Applications/Python 3.5/chromedriver')
        # self.driver.set_window_size(1280, 1080)
        # self.driver.maximize_window()

        self.driver.get("http://voxan.su/")
        self.driver.close()