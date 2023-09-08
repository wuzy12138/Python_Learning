import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

class OtherPages:
    def __init__(self, ref, appendices, headers):
        self.ref = ref
        self.headers = headers
        self.appendices = appendices

    def scraping(self):
        for appendix in self.appendices:
            url = self.ref + eval(appendix)
            print(url)
            page = requests.get(url, headers=self.headers)
            try:
                soup = BeautifulSoup(page.text, 'html.parser')
                # block = soup.find('div',{'class':"md:flex-1 mb-3.5 relative"}).text
                company = soup.find('h1', {'class':"text-xl text-left font-bold leading-7 md:text-3xl md:leading-8 mb-2.5 md:mb-2 text-[#232526] rtl:soft-ltr"}\
                                    ).text
                
                price = soup.find('div', {"class":"text-5xl font-bold leading-9 md:text-[42px] md:leading-[60px] text-[#232526]"}\
                                ).text
                change = soup.find('div', {"class":"text-base font-bold leading-6 md:text-xl md:leading-7 rtl:force-ltr"}\
                                ).text + "%"
                volume = soup.find('div', {"class":"font-bold tracking-[0.2px]"}).text
                x = [company, price, change, volume]
                # print(x)
                all.append(x)

            except AttributeError:
                print("shit")
                break

        return all