import allure
from selene import browser, have


class LoginPage:

    LOGIN_PAGE_BUTTON = ".nav-panel__link_login"
    INPUT_USER_LOGIN = '[name="USER_LOGIN"]'
    INPUT_USER_PASSWORD = '[name="USER_PASSWORD"]'
    LOGIN_BUTTON = '[name="Login"]'
    LOGIN_ERROR_MESSAGE = ".auth-error.form-group.form-helper"
    USER_NAME = '.profile-header__title'


    @allure.step("открытие страницы логина")
    def open_login_page(self):
        browser.open("/login/")
        return self


    @allure.step("ввод логина")
    def input_login(self, value):
        browser.element(self.INPUT_USER_LOGIN).type(value)

        return self

    @allure.step("ввод пароля")
    def input_password(self, value):
        browser.element(self.INPUT_USER_PASSWORD).type(value)
        return self

    @allure.step("клик по кнопке логина")
    def login_button_click(self):
        browser.element(self.LOGIN_BUTTON).click()
        return self

    @allure.step("проверка сообщения об ошибке авторизации")
    def assert_login_error_message(self, value):
        browser.element(self.LOGIN_ERROR_MESSAGE).should(have.exact_text(value))
        return self

    @allure.step("проверка имени пользователя в профиле: {value}")
    def assert_user_name_in_profile(self,value):
        browser.element(self.USER_NAME).should(have.exact_text(value))


