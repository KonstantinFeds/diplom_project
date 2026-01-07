import time
import allure
from selene import browser, have, be


class CatalogPage:

    TITLE_CATALOG_SUBWOOFERS = ".page-header__title"
    ALL_PRODUCTS_CATALOG = ".catalog-block__name"
    CHECKBOX_SERIES_NAME_AK = '//label[text()="АК"]'
    CHECKBOX_SERIES_NAME_BULAVA = '//label[text()="Булава"]'
    CATALOG_RESULTS_PRODUCTS = '[class="catalog-block__helper"]'
    PRODUCT_PRICE_IN_CATALOG = '.catalog-block__price.catalog-block__price_new'
    CONTINUE_BUYING_BUTTON = ".btn.btn_primary.btn_block.js-modal-close"
    ADD_TO_CART_BUTTON = (
        ".catalog-block__btn.btn.btn_primary.btn_sm.js-catalog-block__btn"
    )

    @allure.step('переход в каталог "Cабвуферы"')
    def go_to_the_catalog_subwoofer(self):
        browser.open("/catalog/subwoofers/")
        return self

    @allure.step('переход в каталог "Акустика"')
    def go_to_the_catalog_dinamiki(self):
        browser.open("/catalog/dinamiki/")
        return self

    @allure.step('проверка наименования каталога "Cабвуферы"')
    def assert_name_catalog_subwoofer(self, value):
        browser.element(self.TITLE_CATALOG_SUBWOOFERS).should(have.exact_text(value))

        return self

    @allure.step("проверка наличия товаров в каталоге")
    def assert_products_in_the_catalog(self, *products):
        (browser.all(self.ALL_PRODUCTS_CATALOG).should(have.exact_texts(*products)))

        return self

    @allure.step('выбор фильтра "{filter_name}"')
    def select_filter(self, filter_name):
        browser.element(f'//label[text()="{filter_name}"]').click()
        return self

    @allure.step("проверка товаров после применения фильтра")
    def assert_products_with_filter(self, *products):
        browser.all(self.CATALOG_RESULTS_PRODUCTS).should(have.exact_texts(*products))

        return self

    @allure.step('проверка цены "{value}" товара в каталоге')
    def assert_product_price_in_catalog(self, value):
        browser.all(self.PRODUCT_PRICE_IN_CATALOG).element_by(have.text(value)).should(be.visible)


    @allure.step('добавление товара "{product_title}" в корзину')
    def add_product_to_cart(self,product_title):
        button_locator = f'//a[@class="catalog-block__btn btn btn_primary btn_sm js-catalog-block__btn" and @data-title=" {product_title}"]'
        browser.element(button_locator).click()
        time.sleep(0.5)
        browser.element(self.CONTINUE_BUYING_BUTTON).should(be.clickable).click()


    @allure.step("добавление {count} товаров в корзину")
    def add_products_to_cart(self, count: int = 5):

        add_buttons = browser.all(self.ADD_TO_CART_BUTTON)

        for i in range(count):
            add_buttons[i].click()
            time.sleep(0.5)
            browser.element(self.CONTINUE_BUYING_BUTTON).should(be.clickable).click()

        return self
