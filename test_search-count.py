from seleniumbase import BaseCase

class SearchTest(BaseCase):
    def test_search_valid(self):
        # Open the Lazada homepage
        self.open("https://www.lazada.vn/")
        
        # Wait for the page to load
        search_term = "RG sazabi"  # Or, make this a parameter.
        search_input_selector = 'input[placeholder*="Search in Lazada"]' #  *Contains search
        self.type(search_input_selector, search_term)
        self.click('a[class*="search-box__button--1oH7"]')
        
        self.wait_for_element('div[data-qa-locator="product-item"]', timeout=10)


        # Step 4: Count the number of product results
        products = self.find_elements('div[data-qa-locator="product-item"]')
        count = len(products)

        # Step 5: Output the result
        print(f"Search for '{products}' returned {count} results.")
        self.assert_true(count > 0, f"No products found for '{products}'")

