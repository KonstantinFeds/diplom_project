import allure
from selene import browser, have


class CatalogPage:

    TITLE_CATALOG_SUBWOOFERS = ".page-header__title"
    ALL_PRODUCTS_CATALOG = ".catalog-block__name"
    CHECKBOX_SERIES_NAME_AK = '//label[text()="АК"]'
    CHECKBOX_SERIES_NAME_BULAVA = '//label[text()="Булава"]'
    CATALOG_RESULTS_PRODUCTS = '[class="catalog-block__helper"]'

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
