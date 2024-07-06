from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.google.com')
time.sleep(2)

driver.close()