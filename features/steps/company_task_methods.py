import time
from common_ui_actions import click, fill_area, get_text_value
import re

search_box = "//*[@id='APjFqb']"
company_name = "//div[@class='SPZz6b']//h2"
company_rating = "//*[@class='Aq14fc']"
company_review = "//span[@class='hqzQac']//a//span"
company_address = "//span[@class='LrzXr']"
company_phone_number = "//span[@class='LrzXr zdqRlf kno-fv']//a//span"
direction_button = "//a[@class='ab_button' and @tabindex='0']//div"


def search_company(page, company_name):
    """This Will Take User Value And Search """
    fill_area(page, search_box, company_name)
    page.keyboard.press('Enter')


def Extracting_Information(page):
    """This Method Will Extract All Information User Need To Save In A Dictionary And Return That """
    information = {}
    try:
        information['Company_Name'] = get_text_value(page, company_name)
    except:
        information['Company_Name'] = page.title.split('-')[0]

    try:
        information['Company_Rating'] = get_text_value(page, company_rating)
    except:
        information['Company_Rating'] = None
    try:
        information['Company_Review'] = get_text_value(page, company_review).split()[0]
    except:
        information['Company_Review'] = None
    try:
        information['Company_Address'] = get_text_value(page, company_address)
    except:
        information['Company_Address'] = None
    try:
        information['Company_Contact_Number'] = get_text_value(page, company_phone_number)
    except:
        information['Company_Contact_Number'] = None
    try:
        click(page, direction_button)
        page.reload()
        url = page.url
        lan = re.search('@\d+\S{1}\d+,\d+\S{1}\d+', url).group()
        information['Long_and_Lat'] = lan.replace('@', '')
    except:
        information['Long_and_Lat'] = None
    return information
