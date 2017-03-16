from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestSearch:

    def test_search_success(self, setup):
        self.driver.get("http://voxan.su/")
        search = self.driver.find_element_by_id(search_input)
        search.send_keys('обои')
        search.send_keys(Keys.RETURN)
        sleep(5)
        assert "Сожалеем, но ничего не найдено." not in self.driver.page_source

    def test_search_not_found(self, setup):
        """
        Тест отображаения сообщения "Сожалеем, но ничего не найдено" в результатах поиска
        """
        self.driver.get("http://voxan.su/")
        search = self.driver.find_element_by_id(search_input)
        search.send_keys('вдвааолв')
        search.send_keys(Keys.RETURN)
        sleep(5)
        assert "Сожалеем, но ничего не найдено." in self.driver.page_source

    @pytest.fixture(scope='function')
    def setup(self):
        self.driver = webdriver.Chrome(executable_path='/Applications/Python 3.5/chromedriver')

        global search_input
        search_input = 'title-search-input2'
        # self.driver.set_window_size(1280, 1080)

    def teardown(self):
        self.driver.close()
