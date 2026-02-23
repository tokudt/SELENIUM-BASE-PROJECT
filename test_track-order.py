
from seleniumbase import BaseCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        self.sleep(30)  # Wait for page to load

        # Step 4: Click "Account"
        account_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "topActionTrack"))
        )
        ActionChains(self.driver).move_to_element(account_button).click().perform()
        self.sleep(3)

        # Step 5: Input the number into the target field
        input_field = WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="eg.123456789"]'))
        )
        input_field.send_keys("399787607928126")
        
        # Step 6: Click submit button
        self.click('/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div/div[6]/div/div/form/div/button')
        self.sleep(2)