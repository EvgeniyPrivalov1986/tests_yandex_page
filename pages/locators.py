from selenium.webdriver.common.by import By


class SearchLocators:
    """ Locators on the Yandex search page. """
    LOCATOR_YANDEX_SEARCH_FIELD = (
        By.CSS_SELECTOR,
        "input[class*=search3__input]"
    )
    LOCATOR_YANDEX_SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        "button[class*=search3__button]"
    )
    LOCATOR_YANDEX_POPUP_CONTENT = (
        By.CSS_SELECTOR,
        "ul[class*=mini-suggest__popup-content]"
    )
    LOCATOR_YANDEX_PAGE_PATH = (
        By.CSS_SELECTOR,
        "div[class*=Path]"
    )


class ImagesLocators:
    """ Locators on the Yandex images page. """
    LOCATOR_YANDEX_SEARCH_FIELD_IMAGE_NAME = (
        By.XPATH,
        "/html/body/header/div/div[1]/div[2]/form/div[4]/ul/li[1]"
    )
    LOCATOR_YANDEX_MENU_BUTTON = (
        By.CSS_SELECTOR,
        "a[class*=services-suggest__item-more]"
    )
    LOCATOR_YANDEX_IMAGE_BUTTON = (
        By.CSS_SELECTOR,
        "a[aria-label*='Картинки']"
    )
    LOCATOR_YANDEX_NEXT_BUTTON = (
        By.CSS_SELECTOR,
        "div[class*=CircleButton_type_next]"
    )
    LOCATOR_YANDEX_PREVIOUS_BUTTON = (
        By.CSS_SELECTOR,
        "div[class*=CircleButton_type_prev]"
    )
    LOCATOR_YANDEX_FIRST_CATEGORY = (
        By.CSS_SELECTOR,
        "a[class*=PopularRequestList-Preview]"
    )
    LOCATOR_YANDEX_NAVIGATION_BAR = (
        By.CSS_SELECTOR,
        "a[class*=services-suggest__item-more]"
    )
    LOCATOR_YANDEX_FIRST_IMAGE = (
        By.CSS_SELECTOR,
        "div[class*=serp-item_pos_0]"
    )


class SitesUrls:
    """ URLs of required pages. """
    TENSOR_URL = 'tensor.ru'
    SEARCH_URL = 'https://yandex.ru/search/'
    IMAGES_URL = 'https://yandex.ru/images/'
