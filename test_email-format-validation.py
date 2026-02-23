from seleniumbase import BaseCase

class LazadaLoginTest(BaseCase):

    def test_open_signup(self):
         # Go directly to the Lazada login page 
        self.open("https://pages.lazada.vn/wow/gcp/vn/member/login-signup?redirect=https%3A%2F%2Fmember%2Elazada%2Evn%2Fuser%2Fprofile&globalRegionID=VN&globalLanguage=en&globalOgUrl=https%3A%2F%2Fpages.lazada.vn%2Fwow%2Fi%2Fvn%2Fact%2Fhome&globalOgImage=%2F%2Flaz-img-cdn.alicdn.com%2Ftfs%2FTB1PApewFT7gK0jSZFpXXaTkpXa-200-200.png&globalOgDescription=Widest+Range+of+Mobile+%26amp%3B+Tablets%2C+Home+Appliances%2C+Tv%2C+Audio%2C+Home+%26amp%3B+Living+At+Lazada+%7C+Best+Prices+%3F+Fast+DELIVERY+%7C+Cash+on+Delivery+%3F+Effortless+Shopping+%3F+Best+Customer+Care%21&globalFaviconUrl=%2F%2Flaz-img-cdn.alicdn.com%2Ftfs%2FTB1ODo.f2b2gK0jSZK9XXaEgFXa-64-64.png&globalCanonicalUrl=https%3A%2F%2Fwww.lazada.vn%2F&globalHeadFragmentUrl=%2Fi%2Fvn%2Fnew_gcp_header%3FneedFooter%3Dfalse%26wh_env%3Dproduct%26wh_language%3Den%26wh_site%3Dvn%26wh_channel%3Dmember%26wh_version%3D2&globalFooterFragmentUrl=%2Fi%2Fvn%2Fnew_gcp_footer%3FneedFooter%3Dfalse%26wh_env%3Dproduct%26wh_language%3Den%26wh_site%3Dvn%26wh_channel%3Dmember%26wh_version%3D2&keyOfHtmlTitleTextInMcms=lazada.buyer.portal.keyOfHtmlTitleTextInMcms&forntConfigGlobalDataSpm=a2o42")
        self.sleep(2)
        
        # Choose log in with phone number, because the email is not verified yet 
        self.click('//*[@id="login-container"]/div/div/div/div/div[2]/div[3]')
        self.sleep(2) 
        
        # Enter phone number to recieve the verify code 
        self.type('input[placeholder="Please enter your phone number"]', "0907289404")
        self.sleep(2)
        self.click('/html/body/div[2]/div/div/div/div/div/div[3]/button[2]/div[2]') #it will send you the code from the sms
        
        # Type the code by yourself 
        self.sleep(40)
        
        # Go go my profile and add the email
        self.click('#My-profile a')
        self.sleep(2)
        self.click('a[data-spm*="demail_add"]')
        self.sleep(5)
        
        # Veryfile identity 
        self.click('//*[@id="container"]/div/div[2]/ul/li')
        self.sleep(1)
    
        
        # Choose to send the code 
        self.click('button[class*="mod-sendcode-btn"]')
        self.sleep(10) # Type the code and verify
        self.click('//*[@id="container"]/div/div[2]/div/div[4]/button')
        self.sleep(20)
        
        # Veryfy again by confirming through SMS - đứng mẹ chổ này :)
        self.click('//*[@id="container"]/div/div[2]/ul/li')
        self.sleep(20)
        
        # Enter the mail and verification code
        self.type('input[placeholder="Please enter your email"]', "mapditday@gmail.com")
        self.click('button[class*="mod-sendcode-btn"]')
        self.sleep(20)
        self.click('//*[@id="container"]/div/div/div/div/div[4]/button')
        self.sleep(5)
        