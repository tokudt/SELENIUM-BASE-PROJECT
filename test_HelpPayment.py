from seleniumbase import BaseCase


class LazadaLoginTest(BaseCase):
    def test_login(self):
        # Step 1: Open Lazada login page
        self.open("https://www.lazada.vn/#?")
        self.sleep(1)

        # Step 2: Click "Help Care and use Help Center"
        # click on the customer care
        self.click('/html/body/div[2]/div/div/div/div[1]/div/div[5]/span')
        self.sleep(2)
        
        # click on the help center
        self.click('/html/body/div[2]/div/div/div/div[1]/div/div[5]/div/div/ul/li[1]/a')
        self.sleep(3)

        # Step 3: Click on "Payment"
        self.click("/html/body/div[2]/div/div/div[2]/div/div[3]/div[2]/div/ul/div[6]/li/div[1]/span")
        self.sleep(2)
        
        # Step 4: Click on "Payment Methods"
        self.click('/html/body/div[2]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]')
        self.sleep(2)
        
        # Step 5: Click on the first question
        self.click('/html/body/div[2]/div/div[1]/div[2]/div/div/div[2]/div[2]/div[2]/div/ul/li[1]/div/div')
        self.sleep(5)