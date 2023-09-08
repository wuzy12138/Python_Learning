import requests
from bs4 import BeautifulSoup
import re

url = "https://www.investing.com/equities/"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; \
    Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/84.0.4147.105 Safari/537.36'}


html = requests.get(url, headers=headers)

soup = BeautifulSoup(html.text, "html.parser")
# try:
    # anchor = soup.find_all('a').texts
# except AttributeError:
#     print("cao")
anchors = soup.find_all('a')
finder = re.compile(r'/equities/*')
# finder.findall(anchor)
print(anchor)
for anchor