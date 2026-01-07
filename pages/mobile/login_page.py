import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
from pages.mobile.locators import LocatorsMob


class LoginPage:

    @allure.step('клик по меню "More"')
    def more_menu_click(self):
        browser.element(
            (AppiumBy.ACCESSIBILITY_ID, LocatorsMob.MORE_MENU_BUTTON)
        ).click()
        return self

    @allure.step("переход на страницу создания аккаунта")
    def go_to_create_account_page(self):
        browser.element((AppiumBy.ID, LocatorsMob.LOGIN_MENU_BUTTON)).click()
        return self

    @allure.step("переход на страницу логина")
    def go_to_login_page(self):
        browser.element((AppiumBy.ID, LocatorsMob.LOGIN_PAGE_BUTTON)).click()
        return self

    @allure.step('tap по полю "username"')
    def username_tap(self):
        browser.element((AppiumBy.XPATH, LocatorsMob.USERNAME)).click()
        return self

    @allure.step("ввод username")
    def insert_username(self, value):
        browser.element((AppiumBy.XPATH, LocatorsMob.USERNAME)).type(value)
        return self

    @allure.step('tap по полю "password"')
    def password_tap(self):
        browser.element((AppiumBy.XPATH, LocatorsMob.PASSWORD)).click()
        return self

    @allure.step("ввод password")
    def insert_password(self, value):
        browser.element((AppiumBy.XPATH, LocatorsMob.PASSWORD)).type(value)

        return self

    @allure.step("клик по кнопке Log in")
    def login_button_click(self):
        browser.element((AppiumBy.ID, LocatorsMob.LOGIN_BUTTON)).click()

        return self

    @allure.step("наличие сообщения об неверном логине и пароля")
    def assert_error_msg_login(self, value):
        browser.element((AppiumBy.ID, LocatorsMob.ERROR_MSG_LOGIN)).should(
            have.exact_text(value)
        )

        return self
