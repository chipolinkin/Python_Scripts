from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/file_input.html"
try:

    browser = webdriver.Chrome()
    time.sleep(10)
    browser.get(link)


    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("s")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("c")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("p")

    browser.execute_script("window.scrollBy(0, 150);")



    element = browser.find_element(By.ID, "file")
    element.send_keys("/Users/chipolinkin/PycharmProjects/pythonProject/file.txt")


    button = browser.find_element(By.TAG_NAME, "button")
    button.click()



finally:
    time.sleep(30)
    browser.quit()
