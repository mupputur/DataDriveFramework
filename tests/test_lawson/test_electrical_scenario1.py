import pytest
from lawson_product.home_page import HomePage
from lawson_product.product_page import Product
from lawson_product.electrical_page import Electrical
from lawson_product.batteries_page import Batteries
from lawson_product.category_page import CategoryPage

@pytest.fixture(scope="module")
def common_driver():
    # Create the common driver instance and perform any setup
    common = HomePage()
    common.driver.implicitly_wait(10)
    yield common.driver
    # Clean up after tests
    common.driver.quit()

def test_navigate_to_product(common_driver):
    product_page = Product(common_driver)
    product_page.navigate_to_product()

def test_navigate_to_electrical(common_driver):
    electrical_page = Electrical(common_driver)
    electrical_page.navigate_to_elecrical()

def test_navigate_to_battery(common_driver):
    battery_page = Batteries(common_driver)
    battery_page.navigate_to_battery()

def test_navigate_to_category(common_driver):
    category_page = CategoryPage(common_driver)
    category_page.navigate_to_category()
