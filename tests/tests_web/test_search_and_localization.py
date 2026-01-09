import allure
from pages.web.search_page import SearchPage
from pages.web.footer_component import FooterComponent

search_page = SearchPage()
footer_page = FooterComponent()



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


@allure.epic("footer сайта")
@allure.title("переключение языка на сайта")
@allure.severity(allure.severity_level.MINOR)
def test_switch_to_german_language(open_site_without_cookies):

        footer_page.select_language("Немецкий").assert_catalog_titles(
            "Kopf -\nGerät",
            "Die akustischen\nSysteme",
            "Ein lautes\nGeräusch",
            "Subwoofer",
            "Verstärker",
            "Kopfhörer",
            "Tragbare\nAkustik",
        )

