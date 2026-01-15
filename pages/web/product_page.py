import allure
from selene import browser, have


class ProductPage:
    NAME_PRODUCT = ".product-detail__name.product-detail__name_mb"

    @allure.step("проверка наименования товара")
    def assert_name_product(self, value: str):
        browser.element(self.NAME_PRODUCT).should(have.exact_text(value))
        return self
