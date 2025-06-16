import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from utilities.csv_reader import read_csv
import os

# Element locators
def username_field(driver):
    return driver.find_element(By.ID, "user-name")

def password_field(driver):
    return driver.find_element(By.ID, "password")

def login_button(driver):
    return driver.find_element(By.ID, "login-button")

def login_error_message(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
    )

# Path to CSV file
CSV_PATH = os.path.join(os.path.dirname(__file__), "../testdata/login_data.csv")

@pytest.mark.parametrize("username,password", read_csv(CSV_PATH))
def test_login_with_multiple_users(username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    username_field(driver).send_keys(username)
    password_field(driver).send_keys(password)
    login_button(driver).click()

    if username == "invalid_user" or username == "locked_out_user":
        assert "Epic sadface" in login_error_message(driver).text
    else:
        WebDriverWait(driver, 5).until(EC.url_contains("inventory"))
        assert "inventory" in driver.current_url

    driver.quit()
