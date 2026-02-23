from seleniumbase import BaseCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LazadaLoginTest(BaseCase):
    def test_login(self):
        # Step 1: Open Lazada login page
        self.open("https://pages.lazada.vn/wow/gcp/vn/member/login-signup?redirect=https%3A%2F%2Fmember%2Elazada%2Evn%2Fuser%2Fprofile")
        self.sleep(2)

        # Step 2: Enter credentials
        self.type('input[placeholder="Please enter your Phone or Email"]', "qdung312@gmail.com")
        self.type('input[placeholder="Please enter your password"]', "tyfguo01vn^^")

        # Step 3: Click login
        self.click('button[class*="iweb-button iweb-button-primary index_module_loginButton__3bfb1909"]')
        self.sleep(30)

        # Step 4: Click "Account"
        account_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "myAccountTrigger"))
        )
        ActionChains(self.driver).move_to_element(account_button).click().perform()
        self.sleep(3)

        # Step 5: Click "Logout"
        logout_link = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(normalize-space(.), 'Logout')]"))
        )
        ActionChains(self.driver).move_to_element(logout_link).click().perform()
