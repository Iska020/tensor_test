from .pages.main_page import MainPage

link = "https://yandex.ru/"

def test_search_in_yandex(browser):
    page = MainPage(browser=browser, url=link)
    page.open()
    page.should_be_the_search_field()
    page.should_be_the_suggest_table_after_some_input()
    page.should_be_the_results_table_after_pressing_enter_key()
    page.check_presence_the_link_in_the_first_five_results()