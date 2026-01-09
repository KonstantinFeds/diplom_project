import pytest

import config


@pytest.fixture(scope="session", autouse=True)
def clean_allure_results():
    """Очистка allure-результатов"""
    config.clean_allure_results()
