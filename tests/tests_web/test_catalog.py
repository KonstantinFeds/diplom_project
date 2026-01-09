import allure

from pages.web.catalog_page import CatalogPage

catalog_page = CatalogPage()


@allure.epic("каталог")
@allure.title('наличие в каталоге "Сабвуферы" товаров')
@allure.severity(allure.severity_level.NORMAL)
def test_go_to_the_catalog_subwoofer(open_site_without_cookies):
    (
        (
            catalog_page.open_subwoofer_catalog().assert_catalog_subwoofer_title(
                "САБВУФЕРЫ"
            )
        ).assert_products(
            "ТТ 12",
            "МОЛОТ 12",
            "ТТ 15",
            'ПМН-1 "Черная Вдова"',
            "МОЛОТ 10",
            "СИМФОНИЯ 15",
            "УЛЬТИМАТУМ 12",
            "УЛЬТИМАТУМ 15",
            "ПАТРИОТ 6,5",
        )
    )


@allure.epic("фильтры")
@allure.title('применение фильтра "АК" и "Булава" в каталоге')
@allure.severity(allure.severity_level.NORMAL)
def test_series_filter_works_in_subwoofers_catalog(open_site_without_cookies):
    (
        (
            (catalog_page.open_subwoofer_catalog().select_filter("АК")).select_filter(
                "Булава"
            )
        ).assert_products_with_filter(
            "СЕРИЯ БУЛАВА", "СЕРИЯ АК", "СЕРИЯ АК", "СЕРИЯ БУЛАВА", "СЕРИЯ БУЛАВА"
        )
    )
