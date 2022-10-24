from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome()
    time.sleep(5)
    browser.get(link)

    import math


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)



    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()


    option1 = browser.find_element(By.ID, "robotsRule")
    option1.click()

    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()


finally:
    time.sleep(30)
    browser.quit()
