import os

import allure
from dotenv import load_dotenv

import utils.file
from pages.web.login_page import LoginPage

login_page = LoginPage()
load_dotenv(dotenv_path=utils.file.abs_path_from_project(".env.credentials"))


@allure.epic("авторизация")
@allure.title("успешный логин пользователя")
@allure.severity(allure.severity_level.CRITICAL)
def test_success_login(open_site_without_cookies):
    (
        login_page.open_login_page()
        .input_login(os.getenv("WEB_USER_LOGIN"))
        .input_password(os.getenv("WEB_USER_PASSWORD"))
        .login_button_click()
        .assert_user_name_in_profile(f"Здравствуйте, {os.getenv('WEB_USER_LOGIN')}!")
    )


@allure.epic("авторизация")
@allure.title("сообщение об ошибке при неверном вводе логина и пароля")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login(open_site_without_cookies):
    (
        login_page.open_login_page()
        .input_login("TestLogin@mail.ru")
        .input_password("TestPassword")
        .login_button_click()
        .assert_login_error_message("Неверный логин или пароль.")
    )
