#install the requests lib
#install the bs4
import requests
import csv
from bs4 import BeautifulSoup
url= "https://en.wikipedia.org/wiki/India"
#response from server
r=requests.get(url)
htmlContent=r.content
# parsed the data in html
soup=BeautifulSoup(htmlContent, 'html.parser')
# data scrapping
#for first paragaraph data 
# print(soup.find('p').get_text())

# for all the text data

output=soup.get_text()
import io
file = io.open('india.csv', "w", encoding="utf-8")
file.write(output)
