from pages.base import BasePage
from pages.locators import SearchLocators, ImagesLocators, SitesUrls


class YandexPage(BasePage):
    """ Accessory methods for working with Yandex page. """

    def enter_word(self, word):
        """ Enters the word in the search field. """
        search_field = self.find_element(
            SearchLocators.LOCATOR_YANDEX_SEARCH_FIELD
        )
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def check_popup_content(self):
        """ Checks the popup content. """
        popup_content = self.find_element(
            SearchLocators.LOCATOR_YANDEX_POPUP_CONTENT
        )
        return popup_content

    def click_on_the_search_button(self):
        """ Clicks on the search button. """
        return self.find_element(
            SearchLocators.LOCATOR_YANDEX_SEARCH_BUTTON, time=2
        ).click()

    def click_on_the_image_button(self):
        """ Clicks on the image button. """
        return self.find_element(
            ImagesLocators.LOCATOR_YANDEX_IMAGE_BUTTON, time=2
        ).click()

    def click_on_the_first_category(self):
        """ Clicks on the first category. """
        return self.find_element(
            ImagesLocators.LOCATOR_YANDEX_FIRST_CATEGORY, time=2
        ).click()

    def click_on_the_first_image(self):
        """ Clicks on the first image. """
        return self.find_element(
            ImagesLocators.LOCATOR_YANDEX_FIRST_IMAGE, time=2
        ).click()

    def click_on_the_next_image(self):
        """ Clicks on the next image button. """
        return self.find_element(
            ImagesLocators.LOCATOR_YANDEX_NEXT_BUTTON, time=2
        ).click()

    def click_on_the_previous_image(self):
        """ Clicks on the previous image button. """
        return self.find_element(
            ImagesLocators.LOCATOR_YANDEX_PREVIOUS_BUTTON, time=2
        ).click()

    def click_on_the_menu_button(self):
        """ Clicks on the menu button. """
        search_field = self.find_element(
            SearchLocators.LOCATOR_YANDEX_SEARCH_FIELD
        )
        search_field.click()
        menu_button = self.find_element(
            ImagesLocators.LOCATOR_YANDEX_MENU_BUTTON
        )
        menu_button.click()
        return menu_button

    def get_first_link(self):
        """ Gets the first link in page. """
        all_links = self.find_elements(
            SearchLocators.LOCATOR_YANDEX_PAGE_PATH, time=2
        )
        links = [x.text for x in all_links if len(x.text) > 0]
        first_link = links[:1]
        return first_link

    def get_category_name(self):
        """ Gets the category name. """
        text = self.find_element(
            ImagesLocators.LOCATOR_YANDEX_FIRST_CATEGORY
        ).text
        return text

    def get_search_name(self):
        """ Gets the name in search field. """
        search = self.find_element(
            ImagesLocators.LOCATOR_YANDEX_SEARCH_FIELD_IMAGE_NAME
        )
        text = search.get_attribute('data-text')
        return text

    def check_text_in_search_field(self, category_name, search_text):
        """ Checks the name in search field and category name. """
        assert category_name.lower() == search_text, \
            'The search field does not match the category name'

    def check_next_image(self, first_image, next_image):
        """ Checks the next image navigation. """
        assert first_image != next_image, \
            "The next image is incorrect"

    def check_previous_image(self, previous_image, first_image):
        """ Checks the next image navigation. """
        assert first_image == previous_image, \
            "The previous image is incorrect"

    def check_first_url(self, url):
        """ Checks the first url on the page. """
        assert SitesUrls.TENSOR_URL in url, \
            f"The first URL is not {SitesUrls.TENSOR_URL}"

    def check_search_url(self, url):
        """ Checks the urls searching. """
        assert SitesUrls.SEARCH_URL in url, \
            f"{SitesUrls.SEARCH_URL} was not found"

    def check_image_url(self, url):
        """ Checks the navigation to the image page. """
        assert SitesUrls.IMAGES_URL in url, \
            f"{SitesUrls.IMAGES_URL} was not found"
