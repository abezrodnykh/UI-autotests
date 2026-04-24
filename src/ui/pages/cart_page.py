from playwright.sync_api import Page

from src.ui.helper.urls import BASE_URL, CART_URL
from src.ui.page_elements.button import Button
from src.ui.pages.base_page import BasePage


class CartPage(BasePage):
    """Логика для тестов на странице Корзина"""

    def __init__(self, page: Page, url=BASE_URL + CART_URL):
        super().__init__(page, url)
        self.button_place_order = Button(page, strategy="by_role", role="button", value="Place Order", allure_name="Place Order")

    def check_place_order_button(self):
        self.button_place_order.check_visible()
