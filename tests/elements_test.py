from pages.elements_page import TestBoxPages


def test(driver):
    text_box_page = TestBoxPages(driver, 'https://demoqa.com/text-box')
    text_box_page.open()
    input_data = text_box_page.fill_all_fields()
    output_data = text_box_page.check_filled_form()
    assert input_data == output_data
