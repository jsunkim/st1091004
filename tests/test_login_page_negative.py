import time
import pytest

from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message", [("incorrectUser", "Password123", "Your username is invalid!"), ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.is_error_message_displayed(), "Error message should be displayed"
        assert login_page.gt_error_message(
        ) == expected_error_message, "Error message is not displayed"

        """
        # Go to the webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys(password)

        # Click Submit button
        submit_button_locator = driver.find_element(
            By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed"

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == expected_error_message, "Error message is not expected"

    def test_negative_username(self, driver):

        # Go to the webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorretUser")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Click Submit button
        submit_button_locator = driver.find_element(
            By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed"

        # Verify error message text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"

    def test_negative_password(self, driver):

        # Go to the webpage
        driver.get(
            "https://practicetestautomation.com/practice-test-login/")

        # Type username "student" into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password "incorrectPassword" into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("incorrectPassword")

        # Click 'submit' button
        submit_button_locator = driver.find_element(
            By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator.is_displayed(), "Error message is not displayed"

        # Verify error message text is 'Your password is invalid'
        error_message = error_message_locator.text
        assert error_message == "Your password is invalid!", "Error message is not expected"
        """