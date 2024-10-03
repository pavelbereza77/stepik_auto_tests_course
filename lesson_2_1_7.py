import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input_y = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_y.send_keys(y)

    elem_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    elem_checkbox.click()

    elem_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    elem_radio.click()

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    time.sleep(1)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
