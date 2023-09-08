import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

class MainPage:
    def __init__(self, headers, indexURL):
        self.headers = headers

        self.indexURL = indexURL

    def extractAppendix(self):
        html = requests.get(self.indexURL, headers=self.headers)
        soup = BeautifulSoup(html.text, "html.parser")
        tags = soup.find('table',{"id":"cross_rate_markets_stocks_1"}).find("tbody")\
        .find_all("td",{"class":"bold left noWrap elp plusIconTd"})
        # finder = re.compile( )
        names = []
        for tag in tags:
            anchor = tag.a
            appendix = re.findall(r'<a .*?href=(.*?) title.*?>.*?</a>', anchor.decode())
            names.append(appendix[0])

        return names

    