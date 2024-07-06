from selenium import webdriver
driver= webdriver.Firefox()
driver.get("file:///C:/Users/Mreza/Documents/VS Code/Python/Automation/Exercise Files/CH02/html_code_02.html")
username = driver.find_element("name",'username')
print("My input element is:")
print(username)
driver.close()
