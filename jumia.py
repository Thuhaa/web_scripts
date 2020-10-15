# Imports
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions

# Grab the path to the chrome_driver
path = "C://Program Files (x86)//chromedriver.exe"
driver = webdriver.Chrome(path)

# Open Chrome and go to the Jumia Website
url = 'https://www.jumia.co.ke/'
driver.get(url)
# Wait to ensure that all the Jumia homepage HTML is loaded
time.sleep(5)
# Grab the search box in the homepage
search_box = driver.find_element_by_id('fi-q')
# Type in the search text and hit enter
search_box.send_keys("Phones")
search_box.send_keys(Keys.RETURN)

try:
    result_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, '-paxs'))
    )
    search_results = result_div.find_elements_by_tag_name('article')
    for result in search_results:
        phones_names = result.find_element_by_class_name('name')
        phones_price = result.find_element_by_class_name('prc')
        print(phones_names.text, ": ", phones_price.text)
except exceptions.StaleElementReferenceException:
    article_div = driver.find_elements_by_tag_name('article')
    for article in article_div:
        info_class = article.find_elements_by_class('info')
        for infs in info_class:
            name = infs.find_element_by_class('name')
            price = infs.find_element_by_class('price')
            print(name.text, "XXXXX", price.text)