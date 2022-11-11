import time

from selenium.webdriver.common.by import By

from helpers import navigate_to_create_event_page, set_up_test

TEST_FILE_PATH = "C:/Users/llsaz/Documents/Code/Examples of files to upload/Screenshot.jpg"
TEST_BIG_FILE_PATH = "C:/Users/llsaz/Documents/Code/Examples of files to upload/more than 2 MB.jpg"


def test_event_can_be_deleted(browser):
    navigate_to_create_event_page(browser)

    input_field = browser.find_element(By.CSS_SELECTOR, 'input[data-qa="eventName"]')
    input_field.send_keys("Test event 1")

    button_next = browser.find_element(By.CSS_SELECTOR, '[data-qa="eventNextBtn"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_next)
    button_next.click()

    button_del = browser.find_element(By.CSS_SELECTOR, 'button[data-qa="eventDeleteBtn"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_del)
    button_del.click()

    button_approve = browser.find_element(By.CSS_SELECTOR, f'button.app-button.app-dialog__button.app-button--'
                                                           f'primary.app-button--sm')
    button_approve.click()
    time.sleep(3)

    assert browser.current_url == "https://leader-id.ru/places"


def test_can_upload_file_with_correct_dimension_and_size(browser):
    set_up_test(browser)

    upload_file = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    upload_file.send_keys(TEST_FILE_PATH)

    button_upload = browser.find_element(By.CSS_SELECTOR, 'button.app-button.app-button--primary.app-button--sm')
    button_upload.click()

    uploaded_file = browser.find_element(By.CSS_SELECTOR, f'#__layout > div > div.content > div > div.wrapper > div > '
                                                          f'div._1oOXncqVzqmx._3IJlBydYjn7Z > span > div:nth-child(4) > '
                                                          f'div._1riPLVE9QnT6 > div:nth-child(1) > div:nth-child(3) > '
                                                          f'div > div.GMhwYUFsCOPX._2CCaD8ysRMCG > div:nth-child(1) > '
                                                          f'div > h4')
    assert uploaded_file.text == 'Screenshot.jpg'


def test_cannot_upload_file_of_over_2mb_size(browser):
    set_up_test(browser)

    upload_file = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    upload_file.send_keys(TEST_BIG_FILE_PATH)

    error_msg = browser.find_element(By.CSS_SELECTOR, f'#__layout > div > div.content > div > div.wrapper > div > '
                                                      f'div._1oOXncqVzqmx._3IJlBydYjn7Z > span > div:nth-child(4) > '
                                                      f'div._1riPLVE9QnT6 > div:nth-child(1) > div:nth-child(3) > div > '
                                                      f'div.app-upload-with-crop > div > div > div > '
                                                      f'div.el-dialog__body > div.app-dialog__body > div > '
                                                      f'div:nth-child(2) > div.app-upload-with-crop__actions > '
                                                      f'div.app-upload-with-crop__error')
    assert error_msg.text == 'Файл превышает допустимый размер'
    browser.find_element(By.CSS_SELECTOR, f'#__layout > div > div.content > div > div.wrapper > div > '
                                          f'div._1oOXncqVzqmx._3IJlBydYjn7Z > span > div:nth-child(4) > '
                                          f'div._1riPLVE9QnT6 > div:nth-child(1) > div:nth-child(3) > '
                                          f'div > div.app-upload-with-crop > div > div > div > '
                                          f'div.el-dialog__header > button > i').click()


def test_user_is_requested_to_fill_required_field(browser):
    navigate_to_create_event_page(browser)

    button_next = browser.find_element(By.CSS_SELECTOR, '[data-qa="eventNextBtn"]')
    browser.execute_script("arguments[0].scrollIntoView();", button_next)
    button_next.click()

    error_msg = browser.find_element(By.CSS_SELECTOR, f'#__layout > div > div.content > div > div.wrapper > div > '
                                                      f'div._1oOXncqVzqmx._3IJlBydYjn7Z > span > div:nth-child(1) > '
                                                      f'div._1riPLVE9QnT6 > div:nth-child(1) > div:nth-child(3) > '
                                                      f'span > span')
    browser.execute_script("arguments[0].scrollIntoView();", error_msg)
    assert "Поле «Название» обязательно для заполнения" in error_msg.text

