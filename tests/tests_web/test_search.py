import allure
from pages.web.search_page import SearchPage

search_page = SearchPage()


@allure.epic("поиск")
@allure.title("поиск товара по названию")
@allure.severity(allure.severity_level.CRITICAL)
def test_search_by_product_name(open_site_without_cookies):
    (
        search_page.click_search_string()
        .insert_name_product("УРАЛ")
        .click_on_the_found_product("МОЛНИЯ КВАРК")
        .assert_name_product("УРАЛ МОЛНИЯ КВАРК\nПортативная акустическая система")
    )
