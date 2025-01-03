from apps.modules_lowson.homePage import HomePage
from apps.modules_lowson.productPage import Product
from apps.modules_lowson.automotivePage import AutomotivePage
from apps.modules_lowson.universalParts import UniversalParts
from apps.modules_lowson.categoryPage import CategoryPage

def test_scenario4():
    common = HomePage()
    common.driver.implicitly_wait(10)

    product_page = Product(common.driver)
    product_page.navigate_to_product()

    automotive_page = AutomotivePage(common.driver)
    automotive_page.navigate_to_automotive()

    universal_parts_page = UniversalParts(common.driver)
    universal_parts_page.navigate_to_universal_parts()

    category_page = CategoryPage(common.driver)
    category_page.navigate_to_category()

    common.driver.close()