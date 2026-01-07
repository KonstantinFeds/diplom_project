import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

class LoginPage:

    MORE_MENU_BUTTON = "More"
    LOGIN_MENU_BUTTON = "org.wikipedia.alpha:id/main_drawer_login_button"
    LOGIN_PAGE_BUTTON = "org.wikipedia.alpha:id/create_account_login_button"
    USERNAME = '//android.widget.EditText[@text="Username"]'
    PASSWORD = '//android.widget.EditText[@text="Password"]'
    LOGIN_BUTTON = "org.wikipedia.alpha:id/login_button"
    ERROR_MSG_LOGIN = "org.wikipedia.alpha:id/textinput_error"

    @allure.step('клик по меню "More"')
    def more_menu_click(self):
        browser.element(
            (AppiumBy.ACCESSIBILITY_ID, self.MORE_MENU_BUTTON)
        ).click()
        return self

    @allure.step("переход на страницу создания аккаунта")
    def go_to_create_account_page(self):
        browser.element((AppiumBy.ID, self.LOGIN_MENU_BUTTON)).click()
        return self

    @allure.step("переход на страницу логина")
    def go_to_login_page(self):
        browser.element((AppiumBy.ID, self.LOGIN_PAGE_BUTTON)).click()
        return self

    @allure.step('tap по полю "username"')
    def username_tap(self):
        browser.element((AppiumBy.XPATH, self.USERNAME)).click()
        return self

    @allure.step("ввод username")
    def insert_username(self, value):
        browser.element((AppiumBy.XPATH, self.USERNAME)).type(value)
        return self

    @allure.step('tap по полю "password"')
    def password_tap(self):
        browser.element((AppiumBy.XPATH, self.PASSWORD)).click()
        return self

    @allure.step("ввод password")
    def insert_password(self, value):
        browser.element((AppiumBy.XPATH, self.PASSWORD)).type(value)

        return self

    @allure.step("клик по кнопке Log in")
    def login_button_click(self):
        browser.element((AppiumBy.ID, self.LOGIN_BUTTON)).click()

        return self

    @allure.step("наличие сообщения об неверном логине и пароля")
    def assert_error_msg_login(self, value):
        browser.element((AppiumBy.ID, self.ERROR_MSG_LOGIN)).should(
            have.exact_text(value)
        )

        return self
