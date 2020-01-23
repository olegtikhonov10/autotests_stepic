import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
import time
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_id("input_value")
    x=x_element.text
    y = calc(x)
    button1 = browser.find_element_by_id("answer")
    button1.send_keys(y)
    # Отправляем заполненную форму
    button2 = browser.find_element_by_css_selector(".btn-primary")
    button2.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()