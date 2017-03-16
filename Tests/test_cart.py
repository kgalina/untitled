from time import sleep

import pytest
from hamcrest import assert_that, contains_string, equal_to
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestCart:

    def test_one_item_page(self, setup):
        """
        Тест добавления товара в корзину
        Шаги: 1. Выполнить поиск
        2. Кликнуть кнопку "В корзину"
        3. Кликнуть кнопку "Перейти в корзину".
        ОР: Открыта страница корзины с добавленним товаром
        """
        self.driver.get("http://voxan.su/")
        search = self.driver.find_element_by_id(search_input)
        search.send_keys('краска')
        search.send_keys(Keys.RETURN)
        sleep(2)
        item = self.driver.find_element_by_xpath(".//img[contains(@title,'Tintoflex City')]")
        item.click()
        sleep(2)

        #Проверка отображения заголовка товара на штучной странице
        page_title = self.driver.find_element_by_id('pagetitle')
        assert_that(page_title.text, contains_string('Tintoflex')) #проверка, что заголовок содержит заданный текст

        # Клик по кнопке "В корзину" в всплывающей форме "Корзина заказа"
        add_to_cart = self.driver.find_element_by_xpath(".//span[text() = 'В корзину']")

        add_to_cart.click()

        sleep(6)
        open_cart  = self.driver.find_element_by_xpath(".//*[@id='basket_form']/..//span[text() = 'Перейти в корзину']")
        open_cart.click()
        sleep(4)
        # Проверка наличия заголовка 'Корзина' на странице корзины
        page_title = self.driver.find_element_by_id('pagetitle')
        assert_that(page_title.text, equal_to('Корзина'))

        # Проверка наличия текста "Готовые к заказу" на странице корзины
        ready = self.driver.find_element_by_xpath(".//*[@class='wrap_li']")
        assert_that(ready.text, contains_string('Готовые к заказу'))

    @pytest.fixture(scope='function')
    def setup(self):
        global search_input
        search_input = 'title-search-input2'

        self.driver = webdriver.Chrome(executable_path='/Applications/Python 3.5/chromedriver')
        # self.driver.set_window_size(1280, 1080)
        # self.driver.maximize_window()

    def teardown(self):
        self.driver.close()
