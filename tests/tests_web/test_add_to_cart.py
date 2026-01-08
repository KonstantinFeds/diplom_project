
import allure
from pages.web.cart_page import CartPage
from pages.web.catalog_page import CatalogPage

cart_page = CartPage()
catalog_page = CatalogPage()


@allure.epic("добавление товара в корзину")
@allure.title("счетчик кол-ва товара в корзине")
@allure.severity(allure.severity_level.CRITICAL)
def test_product_counter_in_cart(open_site_without_cookies):

    catalog_page.go_to_the_catalog_dinamiki()
    catalog_page.add_products_to_cart(5)
    cart_page.assert_cart_count(5)


@allure.epic("добавление товара в корзину")
@allure.title("добавление товара в корзину")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_product(open_site_without_cookies):

    catalog_page.go_to_the_catalog_dinamiki()
    catalog_page.assert_product_price_in_catalog("5 590 ₽")
    catalog_page.add_product_to_cart("АК-74 М")

    cart_page.cart_button_click()
    cart_page.assert_product_price_in_cart("5 590 ₽")
    cart_page.assert_product_name_in_cart("АК-74 М")
    cart_page.assert_product_positions_count_in_cart(1)






