from seleniumbase import BaseCase


class SearchTest(BaseCase):
    def test_search_valid(self):
        # Open the Lazada homepage
        self.open("https://www.lazada.vn/")
        
        # Wait for the page to load
        search_term = "Mô hình lắp ráp Bandai Gundam RG 1/144 Sazabi"  # Or, make this a parameter.
        search_input_selector = 'input[placeholder*="Search in Lazada"]' #  *Contains search
        self.type(search_input_selector, search_term)
        self.click('a[class*="search-box__button--1oH7"]')  # Click the search button.



        product_title_selector = 'div[class="RfADt"]'
        # Wait for at least one product title to load.  Important!
        self.wait_for_element(product_title_selector, timeout=10) # 10 seconds.

        product_titles = self.find_elements(product_title_selector)  # Returns a list.
        self.assert_true(len(product_titles) > 0, "No product titles found!")
        #Check if the first product title contains the search term.

        first_title_element = product_titles[0]  # Get the *first* element.
        first_title_text = first_title_element.text
        self.assert_true(search_term.lower() in first_title_text.lower(),
                            f"First title '{first_title_text}' does not contain search term '{search_term}'")
        print(f"The first product title '{first_title_text}' contains the search term '{search_term}'.")

        # (Optional) Add a screenshot.
        self.save_screenshot("lazada_first_search_result.png")
