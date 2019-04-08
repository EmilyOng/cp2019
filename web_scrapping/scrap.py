import requests
import urllib.request
import time
from bs4 import BeautifulSoup
url='https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705'
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
soups=soup.find_all('span')
print(soups)
