from selenium.webdriver.common.by import By


class BookStoreAppPageLocators:

    # Login in Book Store
    NEW_USER_BUTTON_SELECTOR = (By.XPATH, "//button[@id='newUser']")
    LOGIN_BUTTON_SELECTOR = (By.XPATH, "//button[@id='login']")

    # Register to Book Store
    FIRST_NAME_FIELD_SELECTOR = (By.XPATH, "//input[@id='firstname']")
    LAST_NAME_FIELD_SELECTOR = (By.XPATH, "//input[@id='lastname']")
    USER_NAME_FIELD_SELECTOR = (By.XPATH, "//input[@id='userName']")
    PASSWORD_FIELD_SELECTOR = (By.XPATH, "//input[@id='password']")
    REGISTER_BUTTON_SELECTOR = (By.XPATH, "//button[@id='register']")
    RECAPTCHA_CHECKBOX_SELECTOR = (By.XPATH, "//div[@id='rc-anchor-container']")
    BACK_TO_LOGIN_BUTTON_SELECTOR = (By.XPATH, "//button[@id='gotologin']")
    RECAPTCHA_FRAME_SELECTOR = (By.XPATH, "//iframe[@title='reCAPTCHA']")

    # Book store Profile
    USER_NAME_SELECTOR = (By.XPATH, "//label[@id='userName-value']")
