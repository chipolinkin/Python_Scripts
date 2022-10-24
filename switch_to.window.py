from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/redirect_accept.html"
try:

    browser = webdriver.Chrome()
    time.sleep(10)
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    browser.switch_to.window(browser.window_handles[1])


    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)


    input1 = browser.find_element(By.NAME, "text")
    input1.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
