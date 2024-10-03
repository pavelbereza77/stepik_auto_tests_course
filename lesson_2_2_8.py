import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    browser.find_element(By.NAME, 'firstname').send_keys('Test_First_Name')
    browser.find_element(By.NAME, 'lastname').send_keys('Test_Last_Name')
    browser.find_element(By.NAME, 'email').send_keys('test@email')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    path_file = os.path.join(current_dir, 'test_file.txt')

    input_file= browser.find_element(By.CSS_SELECTOR,'#file')
    input_file.send_keys(path_file)

    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
