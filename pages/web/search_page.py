import allure
from selene import browser, have


class SearchPage:

    SEARCH_BUTTON = '[title="Поиск"]'
    INPUT_SEARCH = "#title-search-input"
    SEARCH_RESULT_PRODUCT = 'a.catalog-block__name[href*="molniya-kvark"]'
    NAME_PRODUCT = ".product-detail__name.product-detail__name_mb"

    @allure.step('клик по кнопке "поиска"')
    def click_search_string(self):
        browser.element(self.SEARCH_BUTTON).click()
        return self

    @allure.step('ввод наименования товара: "{value}"')
    def insert_name_product(self, value: str):
        browser.element(self.INPUT_SEARCH).type(value).press_enter()
        return self

    @allure.step('выбор найденного товара')
    def click_on_the_found_product(self):
        browser.element(self.SEARCH_RESULT_PRODUCT).click()
        return self

    @allure.step("проверка наименования товара")
    def assert_name_product(self, value: str):
        browser.element(self.NAME_PRODUCT).should(have.exact_text(value))
        return self