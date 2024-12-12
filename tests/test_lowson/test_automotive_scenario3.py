from apps.modules_lowson.homePage import HomePage
from apps.modules_lowson.productPage import Product
from apps.modules_lowson.automotivePage import AutomotivePage
from apps.modules_lowson.bodyHardware import BodyHardware
from apps.modules_lowson.categoryPage import CategoryPage

def test_scenario3():
    common = HomePage()
    common.driver.implicitly_wait(10)

    # Navigate to Product page
    product_page = Product(common.driver)
    product_page.navigate_to_product()

    automotive_page = AutomotivePage(common.driver)
    automotive_page.navigate_to_automotive()

    # Navigate to body_hardware page
    body_hardware_page = BodyHardware(common.driver)
    body_hardware_page.navigate_to_body_hardware()

    category_page = CategoryPage(common.driver)
    category_page.navigate_to_category()

    common.driver.close()