import allure
from selene import browser, command, be, have


class FooterComponent:
    GERMAN_LANGUAGE_BUTTON = '[title = "Немецкий"]'
    ALL_TITLE_NAME_CATALOG = '[class="catalog-tile__name"]'

    @allure.step('применение языка в "футере"')
    def select_language(self, language: str = "Немецкий"):
        language_button = browser.all(f'[title="{language}"]')
        language_button[1].should(be.visible)
        language_button[1].perform(command.js.scroll_into_view)
        language_button[1].click()
        return self

    @allure.step("перевод категорий на немецкий язык")
    def assert_catalog_titles(self, *titles):
        browser.all(self.ALL_TITLE_NAME_CATALOG).should(have.exact_texts(*titles))
        return self
