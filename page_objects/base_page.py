from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _clear(self, locator: tuple, time: int = 5):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).clear()

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_clickable(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.element_to_be_clickable(locator))

    def _wait_until_element_is_not_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.invisibility_of_element(locator))

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    @ property
    def current_url(self) -> str:
        return self._driver.current_url

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def _is_not_displayed(self, locator: tuple) -> bool:
        return self._find(locator).is_not_displayed()

    def _open_url(self, url: str):
        self._driver.get(url)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text
