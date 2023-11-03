from behave import when, then, given
from google_task_methods import search_input, extract_information, click
from common_ui_actions import scroll
import csv

closing_icon = "//*[@class=' NMm5M']"


@given('He Open Google Map')
def opening_google_map(context):
    """ Opening Google Map """
    context.page.goto('https://www.google.com/maps/')
    context.page.set_viewport_size({"width": 1500, "height": 1200})
    context.page.wait_for_load_state(timeout=10000)


@when(u'He Searched "{user_searched_for}"')
def searching_choice(context, user_searched_for):
    """ This Is For Searching And Showing result Based On User Interest
    :param user_searched_for: Hold User Interest wants to search """

    context.search_interest = user_searched_for
    search_input(context.page, user_searched_for)


@then(u'He Extract Information Of First "{number_of_restaurant}" Restaurants')
def extracting_information(context, number_of_restaurant):
    """ This Extract All Information of The Restaurants Like name,rating,review etc . .
    :param number_of_restaurant: Holds Total Number Of Restaurants user want to save for information """

    unique_list = []
    context.details_of_restaurants = []
    index = 0
    while index < int(number_of_restaurant):
        '''This Loop Will Perform Scroll And Click On Element To Get The Information '''
        visible_result_after_search = context.page.locator("//a[@class='hfpxzc']").all()
        if visible_result_after_search[index] not in unique_list:   #To remove duplicates
            visible_result_after_search[index].click()
            det = extract_information(context.page)
            context.details_of_restaurants.append(det)
            click(context.page, closing_icon)
        unique_list.append(visible_result_after_search[index])
        index += 1
        scroll(context.page)


@then(u'He Successfully Make CSV File Of All Information')
def making_csv(context):
    """ Creating CSV File of the Searched_Item Details with the searched item name """

    field_names = ['Name', 'Rating', 'Address', 'Review', 'Long_and_Lat']
    with open(f'{context.search_interest}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(context.details_of_restaurants)
