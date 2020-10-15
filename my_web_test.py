from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = "C://Program Files (x86)/chromedriver.exe"

driver = webdriver.Chrome(path)
url = "https://josephthuha.herokuapp.com/"
driver.get(url)

name = driver.find_element_by_name("name")
email = driver.find_element_by_name("email")
submit = driver.find_element_
name.send_keys("Robot")
email.send_keys("robot@gmail.com")
submit.send_keys(Keys.RETURN)