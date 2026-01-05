import allure
from pages.web.catalog_page import CatalogPage

catalog_page = CatalogPage()


@allure.epic("фильтры")
@allure.title('применение фильтра "АК" и "Булава" в каталоге')
@allure.severity(allure.severity_level.NORMAL)
def test_series_filter_works_in_subwoofers_catalog(open_site_without_cookies):

    (
        (
            (
                catalog_page.go_to_the_catalog_subwoofer().select_filter("АК")
            ).select_filter("Булава")
        ).assert_products_with_filter(
            "СЕРИЯ БУЛАВА", "СЕРИЯ АК", "СЕРИЯ АК", "СЕРИЯ БУЛАВА", "СЕРИЯ БУЛАВА"
        )
    )
