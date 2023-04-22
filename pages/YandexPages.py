import time
from pages.BaseApp import BasePage
from pages.locators import YandexSearchLocators, TenzorParams


class YandexPage(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def check_popup_content(self):
        popup_content = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_POPUP_CONTENT)
        return popup_content

    def click_on_the_search_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2).click()

    def click_on_the_image_button(self):
        return self.find_element(YandexSearchLocators.LOCATOR_YANDEX_IMAGE_BUTTON, time=2).click()

    def click_on_the_first_category(self):
        all_category = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_FIRST_CATEGORY, time=2)
        category = [x.text for x in all_category if len(x.text) > 0]
        first_category = category[:1]
        return first_category

    def click_on_the_menu_button(self):
        search_field = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        menu_button = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_MENU_BUTTON)
        menu_button.click()
        return menu_button

    def get_first_link(self):
        all_links = self.find_elements(YandexSearchLocators.LOCATOR_YANDEX_PAGE_PATH, time=2)
        links = [x.text for x in all_links if len(x.text) > 0]
        first_link = links[:1]
        return first_link

    def check_image_navigation(self):
        next_button = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_NEXT_BUTTON)
        next_button.click()
        time.sleep(5)
        prev_button = self.find_element(YandexSearchLocators.LOCATOR_YANDEX_PREVIOUS_BUTTON)
        prev_button.click()
        time.sleep(5)
        return prev_button

    def check_link(self, link):
        assert link == TenzorParams.TENZOR_URL
