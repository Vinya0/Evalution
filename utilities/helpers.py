import time

def refresh_page_and_wait(driver):
    driver.refresh()
    time.sleep(2)