from selenium.webdriver.common.by import By

class MainPageLocators():
    SEARCH_FIELD = (By.CSS_SELECTOR, "#text")
    SUGGEST_TABLE = (By.CSS_SELECTOR, "[role='listbox']")
    RESULTS_TABLE = (By.CSS_SELECTOR, "[role='main']")
    LINKS = (By.CSS_SELECTOR, ".path__item[tabindex='0']")
    IMAGES_LINK = (By.CSS_SELECTOR, "[data-id='images']")

class ImagesPageLocators():
    FIRST_CATEGORY = (By.CSS_SELECTOR, "[data-grid-name='im']:nth-child(1) a")
    TEXT_FIRST_CATEGORY_ON_THE_IMAGES_PAGE = (By.CSS_SELECTOR,
    ".PopularRequestList-Item:nth-child(1) .PopularRequestList-SearchText ")
    TEXT_FIRST_CATEGORY_ON_THE_PAGE_THAT_CONTINUES_AFTER_THE_IMAGES_PAGE = (By.CSS_SELECTOR,
    "[name='text']")
    FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item:nth-child(1) .serp-item__link")
    FIRST_IMAGE_IS_OPENED = (By.CSS_SELECTOR, ".MMImageContainer")
    FORWARD_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next")
    SRC_IMAGE = (By.CSS_SELECTOR, ".MMImage-Preview")
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev")