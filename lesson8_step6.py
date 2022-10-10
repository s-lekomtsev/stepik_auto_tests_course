from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("window.scrollBy(0, 100);", button)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(y))


    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    checkbox1.click()

    checkbox1 = browser.find_element(By.ID, "robotsRule")
    checkbox1.click()




    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()