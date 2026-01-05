import allure
from pages.web.cart_page import CartPage
from pages.web.catalog_page import CatalogPage

cart_page = CartPage()
catalog_page = CatalogPage()


@allure.epic("добавление товара в корзину")
@allure.title("добавление товаров в корзину")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_product(open_site_without_cookies):

    catalog_page.go_to_the_catalog_dinamiki()
    (cart_page.add_products_to_cart(5).assert_cart_count(5))
