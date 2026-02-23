from seleniumbase import BaseCase

class SearchTest(BaseCase):
    def test_search_valid(self):
        # Open the Lazada homepage
        self.open("https://www.lazada.vn/")
        
        # Wait for the page to load
        self.sleep(2)
        self.type('input[placeholder*="Search in Lazada"]', "nafbcaibcadbc")
        self.click('a[class*="search-box__button--1oH7"]')
        self.sleep(5)
        # wait for the search results to load