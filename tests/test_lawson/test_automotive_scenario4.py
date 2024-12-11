from lawson_product.home_page import HomePage
from lawson_product.product_page import Product
from lawson_product.automotive_page import AutomotivePage
from lawson_product.universal_parts_page import UniversalParts
from lawson_product.category_page import CategoryPage
import pytest

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

def test_navigate_to_automotive(common_driver):
    automotive_page = AutomotivePage(common_driver)
    automotive_page.navigate_to_automotive()

    # Navigate to body_hardware page
def test_navigate_to_universal_parts(common_driver):
    universal_parts_page = UniversalParts(common_driver)
    universal_parts_page.navigate_to_universal_parts()

def test_navigate_to_category(common_driver):
    category_page = CategoryPage(common_driver)
    category_page.navigate_to_category()


