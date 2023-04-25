import time
import allure
import os

from pages.base_page import BasePage
from locators.book_store_app_locators import BookStoreAppPageLocators
from generator.generator import generated_person
from dotenv import load_dotenv
load_dotenv()


class LoginPage(BasePage):
    locators = BookStoreAppPageLocators()

    @allure.step("user authorization")
    def login_user(self):
        with allure.step('filing fields'):
            self.element_is_present(self.locators.USER_NAME_FIELD_SELECTOR).send_keys(os.getenv("USER_NAME"))
            name = self.element_is_present(self.locators.USER_NAME_FIELD_SELECTOR)
            user_name = name.get_attribute('value')
            self.element_is_present(self.locators.PASSWORD_FIELD_SELECTOR).send_keys(os.getenv("PASSWORD"))
        with allure.step('press login button'):
            self.element_is_clickable(self.locators.LOGIN_BUTTON_SELECTOR).click()
            profile_user_name = self.element_is_present(self.locators.USER_NAME_SELECTOR).text
        return user_name.lstrip(), profile_user_name.lstrip()

