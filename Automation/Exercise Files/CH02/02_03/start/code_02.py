from selenium import webdriver
driver= webdriver.Firefox()
driver.get("file:///C:/Users/Mreza/Documents/VS Code/Python/Automation/Exercise Files/CH02/html_code_02.html")
login_form = driver.find_element_by_id('loginForm')
print("My login form element is:")
print(login_form)
driver.close()
