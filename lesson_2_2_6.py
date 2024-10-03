import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = math.log(abs(12 * math.sin(int(x))))
    input_el = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_el.send_keys(str(y))

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    check = browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio.click()

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
