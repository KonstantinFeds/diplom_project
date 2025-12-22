import os
import shutil
from pathlib import Path
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.chrome.options import Options
import utils.file

def clear_allure_results():
    """очистка результатов модуля allure-results"""
    allure_dir = Path("allure-results")

    if allure_dir.exists():
        shutil.rmtree(allure_dir)

    allure_dir.mkdir(exist_ok=True)


def to_driver_options_web(web_context):
    """настройка конфигурация от переданного параметра --web-context"""
    if web_context == "local_browser":
        browser.config.base_url = "https://ural-auto.ru/"
        browser.config.timeout = 10
        browser.config.window_width = 1495
        browser.config.window_height = 870

        # Создаем локальный драйвер Chrome
        options = Options()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=options)
        browser.config.driver = driver

    if web_context == "selenoid":
        # Selenoid
        browser.config.base_url = "https://ural-auto.ru/"
        browser.config.timeout = 10
        browser.config.window_width = 1495
        browser.config.window_height = 870

        # Настройки Selenoid
        options = Options()
        options.page_load_strategy = 'eager'

        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "128.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
            },
        }

        load_dotenv(dotenv_path=utils.file.abs_path_from_project(".env.credentials"))
        options.capabilities.update(selenoid_capabilities)

        # Создаем удаленный драйвер
        driver = webdriver.Remote(
            command_executor=f"https://{os.getenv('SELENOID_LOGIN')}:{os.getenv('SELENOID_PASSWORD')}@{os.getenv('SELENOID_URL')}/wd/hub",
            options=options,
        )
        browser.config.driver = driver

    return browser


def to_driver_options_mobile(mobile_context):
    """настройка конфигурация от переданного параметра --mobile-context"""
    options = UiAutomator2Options()
    if mobile_context == "local_emulator":
        options.set_capability("remote_url", os.getenv("REMOTE_URL"))
        options.set_capability("deviceName", os.getenv("DEVICE_NAME"))
        options.set_capability("appWaitActivity", os.getenv("APP_WAIT_ACTIVITY"))
        options.set_capability(
            "app", utils.file.abs_path_from_project(os.getenv("APP"))
        )

    if mobile_context == "bstack":
        options.set_capability("remote_url", os.getenv("REMOTE_URL"))
        options.set_capability("deviceName", os.getenv("DEVICE_NAME"))
        options.set_capability("platformName", os.getenv("PLATFORM_NAME"))
        options.set_capability("platformVersion", os.getenv("PLATFORM_VERSION"))
        options.set_capability("appWaitActivity", os.getenv("APP_WAIT_ACTIVITY"))
        options.set_capability("app", os.getenv("APP"))
        load_dotenv(dotenv_path=utils.file.abs_path_from_project(".env.credentials"))
        options.set_capability(
            "bstack:options",
            {
                "projectName": "First Python project",
                "buildName": "browserstack-task-number-20",
                "sessionName": "BStack android test",
                "userName": os.getenv("USER_NAME_BSTACK"),
                "accessKey": os.getenv("ACCESS_KEY_BSTACK"),
            },
        )

    return options
