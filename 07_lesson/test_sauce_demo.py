import unittest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage

class TestSauceDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get("https://www.saucedemo.com/")
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def test_purchase_flow(self):
        # Авторизация
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_login()

        # Добавление товаров в корзину
        self.main_page.add_backpack_to_cart()
        self.main_page.add_bolt_tshirt_to_cart()
        self.main_page.add_onesie_to_cart()

        # Переход в корзину и оформление заказа
        self.main_page.go_to_cart()
        self.cart_page.click_checkout()

        # Заполнение формы
        self.checkout_page.fill_first_name("Test")
        self.checkout_page.fill_last_name("User")
        self.checkout_page.fill_postal_code("12345")
        self.checkout_page.click_continue()

        # Получение итоговой стоимости
        total_price = self.checkout_page.get_total_price()

        # Проверка итоговой суммы
        expected_total = "Total: $58.29"
        self.assertEqual(total_price, expected_total,
                        f"Expected total: {expected_total}, but got: {total_price}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
