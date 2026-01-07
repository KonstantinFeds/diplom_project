import allure
from pages.web.catalog_page import CatalogPage

catalog_page = CatalogPage()


@allure.epic("каталог")
@allure.title('наличие в каталоге "Сабвуферы" товаров')
@allure.severity(allure.severity_level.NORMAL)
def test_go_to_the_catalog_subwoofer(open_site_without_cookies):

    (
        (
            catalog_page.go_to_the_catalog_subwoofer().assert_name_catalog_subwoofer(
                "САБВУФЕРЫ"
            )
        ).assert_products_in_the_catalog(
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


