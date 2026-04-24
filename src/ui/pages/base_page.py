from playwright.sync_api import Page

from src.ui.browser.browser import Browser
from src.ui.helper.urls import CART_URL, BASE_URL
from src.ui.page_elements.button import Button
from src.ui.page_elements.element import Element
from src.ui.page_elements.text import Text


class BasePage:
    """Логика для тестов на главной странице"""

    def __init__(self, page: Page, url=BASE_URL):
        self.content_text = None
        self.page = page
        self.url = url
        self.browser = Browser(page)
        self.text_monitors = Text(page, strategy="by_text", value="Monitors", allure_name="Monitors")
        self.text_apple_monitors = Text(page, strategy="by_text", value="Apple monitor 24",
                                        allure_name="Apple monitor 24")
        self.element_card = Element(page, strategy="locator", selector=".card-block", allure_name="Карточка товара")
        self.text_card = Text(page, strategy="locator", selector="#cartur", allure_name="Корзина")
        self.header_categories = Element(page, strategy="locator", selector="a#cat", allure_name="Categories")
        # self.element_phones = Element(page, strategy="locator", selector="a#cat+*", allure_name="Phones")
        self.text_phones = Text(page, strategy="by_text", value="Phones", allure_name="Phones")
        self.text_nexus6 = Text(page, strategy="by_text", value="The Motorola Google Nexus 6", allure_name="Nexus 6")
        self.text_laptops = Text(page, strategy="by_text", value="Laptops", allure_name="Laptops")
        self.text_macbook = Text(page, strategy="by_text", value="MacBook Pro line", allure_name="MacBook")
        self.button_nokia = Button(page, strategy="by_role", role="link", value="Nokia Lumia 1520",
                                   allure_name="Nokia Lumia 1520")
        self.element_nokia = Element(page, strategy="locator", selector="#tbodyid", allure_name="Карточка Nokia")

    def open(self):
        """Открывает страницу по URL"""
        return self.browser.go_to_url(self.url)

    def switching_to_monitors(self):
        """Кликает на мониторы"""
        self.text_monitors.click()
        self.text_apple_monitors.wait_for(state="visible")

    def check_cards(self, number_of_cards: int):
        """Проверяет количество карточек с товаром"""
        """number_of_cards - количество карточек с товаром"""
        cnt = self.element_card.get_element().count()
        assert cnt == number_of_cards

    def switching_to_cart(self):
        self.text_card.click()
        assert CART_URL in self.page.url

    def check_header_categories(self):
        """Проверяет что заголовок 'CATEGORIES' присутствует на странице"""
        self.header_categories.check_visible()

    def check_to_phones(self):
        """Проверяет что кнопка 'Phones' активна"""
        self.text_phones.wait_for(state="visible")

    def switching_to_phones(self):
        """Кликает на Phones"""
        self.text_phones.click()
        self.text_nexus6.wait_for(state="visible")

    def check_cards_phones(self, number_of_cards: int):
        """Проверяет количество карточек с товаром в Phones"""
        """number_of_cards - количество карточек с товаром"""
        cnt = self.element_card.get_element().count()
        assert cnt == number_of_cards

    def switching_to_laptops(self):
        """Кликает на Phones"""
        self.text_laptops.click()
        self.text_macbook.wait_for(state="visible")

    def check_cards_laptops(self, number_of_cards: int):
        """Проверяет количество карточек с товаром в Laptops"""
        """number_of_cards - количество карточек с товаром"""
        cnt = self.element_card.get_element().count()
        assert cnt == number_of_cards

    # def switching_to_nokia(self):
    #     """Кликает на Nokia Lumia 1520"""
    #     self.button_nokia.click()
    #     self.element_nokia.wait_for(state="visible")
    #
    # def check_cards_nokia(self, number_of_words: int):
    #     """Проверяет количество слов Nokia в тексте на карточке Nokia"""
    #     content_text = self.element_nokia.get_text()
    #     cnt = content_text.lower().count("nokia")
    #     assert cnt == number_of_words, f"Ожидалось 2 упоминания nokia, найдено {cnt}"
