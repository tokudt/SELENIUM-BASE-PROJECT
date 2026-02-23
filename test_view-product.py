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
        
        #click the first item in the search result 
        self.click('/html/body/div[4]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]')

        #click the second picture of the product
        self.click('/html/body/div[5]/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[2]')
        self.sleep(2)
        #click the third picture of the product
        self.click('/html/body/div[5]/div/div[3]/div[1]/div/div/div[2]/div/div[1]/div/div[3]')
        self.sleep(2)
        self.click("img[alt='NEW RG/HG 1/144 JMS RX-78-2 Gundam Ver.2.0 Self Assemble model mecha Boys toys Gift']")
        self.sleep(2)
        #it will take the screenshot of the product page
        self.save_screenshot("view_product.png")
