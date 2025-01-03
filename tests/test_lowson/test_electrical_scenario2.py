from apps.modules_lowson.homePage import HomePage
from apps.modules_lowson.productPage import Product
from apps.modules_lowson.electricalPage import Electrical
from apps.modules_lowson.electricalToolPage import ElectricalTool
from apps.modules_lowson.categoryPage import CategoryPage

def test_scenario2():
    common = HomePage()
    common.driver.implicitly_wait(10)

    # Navigate to Product page
    product_page = Product(common.driver)
    product_page.navigate_to_product()

    electrical_page = Electrical(common.driver)
    electrical_page.navigate_to_elecrical()

    # Navigate to Batteries page and list batteries
    electrical_tool_page = ElectricalTool(common.driver)
    electrical_tool_page.navigate_to_electrical_tool()

    category_page = CategoryPage(common.driver)
    category_page.navigate_to_category()

    # Close the driver
    common.driver.close()
