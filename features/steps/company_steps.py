from behave import given, when, then
from company_task_methods import search_company, Extracting_Information
import csv



Details = []
#Taking This Variable Global because we need to search different compnay name and have to store in same csv file
@given(u'User is On Google Page')
def opening_google(context):
    """Opening Google For Searching About Company """

    context.page.goto('https://www.google.com/')
    context.page.set_viewport_size({"width": 1500, "height": 1200})
    context.page.wait_for_load_state(timeout=10000)


@when(u'He Searched For Company "{company_name}"')
def searching_company(context, company_name):
    """ :param company_name: Stores Name Of Company User Searched To See Details"""
    search_company(context.page, company_name)


@when(u'He Extract Information')
def extracting_information(context):
    """Extract All Information Like Name of Company, Total Review etc.."""
    Details.append(Extracting_Information(context.page))


@then(u'Successfully Make Csv file of all data')
def making_csv(context):
    """Making Csv File"""

    field_names = ['Company_Name', 'Company_Rating', 'Company_Review', 'Company_Address', 'Company_Contact_Number',
                   'Long_and_Lat']
    with open('company_details.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(Details)
