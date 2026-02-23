from seleniumbase import BaseCase

class SearchTest(BaseCase):
    def test_language(self):
        # Open the Lazada homepage
        self.open("https://www.lazada.vn/")
        self.sleep(3)
        
        # click on the change language button
        self.click('/html/body/div[2]/div/div/div/div[1]/div/div[10]/span')
        
        #click on the language you want to change to
        self.click('/html/body/div[2]/div/div/div/div[1]/div/div[10]/div/div/div[1]/span')
        self.sleep(5)