import time
from pages.login import LoginPage
from pages.products import Product


def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login()

    time.sleep(3)
    product=Product(driver=driver)

    assert product.is_cart_empty() is True

    product.add_to_cart(product_id="sauce-labs-backpack")

    #product_2=Product(driver=driver)
    product.add_to_cart(product_id="sauce-labs-bike-light")

    #product_3=Product(driver=driver)
    product.add_to_cart(product_id="sauce-labs-bolt-t-shirt")
    time.sleep(3)

    product.remove_from_cart(product_id="sauce-labs-backpack")
    time.sleep(3)

    driver.get("https://www.saucedemo.com/cart.html")
    time.sleep(10)

