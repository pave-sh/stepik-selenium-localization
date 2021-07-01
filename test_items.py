def test_check_add_to_basket_button_exists(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    buttons = browser.find_elements_by_xpath(
        '//form[@id="add_to_basket_form"]/button[@type="submit"][contains(@class, "btn-add-to-basket")]'
    )
    assert buttons, (
        f'Impossible to find submit button to add item to basket with css class "btn-add-to-basket" at page\n{link}'
    )
