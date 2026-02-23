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
        
        self.type('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[5]/div[2]/div/input[1]', "100000")#enter minimum price
        self.type('//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[5]/div[2]/div/input[2]', "1000000")#enter maximum price
        
        self.sleep(10)#wait for the page to load