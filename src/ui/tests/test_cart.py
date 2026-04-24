import allure

@allure.story("Страница Корзина")
class TestCartPage:

    @allure.title("Проверка кнопки Place Order")
    def test_cart(self, cart_page):
        cart_page.open()
        cart_page.check_place_order_button()
