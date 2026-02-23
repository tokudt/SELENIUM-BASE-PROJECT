from seleniumbase import BaseCase

class LazadaLoginTest(BaseCase):

    def test_change_password(self):
         # Go directly to the Lazada login page 
        self.open("https://pages.lazada.vn/wow/gcp/vn/member/login-signup?redirect=https%3A%2F%2Fmember%2Elazada%2Evn%2Fuser%2Fprofile&globalRegionID=VN&globalLanguage=en&globalOgUrl=https%3A%2F%2Fpages.lazada.vn%2Fwow%2Fi%2Fvn%2Fact%2Fhome&globalOgImage=%2F%2Flaz-img-cdn.alicdn.com%2Ftfs%2FTB1PApewFT7gK0jSZFpXXaTkpXa-200-200.png&globalOgDescription=Widest+Range+of+Mobile+%26amp%3B+Tablets%2C+Home+Appliances%2C+Tv%2C+Audio%2C+Home+%26amp%3B+Living+At+Lazada+%7C+Best+Prices+%3F+Fast+DELIVERY+%7C+Cash+on+Delivery+%3F+Effortless+Shopping+%3F+Best+Customer+Care%21&globalFaviconUrl=%2F%2Flaz-img-cdn.alicdn.com%2Ftfs%2FTB1ODo.f2b2gK0jSZK9XXaEgFXa-64-64.png&globalCanonicalUrl=https%3A%2F%2Fwww.lazada.vn%2F&globalHeadFragmentUrl=%2Fi%2Fvn%2Fnew_gcp_header%3FneedFooter%3Dfalse%26wh_env%3Dproduct%26wh_language%3Den%26wh_site%3Dvn%26wh_channel%3Dmember%26wh_version%3D2&globalFooterFragmentUrl=%2Fi%2Fvn%2Fnew_gcp_footer%3FneedFooter%3Dfalse%26wh_env%3Dproduct%26wh_language%3Den%26wh_site%3Dvn%26wh_channel%3Dmember%26wh_version%3D2&keyOfHtmlTitleTextInMcms=lazada.buyer.portal.keyOfHtmlTitleTextInMcms&forntConfigGlobalDataSpm=a2o42")
        self.sleep(2)
        
        # Choose log in with phone number, because the email is not verified yet 
        self.click('//*[@id="login-container"]/div/div/div/div/div[2]/div[3]')
        self.sleep(2) 
        
       # Enter phone number to recieve the verify code 
        self.type('input[placeholder="Please enter your phone number"]', "0907289404")# it could be have error 
        self.sleep(2)
        self.click('/html/body/div[2]/div/div/div/div/div/div[3]/button[2]/div[2]') #it will send you the code from the sms
        
        # Type the code by yourself 
        self.sleep(60)
        
        # Go go my profile
        self.click('#My-profile a')
        self.sleep(2)
        
        # click the Change password 
        self.click('//*[@id="container"]/div/div[2]/button[1]')
        self.sleep(15)# it could be have verify for bot
        self.click('/html/body/div[2]/div/div[2]/div/div[2]/ul/li[1]')
        self.sleep(20)# for verify code
        
        
        # Send the verified code 
        self.click('//*[@id="container"]/div/div[2]/div/div[4]/button')
        self.sleep(30) # Type the code and verify
        
        self.click('//*[@id="container"]/div/div[2]/ul/li')
        self.sleep(30)
        
        #enter password and confirm password
        self.type('//*[@id="container"]/div/div[2]/div/div[4]/button', "Tokudat1311")
        self.type('/html/body/div[2]/div/div[2]/div/div/div/div/div[1]/div[2]/input', "Tokudat1311")
        
        self.click('/html/body/div[2]/div/div[2]/div/div/div/div/div[2]/div/button')
        self.sleep(5)
        