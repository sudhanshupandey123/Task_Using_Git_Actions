import re
from common_ui_actions import click, get_text_value, fill_area

search_box = "//input[@id='searchboxinput']"
search_button = "//button[@id='searchbox-searchbutton']"
restaurant_name = "//h1[@class='DUwDvf lfPIob']"
restaurant_rating = "//span[@class='ceNzKf']/preceding-sibling::span"
restaurant_address = "(//div[@class='rogA2c ']/child::div)[1]"
restaurant_review = "(//div[@class='F7nice ']/child::span)[2]"


def search_input(page, name_want_to_search):
    """ Takes argument as locator and text value for search and perform searching operation
    :param name_want_to_search: holds user interest for search in string format """

    fill_area(page, search_box, name_want_to_search)
    click(page, search_button)


def extract_information(page):
    """
    This Function Takes Various Locator As Arguments and store information in a dictionary
    :return: a dict which stores all  information
    """

    information = {}
    try:
        information['Name'] = get_text_value(page, restaurant_name)
    except:
        information['Name'] = None
    try:
        information['Rating'] = get_text_value(page, restaurant_rating)
    except:
        information['Rating'] = None
    try:
        information['Address'] = get_text_value(page, restaurant_address)
    except:
        information['Address'] = None
    try:
        information['Review'] = get_text_value(page, restaurant_review)
    except:
        information['Review'] = None
    try:
        url = page.url
        filtering_lat_and_long = re.search('@\d+\S{1}\d+,\d+\S{1}\d+', url)
        information['Long_and_Lat'] = filtering_lat_and_long.group()
        information['Long_and_Lat'] = information['Long_and_Lat'].replace('@', '')
    except:
        information['Long_and_Lat'] = None

    return information
