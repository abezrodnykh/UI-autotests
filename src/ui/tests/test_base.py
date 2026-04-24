import allure


@allure.story("Главная страница")
class TestBasePage:
    @allure.title("Проверка количества карточек с товаром на странице Monitors")
    def test_monitors(self, base_page):
        base_page.open()
        base_page.switching_to_monitors()
        base_page.check_cards(2)

    @allure.title("Проверка перехода в корзину")
    def test_transition_cards(self, base_page):
        base_page.open()
        base_page.switching_to_cart()

    @allure.title("Проверка заголовка CATEGORIES")
    def test_categories(self, base_page):
        base_page.open()
        base_page.check_header_categories()

    @allure.title("Проверка кнопки Phones")
    def test_phones(self, base_page):
        base_page.open()
        base_page.check_to_phones()

    @allure.title("Проверка количества карточек с телефонами на странице Phones")
    def test_phones_cards(self, base_page):
        base_page.open()
        base_page.switching_to_phones()
        base_page.check_cards_phones(9)

    @allure.title("Проверка количества карточек с планшетами на странице Laptops")
    def test_laptops_cards(self, base_page):
        base_page.open()
        base_page.switching_to_laptops()
        base_page.check_cards_laptops(6)

    # @allure.title("Проверка что на карточке Nokia два раза встречается текст 'Nokia'")
    # def test_nokia_cards(self, base_page):
    #     base_page.open()
    #     base_page.switching_to_nokia()
    #     base_page.check_cards_nokia(2)
