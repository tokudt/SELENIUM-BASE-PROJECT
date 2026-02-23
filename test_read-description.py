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
        
        #it's scrolling down to the product page for loading the product details
        self.scroll_to('/html/body/div[5]/div/div[3]/div[2]/div/div[2]/div[7]/div/div[3]')
        
        #click to expand the description section
        self.click("button.pdp-view-more-btn.pdp-button_type_text.pdp-button_theme_white")
        self.sleep(2)
        
        #scroll down to the description section
        self.scroll_to('/html/body/div[5]/div/div[10]/div[1]/div[1]/div/div/div/div[1]/div[4]')
        self.sleep(5)
        #it will take the screenshot of the product page
        self.save_screenshot("read_description.png")
