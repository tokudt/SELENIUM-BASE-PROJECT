from seleniumbase import BaseCase

class SearchTest(BaseCase):
    def test_search_valid(self):
        # Open the Lazada homepage
        self.open("https://www.lazada.vn/")
        self.sleep(3)
        
        # Wait for the page to load
        search_term = "RG sazabi"
        search_input_selector = 'input[placeholder*="Search in Lazada"]' #  *Contains search
        self.type(search_input_selector, search_term)
        self.click('a[class*="search-box__button--1oH7"]')
        
        self.hover("div.lzd-site-menu-nav-category-label")
        self.sleep(3)

