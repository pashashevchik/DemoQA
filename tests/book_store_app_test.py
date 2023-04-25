import allure

from pages.book_store_app_page import LoginPage


@allure.suite("Store")
class TestBookStore:
    @allure.feature("Login form")
    class TestLoginForm:

        @allure.title("Check user in a profile")
        def test_login_user(self, driver):
            login_page = LoginPage(driver, 'https://demoqa.com/login')
            login_page.open()
            user_name, profile_name = login_page.login_user()
            assert user_name == profile_name, 'wrong user'
