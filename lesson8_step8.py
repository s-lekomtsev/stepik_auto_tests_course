from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    chekbox1 = browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
    chekbox1.send_keys("Ivan")

    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
    input2.send_keys("Ivanov")

    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    input3.send_keys("Ivanov@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'f1.txt')  # добавляем к этому пути имя файла


    inputf1 = browser.find_element(By.XPATH, "//input[@type='file']")
    inputf1.send_keys(file_path)




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