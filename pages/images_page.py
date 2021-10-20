from .base_page import BasePage
from .locators import ImagesPageLocators

class ImagesPage(BasePage):
    def should_be_the_correct_url(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        print(f"Current url is {self.browser.current_url}")
        assert 'https://yandex.ru/images/' in self.browser.current_url, "This is not the correct url address"

    def go_to_the_first_category(self):
        self.text_first_category = self.browser.find_element(
        *ImagesPageLocators.TEXT_FIRST_CATEGORY_ON_THE_IMAGES_PAGE).text
        print(self.text_first_category)
        self.browser.find_element(*ImagesPageLocators.FIRST_CATEGORY).click()
        print(f'Current url is {self.browser.current_url}')

    def check_the_first_category_is_opened(self):
        assert self.is_element_present(
        *ImagesPageLocators.TEXT_FIRST_CATEGORY_ON_THE_PAGE_THAT_CONTINUES_AFTER_THE_IMAGES_PAGE), \
            "The first category is not opened"

    def check_names_of_the_first_category_are_equal(self):
        text = self.browser.find_element(
        *ImagesPageLocators.TEXT_FIRST_CATEGORY_ON_THE_PAGE_THAT_CONTINUES_AFTER_THE_IMAGES_PAGE)
        print(text.get_attribute("value"))
        assert text.get_attribute("value") == self.text_first_category, \
            "Names of the first category are not equal"

    def go_to_the_first_image(self):
        self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE).click()
        print(f'Current url is {self.browser.current_url}')

    def check_the_first_image_is_opened(self):
        assert self.is_element_present(*ImagesPageLocators.FIRST_IMAGE_IS_OPENED), \
            "First image is not opened"

    def check_the_first_image_is_changed_after_clicking_the_forward_button(self):
        self.src_first_image = self.browser.find_element(*ImagesPageLocators.SRC_IMAGE).get_attribute('src')
        print(f"src of the first image "
              f"{self.src_first_image}")
        self.browser.find_element(*ImagesPageLocators.FORWARD_BUTTON).click()
        src_second_image = self.browser.find_element(*ImagesPageLocators.SRC_IMAGE).get_attribute('src')
        print(f"src of the second image "
              f"{src_second_image}")
        assert src_second_image != self.src_first_image, \
            "The first image is not changed after clicking the forward button"

    def check_the_second_image_is_changed_to_the_first_image_after_clicking_the_previous_button(self):
        self.browser.find_element(*ImagesPageLocators.PREVIOUS_BUTTON).click()
        print(f"src of the first image "
              f"{self.browser.find_element(*ImagesPageLocators.SRC_IMAGE).get_attribute('src')}")
        assert self.src_first_image == self.browser.find_element(
            *ImagesPageLocators.SRC_IMAGE).get_attribute('src'), \
            "The second image is not changed to the first image after clicking the previous button"

