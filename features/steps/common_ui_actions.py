def click(page, locator):
    page.locator(locator).click()


def get_text_value(page, locator):
    return page.locator(locator).text_content()


def get_title(page):
    return page.title


def get_url(page):
    return page.url


def scroll(page):
    page.keyboard.press('End')


def fill_area(page, locator, value):
    page.locator(locator).fill(value)
