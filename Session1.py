import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s= Service(r"C:\Users\cva\PycharmProjects\FarhanProject\Driver\chromedriver.exe")

# create webdriver object
driver = webdriver.Chrome(service=s)

# get google.com
current_url = driver.get("https://www.google.com")
driver.maximize_window()

#end text in searchbar
add_text= driver.find_element(By.NAME, 'q')
add_text.send_keys('First Selenium Session')
add_text.send_keys(Keys.RETURN)
print('Search successfully')
driver.close()


