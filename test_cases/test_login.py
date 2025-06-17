import os
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from constant import validation_assert
from constant import input_field
import os
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SCREENSHOT_DIR = os.path.join(PROJECT_ROOT, "../screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# Ensure log directory exists
os.makedirs("logs", exist_ok=True)

# Logging setup
logger = logging.getLogger("saucedemo_logger")
logger.setLevel(logging.INFO)

# Clear old handlers to ensure logs work every time
if logger.hasHandlers():
    logger.handlers.clear()

handler = logging.FileHandler("logs/saucedemo.log", mode='a')  # use 'w' to overwrite
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

#FUNCTION
def email_input_field(driver):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user-name")))

def password_input_field(driver):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))

def login_button(driver):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))

def username_required(driver):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Username is required')]"))
    )

def password_required(driver):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Password is required')]"))
    )

def both_required(driver):  # Actually shows "Username is required"
    return username_required(driver)  # Since username is checked first


def add_to_cart_button(driver):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))

def add_to_cart_button_light(driver):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-bike-light']")))

def shopping_cart(driver):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='shopping_cart_badge']")))

def remove_product(driver):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='remove-sauce-labs-backpack']")))


def checkout(driver):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='checkout']")))

def firstname(driver):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first-name")))

def lastname(driver):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "last-name")))

def zipcode(driver):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "postal-code")))

def continue_button(driver):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='continue']")))

def first_name_required(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[text()='Error: First Name is required']"))
    )

def last_name_required(driver):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[normalize-space()='Error: Last Name is required']")))

def postal_code_required(driver):
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(), 'Postal Code is required')]")))


def finish_button(driver):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='finish']")))


# Global driver
driver = None

# def test_login_validation():
#     global driver
#     logger.info("Launching Chrome browser")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     wait = WebDriverWait(driver, 10)
#
#     logger.info("Navigating to saucedemo.com")
#     driver.get("https://www.saucedemo.com/")
#     driver.maximize_window()
#
#     # All blank
#     email_input_field(driver).clear()
#     password_input_field(driver).clear()
#     login_button(driver).click()
#     assert both_required(driver).text == "Epic sadface: Username is required"
#     path = os.path.join(SCREENSHOT_DIR, "usernmame.png")
#     driver.save_screenshot(path)
#     print(f"Screenshot saved: {path}")
#     time.sleep(3)
#
#     # Empty username
#     email_input_field(driver).clear()
#     password_input_field(driver).clear()
#     password_input_field(driver).send_keys(input_field.PASSWORD)
#     login_button(driver).click()
#     assert username_required(driver).text == "Epic sadface: Username is required"
#     path = os.path.join(SCREENSHOT_DIR, "usernamee.png")
#     driver.save_screenshot(path)
#     print(f"Screenshot saved: {path}")
#     time.sleep(3)
#
#     # Empty password
#     email_input_field(driver).clear()
#     email_input_field(driver).send_keys(input_field.USERNAME)
#     password_input_field(driver).clear()
#     login_button(driver).click()
#     assert password_required(driver).text == "Epic sadface: Password is required"
#     path = os.path.join(SCREENSHOT_DIR, "password.png")
#     driver.save_screenshot(path)
#     print(f"Screenshot saved: {path}")
#     time.sleep(3)

def test_login_success():
    global driver  # Use global to make it accessible in other functions
    logger.info("Launching Chrome browser")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    logger.info("Navigating to saucedemo.com")
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    logger.info("Entering login credentials")
    email_input_field(driver).clear()
    email_input_field(driver).send_keys(input_field.USERNAME)
    password_input_field(driver).clear()
    password_input_field(driver).send_keys(input_field.PASSWORD)
    login_button(driver).click()

    logger.info("Login test passed ")

def test_add_to_cart():
    global driver
    logger.info("Clicking add to cart")
    add_to_cart_button(driver).click()
    logger.info("Add to cart test passed ")
    add_to_cart_button_light(driver).click()
    logger.info("Add to cart test passed ")
    logger.info("Removing product")

def test_remove():
    global driver
    logger.info("Removing product")
    shopping_cart(driver).click()
    remove_product(driver).click()
    logger.info("Removed the product")


def test_checkout():
    global driver
    logger.info("Clicking Checkout button")
    checkout(driver).click()

    # Optional assertion
    assert "checkout-step-one" in driver.current_url
    logger.info("Checkout page opened successfully")

def test_validation_information():
    global driver
    logger.info("All blank fields")
    continue_button(driver).click()
    assert first_name_required(driver).text == validation_assert.FIRST_NAME_REQUIRED
    path = os.path.join(SCREENSHOT_DIR, "first_name_required.png")
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")
    time.sleep(3)

    logger.info("Last name empty")
    firstname(driver).clear()
    firstname(driver).send_keys(input_field.FIRST_NAME)
    lastname(driver).clear()
    zipcode(driver).clear()
    zipcode(driver).send_keys(input_field.ZIP_CODE)
    continue_button(driver).click()
    assert last_name_required(driver).text == validation_assert.LAST_NAME_REQUIRED
    path = os.path.join(SCREENSHOT_DIR, "last_name_required.png")
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")
    time.sleep(3)

    # logger.info("Zip code empty")
    #
    # firstname(driver).clear()
    # firstname(driver).send_keys(input_field.FIRST_NAME)
    #
    # lastname(driver).clear()
    # lastname(driver).send_keys(input_field.LAST_NAME)
    #
    # zipcode(driver).clear()
    # continue_button(driver).click()
    #
    # assert postal_code_required(driver).text == validation_assert.POSTAL_REQUIRED
    #
    # # Save screenshot
    # path = os.path.join(SCREENSHOT_DIR, "postal_code_required.png")
    # driver.save_screenshot(path)
    # print(f"Screenshot saved: {path}")
    # time.sleep(2)


def test_success_information():
    logger.info("Filling information")
    firstname(driver).clear()
    firstname(driver).send_keys(input_field.FIRST_NAME)
    lastname(driver).clear()
    lastname(driver).send_keys(input_field.LAST_NAME)
    zipcode(driver).clear()
    zipcode(driver).send_keys(input_field.ZIP_CODE)
    continue_button(driver).click()
    assert "checkout-step-two" in driver.current_url
    finish_button(driver).click()
    time.sleep(2)
    menu_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "react-burger-menu-btn"))
    )
    menu_button.click()
    logger.info("Menu opened")

    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()
    logger.info("Logout clicked")

    # Verify redirection
    assert "saucedemo.com" in driver.current_url and "login" in driver.page_source.lower()
    logger.info("Logout redirect test passed")
    driver.quit()












