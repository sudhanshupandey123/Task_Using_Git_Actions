from common_ui_actions import click,  fill_area

search_box = "//input[@id='twotabsearchtextbox']"
add_to_cart_button = "(//div[@id='preAddToCartFramework_feature_div']/preceding-sibling::div[@id='addToCart_feature_div'])[2]/descendant::input[@id='add-to-cart-button']"
filtered_product="//a[@class='a-link-normal s-no-outline']"
cancel_button="//a[@id='attach-close_sideSheet-link']"

def search_product(page, product_name):
    fill_area(page, search_box, product_name)
    page.keyboard.press('Enter')


def filtering_product(page, rating_value):
    click(page, f"//section[@aria-label='{int(rating_value)} Stars & Up']")

def adding_to_cart(page, number_of_product):
    all_selected_product_link=[]
    all_ele=page.locator(filtered_product)
    for i in range(int(number_of_product)):
        link="https://www.amazon.in"+all_ele.nth(i).get_attribute('href')
        all_selected_product_link.append(link)
    for i in all_selected_product_link:
        page.goto(i)
        click(page, add_to_cart_button)
    click(page, cancel_button)

