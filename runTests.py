import unittest

from driverUtil.config import Browser
from pageobjects.page import MainPage, SearchResultsPage


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = Browser().getbrowser()
        self.driver.get("https://www.python.org")
        self.main_page = MainPage(self.driver)

    def test_search_in_python_org(self):

        assert self.main_page.is_title_matches(), "python.org title doesn't match."
        self.main_page.search_text_element = "pycon"
        self.main_page.click_go_button()
        search_results_page = SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()


class tubs(unittest.TestCase):

    def setUp(self):
        self.driver = Browser().getbrowser()
        self.driver.get("http://www.python.org")
        self.main_page = MainPage(self.driver)

    def test_tubs(self):
        self.main_page.click_to_all_Tubs()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
