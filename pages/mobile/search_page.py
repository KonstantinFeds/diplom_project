import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class SearchPage:
    OPEN_SEARCH_BUTTON = "org.wikipedia.alpha:id/search_container"
    SEARCH_TEXT_INPUT = "org.wikipedia.alpha:id/search_src_text"
    RESULT_LIST = "org.wikipedia.alpha:id/page_list_item_title"

    @allure.step("tap по строке поиска")
    def tap_search(self):
        browser.element((AppiumBy.ID, self.OPEN_SEARCH_BUTTON)).click()

        return self

    @allure.step("ввод текста в строку поиска")
    def insert_text(self, value):
        browser.element((AppiumBy.ID, self.SEARCH_TEXT_INPUT)).type(value)

        return self

    @allure.step("выдача результатов по заданному тексту")
    def assert_name_result(self, value):
        browser.element((AppiumBy.ID, self.RESULT_LIST)).should(have.exact_text(value))

        return self
