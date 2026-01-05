import time

import allure
from selene import browser, be, command, have

class CartPage:

    ADD_TO_CART_BUTTON = (
        ".catalog-block__btn.btn.btn_primary.btn_sm.js-catalog-block__btn"
    )
    CONTINUE_BUYING_BUTTON = ".btn.btn_primary.btn_block.js-modal-close"
    CART_BUTTON = '[id="header_basket_count js-header-cart-click"]'
    SELECT_ALL_PRODUCTS_BUTTON = '[for="cart-select-all"]'
    DELETE_ALL_BUTTON = '[id="cart-delete-all"]'
    EMPTY_CART_TITLE = 'h1[class*="header__title"]'


    @allure.step("добавление {count} товаров в корзину")
    def add_products_to_cart(self, count: int = 5):

        add_buttons = browser.all(self.ADD_TO_CART_BUTTON)

        for i in range(count):
            add_buttons[i].click()
            time.sleep(0.5)
            browser.element(self.CONTINUE_BUYING_BUTTON).should(be.clickable).click()

        return self


    @allure.step("проверка счетчика товаров в корзине")
    def assert_cart_count(self, expected_count: int):

        cart_count = browser.element(self.CART_BUTTON).perform(
            command.js.scroll_into_view
        )
        browser.driver.refresh()
        cart_count.should(have.exact_text(f"КОРЗИНА\n{expected_count}"))
        return self

    @allure.step('переход в "корзину"')
    def cart_button_click(self):
        browser.element(self.CART_BUTTON).click()

        return self

    @allure.step("выбор всех товаров")
    def checkbox_select_all_click(self):
        browser.element(self.SELECT_ALL_PRODUCTS_BUTTON).click()

        return self

    @allure.step("удаление всех товаров")
    def cart_delete_all_button_click(self):
        browser.element(self.DELETE_ALL_BUTTON).click()

        return self

    @allure.step("проверка, что корзина очищена")
    def assert_text_empty_cart(self, value):
        browser.element(self.EMPTY_CART_TITLE).should(have.exact_text(value))

        return self
