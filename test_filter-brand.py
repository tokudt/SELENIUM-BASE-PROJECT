from seleniumbase import BaseCase

class SearchTest(BaseCase):
    def test_search_valid(self):
        # Open the Lazada homepage
        self.open("https://www.lazada.vn/")
        self.sleep(3)
        
        # Wait for the page to load
        search_term = "RG"
        search_input_selector = 'input[placeholder*="Search in Lazada"]' #  *Contains search
        self.type(search_input_selector, search_term)
        self.click('a[class*="search-box__button--1oH7"]')
        self.sleep(3)
        
        self.click('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/a[1]/label/span[1]')
        self.sleep(5)
        #click on the first brand when the product pop up
     
        