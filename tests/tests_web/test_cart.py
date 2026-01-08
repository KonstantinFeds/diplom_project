import allure
from pages.web.cart_page import CartPage
from pages.web.catalog_page import CatalogPage

cart_page = CartPage()
catalog_page = CatalogPage()


@allure.epic("корзина")
@allure.title("очистка корзины")
@allure.severity(allure.severity_level.CRITICAL)
def test_removing_products_from_the_cart(open_site_without_cookies):

        catalog_page.open_dinamiki_catalog()

        catalog_page.add_products_to_cart(5)
        cart_page.assert_cart_count(5)
        cart_page.open_cart()
        cart_page.select_all_products_checkbox()
        cart_page.delete_all_products()
        cart_page.assert_text_empty_cart("В КОРЗИНЕ ПУСТО,")

