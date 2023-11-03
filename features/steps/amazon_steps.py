from behave import when, then, given
from amazon_task_methods import search_product, adding_to_cart, filtering_product
from common_ui_actions import click, get_text_value

cart_subtotal = "//*[@id='sc-subtotal-amount-buybox']/child::span"
cart_button = "//span[@id='nav-cart-count']"
summarized_total = "//*[@id='sc-subtotal-amount-activecart']/child::span"


@given('User Is On Amazon Page')
def opening_amazon_page(context):
    """Opening Amazon Page """

    context.page.goto('https://www.amazon.in/')
    context.page.wait_for_load_state(timeout=10000)
    context.page.set_viewport_size({"width": 1500, "height": 1200})


@when(u'User Search For "{item_name}"')
def searching_for_product(context, item_name):
    """This Is For Searching Product Based On User Input
    :param item_name: Contain Value Of User Want to search"""
    search_product(context.page, item_name)


@when(u'Filtered Product Based On "{rating_value_for_filter}" star rating')
def filtering_product_based_on_rating(context, rating_value_for_filter):
    """This Is For Filtering Product Based On User Given Rating Value
    :param rating_value_for_filter: Contains User Interest Rating Value"""

    filtering_product(context.page, int(rating_value_for_filter))


@then(u'He Added "{number_of_product}" Product To Cart')
def adding_product_to_cart(context, number_of_product):
    """This Is Used For adding product to cart based on number of product user want to add
    :param number_of_product: Contains Value Of Product User Want To add"""

    adding_to_cart(context.page, number_of_product)


@then(u'Actual Price Should Be Same As Cart Price')
def verifying_summarized_price_and_subtotal(context):
    """This Is For Verification Whether The Summarized Price Is Equal To Sub-Total or Not"""

    click(context.page, cart_button)
    if get_text_value(context.page, cart_subtotal) != get_text_value(context.page, summarized_total):
        raise Exception('Add To Cart Not Working Properly')
