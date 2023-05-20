#stocks 

import requests
url = "https://www.google.com/finance/quote/%s:NASDAQ"
company = input("Enter the companies ticker symbol: ")
mod_url = url%(company)
data = requests.get(mod_url)
from bs4 import BeautifulSoup
soup = BeautifulSoup(data.text,"html.parser")
a=soup.find("div",{"class":"YMlKec fxKbKc"})
print(a.string)
