from generator.generator import generator_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TestBoxPages(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generator_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.elements_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.elements_is_visible(self.locators.EMAIL).send_keys(email)
        self.elements_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.elements_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.elements_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self) -> str:
        full_name = self.elements_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.elements_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.elements_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.elements_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address
