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
        
        self.click('/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')
        #click the first item in the search result 
        #it will take the screenshot of the product page
        self.save_screenshot("screenshot_name.png")
