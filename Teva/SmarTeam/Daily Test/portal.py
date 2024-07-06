from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.ie.service import Service
from selenium.webdriver.ie.options import Options

# Path to the Edge WebDriver executable
webdriver_path = "iedriver/IEDriverServer.exe"

# Set up Edge options
ie_options = Options()

# Create a new service object
service = Service(webdriver_path)

# Initialize the Edge WebDriver with the service object and options
driver = webdriver.Ie(service=service, options=ie_options)

# Open the URL (configured to open in IE mode)
url = "http://example.com"
driver.get(url)

# Perform any actions or web scraping tasks
# For example, print the page title
print(driver.title)

# Close the browser
driver.quit()
