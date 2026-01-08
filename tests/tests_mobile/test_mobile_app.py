import allure
from pages.mobile.login_page import LoginPage
from pages.mobile.search_page import SearchPage
from pages.mobile.onboarding_page import OnboardingPage

onboarding_page = OnboardingPage()
search_page = SearchPage()
login_page = LoginPage()


@allure.epic("авторизация")
@allure.title("авторизация при неверном логине и пароле")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login():

    onboarding_page.skip_onboarding_button_click()
    (
        login_page.more_menu_click()
        .go_to_create_account_page()
        .go_to_login_page()
        .tap_username()
        .insert_username("Test@gmail.com")
        .tap_password()
        .insert_password("test1122")
        .login_button_click()
        .assert_error_msg_login("Invalid characters in username")
    )


@allure.epic("онбординг")
@allure.title("настройка языка")
@allure.severity(allure.severity_level.NORMAL)
def test_add_language():

    (
        onboarding_page.add_or_edit_languages_button_click()
        .add_language_button_click()
        .open_search_tap()
        .insert_language_in_search("Russian")
        .result_click()
        .back_button_click()
        .assert_available_language("Русский")
    )


@allure.epic("поиск")
@allure.title("поиск по заданному тексту")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_by_text():
    onboarding_page.skip_onboarding_button_click()
    (
        search_page.tap_search()
        .insert_text("Gladiator 2000 film")
        .assert_name_result("Gladiator (2000 film)")
    )
