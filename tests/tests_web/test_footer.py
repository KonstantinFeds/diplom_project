import allure
from pages.web.footer_component import FooterComponent

footer_page = FooterComponent()


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

