from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Нажать кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    # Окно  сообщения
    confirm = browser.switch_to.alert
    confirm.accept()

    # Ваш код, который заполняет обязательные поля

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)


    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(y))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button")
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