from seleniumbase import BaseCase

class LazadaLoginTest(BaseCase):
    def test_login(self):
        # Go directly to the Lazada login page 
        self.open("https://pages.lazada.vn/wow/gcp/vn/member/login-signup?redirect=https%3A%2F%2Fmember%2Elazada%2Evn%2Fuser%2Fprofile&globalRegionID=VN&globalLanguage=en&globalOgUrl=https%3A%2F%2Fpages.lazada.vn%2Fwow%2Fi%2Fvn%2Fact%2Fhome&globalOgImage=%2F%2Flaz-img-cdn.alicdn.com%2Ftfs%2FTB1PApewFT7gK0jSZFpXXaTkpXa-200-200.png&globalOgDescription=Widest+Range+of+Mobile+%26amp%3B+Tablets%2C+Home+Appliances%2C+Tv%2C+Audio%2C+Home+%26amp%3B+Living+At+Lazada+%7C+Best+Prices+%3F+Fast+DELIVERY+%7C+Cash+on+Delivery+%3F+Effortless+Shopping+%3F+Best+Customer+Care%21&globalFaviconUrl=%2F%2Flaz-img-cdn.alicdn.com%2Ftfs%2FTB1ODo.f2b2gK0jSZK9XXaEgFXa-64-64.png&globalCanonicalUrl=https%3A%2F%2Fwww.lazada.vn%2F&globalHeadFragmentUrl=%2Fi%2Fvn%2Fnew_gcp_header%3FneedFooter%3Dfalse%26wh_env%3Dproduct%26wh_language%3Den%26wh_site%3Dvn%26wh_channel%3Dmember%26wh_version%3D2&globalFooterFragmentUrl=%2Fi%2Fvn%2Fnew_gcp_footer%3FneedFooter%3Dfalse%26wh_env%3Dproduct%26wh_language%3Den%26wh_site%3Dvn%26wh_channel%3Dmember%26wh_version%3D2&keyOfHtmlTitleTextInMcms=lazada.buyer.portal.keyOfHtmlTitleTextInMcms&forntConfigGlobalDataSpm=a2o42")
        self.sleep(2)  # Give time for the page to load

        # Input test email and password
        self.type('input[placeholder="Please enter your Phone or Email"]', "")
        self.type('input[placeholder="Please enter your password"]', "")

        # Click the login button
        self.click('button[class*="iweb-button iweb-button-primary index_module_loginButton__b6443e61 index_module_loginButton__b6443e61"]')

        # Wait for login result (you may need to adjust this)
        self.sleep(20)

    