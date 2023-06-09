from pages.page import YandexPage
import time
import logging

LOGGER = logging.getLogger(__name__)


def test_yandex_search(browser):
    """ The first test case of checking the search on the Yandex page. """
    yandex_main_page = YandexPage(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.check_popup_content()
    yandex_main_page.click_on_the_search_button()
    page_url = browser.current_url
    yandex_main_page.check_search_url(page_url)
    link = yandex_main_page.get_first_link()
    yandex_main_page.check_first_url(link)


def test_yandex_image(browser):
    """ The second test case of checking the images on the Yandex page. """
    yandex_main_page = YandexPage(browser)
    yandex_main_page.go_to_site()
    yandex_main_page.click_on_the_menu_button()
    yandex_main_page.click_on_the_image_button()
    browser.switch_to.window(browser.window_handles[1])
    image_url = browser.current_url
    yandex_main_page.check_image_url(image_url)
    category_name = yandex_main_page.get_category_name()
    yandex_main_page.click_on_the_first_category()
    search_name = yandex_main_page.get_search_name()
    yandex_main_page.check_text_in_search_field(category_name, search_name)
    yandex_main_page.click_on_the_first_image()
    time.sleep(1)
    first_image = browser.current_url
    yandex_main_page.click_on_the_next_image()
    time.sleep(1)
    next_image = browser.current_url
    yandex_main_page.check_next_image(first_image, next_image)
    yandex_main_page.click_on_the_previous_image()
    time.sleep(1)
    previous_image = browser.current_url
    yandex_main_page.check_previous_image(previous_image, first_image)
