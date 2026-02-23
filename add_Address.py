from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class LazadaLoginTest(BaseCase):
    def test_login(self):
        self.open("https://pages.lazada.vn/wow/gcp/vn/member/login-signup?redirect=https%3A%2F%2Fmember%2Elazada%2Evn%2Fuser%2Fprofile")
        self.sleep(2)

        # Step 1: Login
        self.type('input[placeholder="Please enter your Phone or Email"]', "qdung312@gmail.com")
        self.type('input[placeholder="Please enter your password"]', "tyfguo01vn^^")
        self.click('button[class*="iweb-button iweb-button-primary"]')
        self.sleep(10)

        # Step 2: Go to address book directly
        self.open("https://member.lazada.vn/address")
        self.sleep(3)

        # Step 3: Click "Add New Address"
        self.click('button[class*="next-btn-warning"]')
        self.sleep(2)

        # Step 4: Fill Name, Phone, Address
        self.type('input[placeholder="First Last"]', "Dung Le")
        self.type('input[placeholder="Please enter your phone number"]', "0364003627")
        self.type('input[placeholder="Please enter your address"]', "Kenh Tan Hoa")

        # Define wait
        wait = WebDriverWait(self.driver, 15)

        # Step 5: Select Province
        province_dropdown = wait.until(EC.element_to_be_clickable(( 
            By.XPATH, "//div[contains(@class,'mod-select-location-tree-1')]//span[contains(@class,'next-select-inner')]"
        )))
        province_dropdown.click()
        self.sleep(1)

        province_option = wait.until(EC.element_to_be_clickable(( 
            By.XPATH, "//li[contains(text(), 'Hồ Chí Minh')]"
        )))
        province_option.click()
        self.sleep(5)  # Wait for district dropdown to become ready

        # Step 6: Select District
        district_dropdown = wait.until(EC.element_to_be_clickable(( 
            By.XPATH, "//div[contains(@class,'mod-select-location-tree-2')]//span[contains(@class,'next-select-inner')]"
        )))
        district_dropdown.click()
        self.sleep(1)

        district_option = wait.until(EC.element_to_be_clickable(( 
            By.XPATH, "//li[contains(text(), 'Quận Tân Phú')]"
        )))
        district_option.click()
        self.sleep(5)  # Wait for ward dropdown to become ready

        # Step 7: Select Ward
        ward_dropdown = wait.until(EC.element_to_be_clickable(( 
            By.XPATH, "//div[contains(@class,'mod-select-location-tree-3')]//span[contains(@class,'next-select-inner')]"
        )))
        ward_dropdown.click()
        self.sleep(1)

        ward_option = wait.until(EC.element_to_be_clickable(( 
            By.XPATH, "//li[contains(text(), 'Phường Hòa Thạnh')]"
        )))
        ward_option.click()
        self.sleep(1)

        # Step 8: Save
        self.click('button[class*="next-btn next-btn-primary next-btn-large mod-address-form-btn"]')
        self.sleep(5)
