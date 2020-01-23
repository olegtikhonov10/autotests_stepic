from selenium import webdriver
import os, time
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input0 = browser.find_element_by_name("firstname")
    input0.send_keys("Oleg")
    input1 = browser.find_element_by_name("lastname")
    input1.send_keys("Oleg")
    input2 = browser.find_element_by_name("email")
    input2.send_keys("test@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла 
    doc = browser.find_element_by_name("file")
    doc.send_keys(file_path)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()