from selenium.webdriver.common.by import By

class Product:
    def __init__(self,driver):
        self.driver=driver
    def add_to_cart(self,product_id):
        self.driver.find_element(By.ID,f"add-to-cart-{product_id}").click()
    def remove_from_cart(self,product_id):
        self.driver.find_element(By.ID,f"remove-{product_id}").click()

    def is_cart_empty(self):
        element = self.driver.find_elements(By.CLASS_NAME,"shopping_cart_badge")
        if element:
            return False
        return True
        