from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from conftest import URL


def navigate_to_create_event_page(browser):

    event_link = WebDriverWait(
        browser, 8
    ).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/events"]')))
    time.sleep(6)
    event_link.click()

    create_event_link = WebDriverWait(
        browser, 5
    ).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-qa="eventCreateBtn"]')))
    create_event_link.click()


def set_up_test(browser):
    navigate_to_create_event_page(browser)

    button = browser.find_element(By.CSS_SELECTOR, 'div.GdFFbwBwANJH > button')
    browser.execute_script("arguments[0].scrollIntoView();", button)
    button.click()

