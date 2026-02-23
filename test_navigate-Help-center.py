from seleniumbase import BaseCase

class SearchTest(BaseCase):
    def test_help_center(self):
        
        # Open the Lazada homepage
        self.open("https://www.lazada.vn/")
        self.sleep(3)
        
        # click on the customer care
        self.click('/html/body/div[2]/div/div/div/div[1]/div/div[5]/span')
        self.sleep(2)
        
        # click on the help center
        self.click('/html/body/div[2]/div/div/div/div[1]/div/div[5]/div/div/ul/li[1]/a')
        self.sleep(5)
        
        # view the help center page
        self.scroll_to('/html/body/div[2]/div/div/div[2]/div/div[3]/div[1]')
        self.sleep(5)        
        self.scroll_to('//*[@id="root"]/div/div/div[3]/div[1]/div/div[1]/span')
        self.sleep(5)