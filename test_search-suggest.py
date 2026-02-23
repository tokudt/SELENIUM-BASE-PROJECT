from seleniumbase import BaseCase

class SearchTest(BaseCase):
    def test_search_valid(self):
        # Open the Lazada homepage
        self.open("https://www.lazada.vn/")
        
        # Wait for the page to load
        self.sleep(2)
        self.type('input[placeholder*="Search in Lazada"]', "RG") # type "RG" in the search bar
        self.wait_for_element('div.suggest-list--3Tm8', timeout=5) # wait for the suggestion list to appear
        self.click('div.suggest-list--3Tm8 a.suggest-common--2KmE:nth-child(1)') #click the first suggestion
        self.sleep(5)
        # wait for the search results to load
    