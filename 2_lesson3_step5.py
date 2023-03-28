from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()


    x_element = browser.find_element(By.CSS_SELECTOR, '[id=input_value]')
    x = x_element.text
    print(x)
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '[id=answer]')
    input1.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

