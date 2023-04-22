from pages.page import YandexPage
import time


def test_yandex_search(browser):
    yandex_main_page = YandexPage(browser)
    yandex_main_page.go_to_site()
    time.sleep(20)
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.check_popup_content()
    yandex_main_page.click_on_the_search_button()
    page_url = browser.current_url
    yandex_main_page.check_search_url(page_url)
    link = yandex_main_page.get_first_link()
    yandex_main_page.check_first_url(link)


def test_yandex_image(browser):
    yandex_main_page = YandexPage(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.click_on_the_menu_button()
    yandex_main_page.click_on_the_image_button()
    image_url = browser.current_url



