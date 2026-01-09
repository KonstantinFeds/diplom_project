import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


class OnboardingPage:
    CKIP_ONBOARDING_BUTTON = "org.wikipedia.alpha:id/fragment_onboarding_skip_button"
    ADD_OR_EDIT_LANGUAGES_BUTTON = "org.wikipedia.alpha:id/addLanguageButton"
    ADD_LANGUAGE_BUTTON = 'text("Add language")'
    ADD_LANGUAGE_OPEN_SEARCH = 'className("android.widget.Button").instance(1)'
    ADD_LANGUAGE_SEARCH_INPUT = 'text("Search for a language")'
    INSERT_LANGUAGE = "android.widget.EditText"
    LANGUAGE_RESULT = 'text("Русский")'
    BACK_BUTTON = "Navigate up"
    AVAILABLE_LANGUAGE = "org.wikipedia.alpha:id/option_label"

    @allure.step("пропуск онбординга")
    def skip_onboarding_button_click(self):
        browser.element((AppiumBy.ID, self.CKIP_ONBOARDING_BUTTON)).click()

        return self

    @allure.step('клик по кнопке "добавить или отредактировать язык"')
    def add_or_edit_languages_button_click(self):
        browser.element((AppiumBy.ID, self.ADD_OR_EDIT_LANGUAGES_BUTTON)).click()

        return self

    @allure.step('клик по кнопке "добавить язык"')
    def add_language_button_click(self):
        browser.element(
            (AppiumBy.ANDROID_UIAUTOMATOR, self.ADD_LANGUAGE_BUTTON)
        ).click()

        return self

    @allure.step("tap по строке поиска")
    def open_search_tap(self):
        (
            browser.element(
                (AppiumBy.ANDROID_UIAUTOMATOR, self.ADD_LANGUAGE_OPEN_SEARCH)
            ).click()
        )

        return self

    @allure.step("ввод названия языка")
    def insert_language_in_search(self, value):
        browser.element((AppiumBy.CLASS_NAME, self.INSERT_LANGUAGE)).type(value)

        return self

    @allure.step("клик по выдаче результатов")
    def result_click(self):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, self.LANGUAGE_RESULT)).click()

        return self

    @allure.step("возврат начальную страницу")
    def back_button_click(self):
        browser.element((AppiumBy.ACCESSIBILITY_ID, self.BACK_BUTTON)).click()

        return self

    @allure.step("наличие добавленного языка на начальной странице")
    def assert_available_language(self, value):
        browser.all((AppiumBy.ID, self.AVAILABLE_LANGUAGE))[1].should(have.text(value))

        return self
