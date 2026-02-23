from seleniumbase import BaseCase

class SearchTest(BaseCase):
    def test_search_valid(self):
        # Open the Lazada homepage
        self.open("https://www.lazada.vn/")
        self.sleep(3)
        
        # Wait for the page to load
        search_term = "RG gundam"
        search_input_selector = 'input[placeholder*="Search in Lazada"]' #  *Contains search
        self.type(search_input_selector, search_term)
        self.click('a[class*="search-box__button--1oH7"]')
        self.sleep(10)

        self.hover("div.lzd-site-menu-nav-category-label")
        self.hover('//*[@id="Level_1_Category_No1"]/div/span')
        self.sleep(1)
        self.click('//*[@id="topActionHeader"]/div[2]/div/div/div[2]/div/ul/ul[1]/li[1]/a/span')
        self.sleep(5)

