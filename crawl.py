import requests

from bs4 import BeautifulSoup
import urllib.request

url="http://www.busan.go.kr/bhareasymbol"
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,"html.parser")
symbols=soup.find_all(['h4'])

for symbols in symbols:
    print(symbols.get_text())
    
print()