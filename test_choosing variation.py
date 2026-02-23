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
        self.sleep(3)
        #click the second item in the search result 
        self.click('/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
        self.sleep(3)
        
        #this function only works for the product that has variations
        #click the fouth variation of the product
        self.click('/html/body/div[5]/div/div[3]/div[2]/div/div[1]/div[14]/div/div/div/div/div[2]/span[4]')
        self.sleep(2)
        #click the second variation of the product
        self.click('/html/body/div[5]/div/div[3]/div[2]/div/div[1]/div[14]/div/div/div/div/div[2]/span[2]')
        self.save_screenshot("product-variation.png")
        