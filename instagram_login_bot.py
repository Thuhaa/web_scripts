from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
PATH = "C://Program Files (x86)//chromedriver.exe"
try:
    driver = webdriver.Chrome(PATH)
    driver.get('https://www.instagram.com/')
    time.sleep(20)
    username_input = driver.find_element_by_name("username")
    username_input.send_keys("your_username")
    username_input.send_keys(Keys.RETURN)
    password_input = driver.find_element_by_name("password")
    password_input.send_keys("your_password")
    password_input.send_keys(Keys.RETURN)
    not_now = driver.find_element_by_class_name('yWX7d')
    time.sleep(5)
    not_now.send_keys(Keys.RETURN)
    time.sleep(5)
    not_now1 = driver.find_element_by_class_name('HoLwm')
    not_now1.send_keys(Keys.RETURN)
except NoSuchElementException:
    print("No such element")