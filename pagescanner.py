print("Hutinni!")
######################### Import-Section ##########################

from urllib.request import urlopen;
from bs4 import BeautifulSoup;

######################## Import-Section ###########################

_url="https://veil-carre.de/wohnungsfinder/"
_page= urlopen(_url).read().decode("utf-8")

scan = BeautifulSoup(_page,"html.parser")

print("url",_url)
scan.get_text()
#print(scan.find_all("td"))

for letter in scan.find_all("td"): print(letter.string)
 #push to array
 #filter/map array for "3H"


