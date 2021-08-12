from libs.config_web import config, browser
from web.pageobject.home_page import HomePage
from web.pageobject.search_result import SearchResult

def test_success_search_product(browser):
    # variable
    productname = 'Pacar'

    # Given home page is displayed
    HomePage(browser).load()

    # When user search product
    HomePage(browser).search_product(productname)

    # Then showing title result of products
    assert 'Hasil pencarian' in browser.page_source
    assert SearchResult(browser).page_result_title() in browser.page_source

    # And search input value result is Pacar
    assert productname == SearchResult(browser).search_input_value()

    # And showing the product
    title = SearchResult(browser).product_result()
    match = [product_name for product_name in title if productname in product_name]
    assert len(match) > 0

    # And showing web title of search
    title_array = SearchResult(browser).web_title_result().split(' ')
    assert productname in title_array

def test_not_found_search_product(browser):
    # variable
    productname = 'Kdsfl'

    # Given home page is displayed
    HomePage(browser).load()

    # When user search product
    HomePage(browser).search_product(productname)

    # Then showing title result of products
    assert 'Hasil pencarian' in browser.page_source
    assert SearchResult(browser).page_result_title() in browser.page_source

    # And search input value result is Kdsfl
    assert productname == SearchResult(browser).search_input_value()

    # And product not found
    assert 'Maaf, barangnya tidak ketemu' in browser.page_source

    # And showing web title of search
    title_array = SearchResult(browser).web_title_result().split(' ')
    assert productname in title_array

def test_no_result_without_input_product(browser):
    # variable
    productname = ''

    # Given home page is displayed
    HomePage(browser).load()

    # When user search product
    HomePage(browser).search_product(productname)

    # Then not showing title result of products
    assert not 'Hasil pencarian' in browser.page_source
