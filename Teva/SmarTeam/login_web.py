from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge()
driver.get('https://ilstweb-st.teva.corp/WebEditor/Authentication/LoginPage.aspx?ReturnUrl=%2fwebeditor')

username = driver.find_element("id", 'AuthenticatedLogin1_tbUsername')
password = driver.find_element("id", 'AuthenticatedLogin1_tbPassword')

username.send_keys("MREZA")
password.send_keys("Pala@2786" + Keys.ENTER)

time.sleep(10)
driver.close()