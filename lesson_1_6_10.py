# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/registration2.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
#     first_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block .first_class .first')
#     first_name.send_keys('Test')
#
#     last_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block .second_class .second')
#     last_name.send_keys('Testovich')
#
#     email = browser.find_element(By.CSS_SELECTOR, 'div.first_block .third_class .third')
#     email.send_keys('test@test.ru')
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     time.sleep(1)
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     welcome_text = welcome_text_elt.text
#
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     time.sleep(10)
#     browser.quit()
#
# ###########################################################################################################
#
# link = "http://suninjuly.github.io/registration1.html"
# browser = webdriver.Chrome()
# browser.get(link)
#
# try:
#     first_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block .first_class .first')
#     first_name.send_keys('Test')
#
#     last_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block .second_class .second')
#     last_name.send_keys('Testovich')
#
#     email = browser.find_element(By.CSS_SELECTOR, 'div.first_block .third_class .third')
#     email.send_keys('test@test.ru')
#
#     phone = browser.find_element(By.CSS_SELECTOR, 'div.second_block .first_class .first')
#     phone.send_keys('iPhone')
#
#     address = browser.find_element(By.CSS_SELECTOR, 'div.second_block .second_class .second')
#     address.send_keys('address')
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     time.sleep(1)
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     welcome_text = welcome_text_elt.text
#
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     time.sleep(10)
#     browser.quit()

#######################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #link = "http://suninjuly.github.io/registration1.html"
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]').send_keys("Ivan")
    browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys("Petrov")
    browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys("Ipe@mail.ru")


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

link = "https://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(1)


try:
    first_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block .first_class .first')
    first_name.send_keys('Test')

    last_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block .second_class .second')
    last_name.send_keys('Testovich')

    email = browser.find_element(By.CSS_SELECTOR, 'div.first_block .third_class .third')
    email.send_keys('test@test.ru')

    phone = browser.find_element(By.CSS_SELECTOR, 'div.second_block .first_class .first')
    phone.send_keys('iPhone')

    address = browser.find_element(By.CSS_SELECTOR, 'div.second_block .second_class .second')
    address.send_keys('address')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()