import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"),"100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_id("input_value")
    x=x_element.text
    y = calc(x)
    button1 = browser.find_element_by_id("answer")
    button1.send_keys(y)
    # Отправляем заполненную форму
    button2 = browser.find_element_by_id("solve")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()