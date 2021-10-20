from .pages.main_page import MainPage
from .pages.images_page import ImagesPage

link = "https://yandex.ru/"

def test_images_in_yandex(browser):
    page = MainPage(browser=browser, url=link)
    page.open()
    page.should_be_link_to_images()
    page.go_to_images_page()
    page = ImagesPage(browser=browser, url=link)
    page.should_be_the_correct_url()
    page.go_to_the_first_category()
    page.check_the_first_category_is_opened()
    page.check_names_of_the_first_category_are_equal()
    page.go_to_the_first_image()
    page.check_the_first_image_is_opened()
    page.check_the_first_image_is_changed_after_clicking_the_forward_button()
    page.check_the_second_image_is_changed_to_the_first_image_after_clicking_the_previous_button()