import requests
from bs4 import BeautifulSoup
response = requests.get('http://www.wisdompetmed.com/')
headers = response.headers
content = response.content
#print(headers)
#print(content)
soup = BeautifulSoup(response.text)
print(soup.prettify)