from seleniumbase import BaseCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class LazadaLoginTest(BaseCase):
    def test_login(self):
        self.open("https://pages.lazada.vn/wow/gcp/vn/member/login-signup?redirect=https%3A%2F%2Fmember%2Elazada%2Evn%2Fuser%2Fprofile")
        self.sleep(2)

        # Login
        self.type('input[placeholder="Please enter your Phone or Email"]', "qdung312@gmail.com")
        self.type('input[placeholder="Please enter your password"]', "tyfguo01vn^^")
        self.click('button[class*="iweb-button iweb-button-primary"]')
        self.sleep(10)

        wait = WebDriverWait(self.driver, 15)

        # Go to profile
        my_profile_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[@id="My-profile"]/a')))
        my_profile_link.click()
        self.sleep(3)

        # Click "Edit Profile"
        self.click('button[class*="next-btn next-btn-warning next-btn-normal next-btn-large"]')
        self.sleep(5)

        # Set name
        self.type('input[placeholder="First Last"]', "Dung Le")

        # Select Month: December
        month_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.mod-birthday-month')))
        month_dropdown.click()
        self.sleep(1)
        december_li = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//li[contains(@class, "next-menu-item") and text()="December"]')))
        december_li.click()

        # Step 7: Select Day "03" 
        day_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span#day.mod-birthday-day')))
        day_dropdown.click()
        self.sleep(1)

        # Ensure the dropdown options are visible
        day_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//li[contains(@class, "next-menu-item") and text()="03"]')
        ))
        self.driver.execute_script("arguments[0].click();", day_option)

        # Step 7: Select Day "03" 
        year_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span#year.mod-birthday-year')))
        year_dropdown.click()
        self.sleep(1)

        # Ensure the dropdown options are visible
        year_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//li[contains(@class, "next-menu-item") and text()="2004"]')
        ))
        self.driver.execute_script("arguments[0].click();", year_option)
        self.sleep(5)
        
        # Step 8: Set gender
        gender_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span#gender.mod-gender-gender')))
        gender_dropdown.click()
        self.sleep(1)

        # Ensure the dropdown options are visible
        gender_option = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//li[contains(@class, "next-menu-item") and text()="male"]')
        ))
        self.driver.execute_script("arguments[0].click();", gender_option)
        self.sleep(5)
        
        # Step 9: Save it
        self.click('button[class*="next-btn next-btn-primary next-btn-large"]')
        self.sleep(5)
        