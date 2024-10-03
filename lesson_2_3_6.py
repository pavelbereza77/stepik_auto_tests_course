import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser.get(link)

    button_trollface = browser.find_element(By.CSS_SELECTOR, '.trollface')
    button_trollface.click()

    list_window = browser.window_handles
    new_window = browser.switch_to.window(list_window[1])

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
