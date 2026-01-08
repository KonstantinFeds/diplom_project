import allure
from dotenv import load_dotenv
import pytest
from selene import browser, be
import config
from utils import attach



def pytest_addoption(parser):
    """добавляет опцию командной строки --web-context"""
    parser.addoption(
        "--web-context",
        default="local_browser",  # значение по умолчанию
        help="Specify the test context",
    )


def pytest_configure(config):
    """настройка тестового окружения на основе переданного параметра --context"""
    web_context = config.getoption("--web-context")
    env_file_path = f".env.{web_context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture(scope="function")
def web_context(request):
    """возвращение контекста из командной строки"""
    return request.config.getoption("--web-context")


@allure.title("настройка конфигураций для управления браузером")
@pytest.fixture(scope="function", autouse=True)
def browser_management(web_context):
    config.set_web_driver_options(web_context)

    yield

    if web_context == "selenoid":
        attach.add_selenoid_video(browser)
        attach.add_screenshot_selenoid(browser)
        attach.add_logs_selenoid(browser)
        attach.add_html_selenoid(browser)

    with allure.step("завершение сессии"):
        browser.quit()


@allure.title("открытие сайта и обработка cookies")
@pytest.fixture(scope="function")
def open_site_without_cookies():

    ACCEPT_COOKIES_BUTTON = ".js-message-block__close"

    browser.open_login_page("/")
    browser.element(ACCEPT_COOKIES_BUTTON).should(be.clickable).click()

    yield
