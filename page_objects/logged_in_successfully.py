from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):
    _url = "https://practicetestautomation.com/practice-test-login/"
    __header_locator = (By.TAG_NAME, "h1")
    __logout_button_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def expected_url(self) -> str:
        return self._url

    @property
    def header(self) -> str:
        return super()._get_text(self.__header_locator)

    def is_logout_button_displayed(self) -> bool:
        return super().is_displayed(self.__logout_button_locator)
