from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):
    def should_be_the_search_field(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_FIELD), "There is no the search field"

    def should_be_the_suggest_table_after_some_input(self):
        self.browser.find_element(*MainPageLocators.SEARCH_FIELD).send_keys("Тензор")
        assert self.is_element_present(*MainPageLocators.SUGGEST_TABLE), \
            "There is no suggest table after some input in the search field"

    def should_be_the_results_table_after_pressing_enter_key(self):
        self.browser.find_element(*MainPageLocators.SEARCH_FIELD).send_keys(Keys.ENTER)
        assert self.is_element_present(*MainPageLocators.RESULTS_TABLE), \
            "There is no results table after pressing enter key"

    def check_presence_the_link_in_the_first_five_results(self):
        links = self.browser.find_elements(*MainPageLocators.LINKS)
        links = [link.get_attribute("href") for link in links]
        print(f"All links are {links}")
        assert "https://tensor.ru/" in links[:5], "There is no link to tensor.ru in the first five results"

    def should_be_link_to_images(self):
        assert self.is_element_present(*MainPageLocators.IMAGES_LINK), "There is no link to images"

    def go_to_images_page(self):
        self.browser.find_element(*MainPageLocators.IMAGES_LINK).click()


