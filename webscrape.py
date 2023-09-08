from bs4 import BeautifulSoup

from urllib.request import urlopen

import webbrowser

import mechanicalsoup

import requests


url = "https://dteenergy.com/"
target_url = "https://www.google.com/search?q=scrape+allow+file&rlz=1C1GCEU_en-gbUS1044US1044&oq=scrap&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgYIARBFGDkyDQgCEC4YgwEYsQMYgAQyDQgDEC4YgwEYsQMYgAQyCggEEAAYsQMYgAQyDQgFEAAYgwEYsQMYgAQyBwgGEAAYgAQyDQgHEC4YrwEYxwEYgAQyCggIEAAYyQMYgAQyCggJEAAYkgMYgATSAQ8xMTM0NjgzNDI2ajBqMTWoAgCwAgA&sourceid=chrome&ie=UTF-8/robots.txt"
# # proxies = {'http':'http://172.31.1.57','https':'http://172.31.1.57'}

# headers = {"User-Agent":"chrome"}
# resp = requests.get(url, headers=headers)

 

# print(resp.status_code)

 

# webpage = urlopen(url)

# webbrowser.open(url)

# html = webpage.read().decode("utf-8")

# soup = BeautifulSoup(html, "html.parser")

 

# print(soup.get_text())

 

 

browser = mechanicalsoup.StatefulBrowser()

browser.open(url)