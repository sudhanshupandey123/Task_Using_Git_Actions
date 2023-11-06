from common_ui_actions import click, get_text_value, fill_area, scroll

search_box = "//input[@id='twotabsearchtextbox']"
filtered_product_list = "//span[@class='a-size-medium a-color-base a-text-normal']"
add_to_cart_button = "(//input[@aria-labelledby='submit.add-to-cart-announce'])[1]"

def search_product(page, product_name):
    fill_area(page, search_box, product_name)
    page.keyboard.press('Enter')


def filtering_product(page, rating_value):
    click(page, f"//section[@aria-label='{int(rating_value)} Stars & Up']")

def adding_to_cart(page, number_of_product):
    all_product_box = page.locator(filtered_product_list)
    added_to_cart = 1

    for index in range(0, all_product_box.count()):
        if added_to_cart > int(number_of_product):
            break

        '''This Is Method For Handling Multiple Tab'''
        with page.expect_popup() as popup_info:
            all_product_box.nth(index).click()

        page1 = popup_info.value
        scroll(page)
        click(page1, add_to_cart_button)
        page1.close()
        page.bring_to_front()
        added_to_cart += 1
