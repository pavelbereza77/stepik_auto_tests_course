import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = " http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)

    button_primary = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    button_primary.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = math.log(abs(12 * math.sin(int(x))))
    input_el = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_el.send_keys(str(y))

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
