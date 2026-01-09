import allure
import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser

import config
import utils.attach


def pytest_addoption(parser):
    """добавляет опцию командной строки --mobile-context"""
    parser.addoption(
        "--mobile-context", default="bstack", help="Specify the test context"
    )


def pytest_configure(config):
    """настройка тестового окружения на основе переданного параметра --mobile-context"""
    mobile_context = config.getoption("--mobile-context")
    env_file_path = f".env.{mobile_context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture(scope="function")
def mobile_context(request):
    """возвращение контекста из командной строки"""
    return request.config.getoption("--mobile-context")


@allure.title("настройка конфигураций для управления девайсом")
@pytest.fixture(scope="function", autouse=True)
def mobile_management(mobile_context):
    options = config.set_mobile_driver_options(mobile_context)

    browser.config.driver = webdriver.Remote(
        options.get_capability("remote_url"), options=options
    )
    browser.config.timeout = 10.0

    yield

    session_id = browser.driver.session_id

    with allure.step("завершение сессии"):
        browser.quit()

    if mobile_context == "bstack":
        utils.attach.attach_bstack_video_android(session_id)
