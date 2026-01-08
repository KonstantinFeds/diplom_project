
import allure
from selene import browser, be, command, have

class CartPage:


    CONTINUE_BUYING_BUTTON = ".btn.btn_primary.btn_block.js-modal-close"
    CART_BUTTON = '[id="header_basket_count js-header-cart-click"]'
    SELECT_ALL_PRODUCTS_BUTTON = '[for="cart-select-all"]'
    DELETE_ALL_BUTTON = '[id="cart-delete-all"]'
    EMPTY_CART_TITLE = 'h1[class*="header__title"]'
    PRODUCT_PRICE_IN_CART = '.side-line__item.col-auto.side-section__price.text-nowrap'
    PRODUCT_NAME_IN_CART = '.cart-block__name'
    BLOCK_PRODUCT_IN_CART = '.cart-block__content.col'


    @allure.step("проверка счетчика {expected_count} товаров в корзине")
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

    @allure.step("выбор товаров")
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


    @allure.step('проверка цены "{value}" товара после добавления в корзину')
    def assert_product_price_in_cart(self, value):
        browser.element(self.PRODUCT_PRICE_IN_CART).should(have.exact_text(value))


    @allure.step('проверка названия "{value}" добавленного товара в корзину')
    def assert_product_name_in_cart(self,value):
        browser.element(self.PRODUCT_NAME_IN_CART).should(have.exact_text(value))


    @allure.step('проверка кол-ва позиций товаров в корзине - "{expected_count}"')
    def assert_product_positions_count_in_cart(self,expected_count: int):
        browser.all(self.BLOCK_PRODUCT_IN_CART).should(have.size(expected_count))
        return self









