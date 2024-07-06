from selenium import webdriver

driver= webdriver.Chrome()

driver.implicitly_wait(10)

driver.get('http://www.python.org')
myDynamicElement = driver.find_element("id", 'start-shell')

driver.close()
