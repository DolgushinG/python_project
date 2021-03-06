from element import BasePageElement
from locator import MainPageLocators
from pageobjects.basepage import BasePage


class SearchTextElement(BasePageElement):
    locator = 'q'


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source


class MainPage(BasePage):
    """Здесь находятся методы действий домашней страницы. Например, Python.org"""
    # Объявляет переменную, которая будет содержать полученный текст
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Проверяет, присутствует ли жестко запрограммированный текст «Python» в заголовке страницы."""
        return "Python" in self.driver.title

    def is_title_tabs_matches(self):
        return "About" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_to_all_Tubs(self):
        element = self.driver.find_element(*MainPageLocators.ABOUT)
        element.click()
        element = self.driver.find_element(*MainPageLocators.DOWNLOAD)
        element.click()
        element = self.driver.find_element(*MainPageLocators.DOCUMENTARY)
        element.click()
        element = self.driver.find_element(*MainPageLocators.COMMUNITY)
        element.click()
