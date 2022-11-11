import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from env import TEST_EMAIL, TEST_PASSWORD  # should be in env var in real life

URL = 'https://leader-id.ru/'


@pytest.fixture(scope="session")  # Use scope=session to avoid risk of captcha
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get(URL)
    login_link = browser.find_element(By.CSS_SELECTOR, '[data-qa="loginOpenBtn"]')
    login_link.click()

    login_input = browser.find_element(By.CSS_SELECTOR, 'input[dataqa="loginEmail"]')
    login_input.send_keys(TEST_EMAIL)

    password_input = browser.find_element(By.CSS_SELECTOR, 'input[data-qa="loginPassword"]')
    password_input.send_keys(TEST_PASSWORD)

    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[data-qa="loginSubmitBtn"]')
    submit_button.click()

    yield browser
    browser.quit()
