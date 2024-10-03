import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser.get(link)

    button_book = browser.find_element(By.CSS_SELECTOR, '#book')

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))
    button_book.click()

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = math.log(abs(12 * math.sin(int(x))))
    input_el = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_el.send_keys(str(y))
    

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
