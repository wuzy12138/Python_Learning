######################################################################
# reference:
# company 
# <h1 class="text-xl text-left font-bold leading-7 md:text-3xl md:leading-8 mb-2.5 md:mb-2 text-[#232526] rtl:soft-ltr">Goldman Sachs Group Inc (GS)</h1>
# price 
# <div class="text-5xl font-bold leading-9 md:text-[42px] md:leading-[60px] text-[#232526]">320.60</div>
# percentage
# <div class="text-base font-bold leading-6 md:text-xl md:leading-7 rtl:force-ltr">(-0.76%)</div>
# volume
# <div class="font-bold tracking-[0.2px]">896,518</div>
# 
# url example: 
# urls = ["https://www.investing.com/equities/goldman-sachs-group"]
#######################################################################
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def extractAppendix(indexURL, headers):
    html = requests.get(indexURL, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    tags = soup.find('table',{"id":"cross_rate_markets_stocks_1"}).find("tbody")\
    .find_all("td",{"class":"bold left noWrap elp plusIconTd"})

    names = []
    for tag in tags:
        anchor = tag.a
        appendix = re.findall(r'<a .*?href=(.*?) title.*?>.*?</a>', anchor.decode())
        names.append(appendix[0])

    return names

def scraping(ref, appendices, headers):
    results = []
    for appendix in appendices:
        url = ref + eval(appendix)
        print(url)
        page = requests.get(url, headers=headers)
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
            results.append(x)

        except AttributeError:
            print("shit")
            break

    return results

def main():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; \
        Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/84.0.4147.105 Safari/537.36'}
    index_url = "https://www.investing.com/equities/"

    appendices = extractAppendix(index_url, headers)

    ref = "https://www.investing.com"
    results = scraping(ref, appendices, headers)


    column_names = ["company", "price", "change", "volume"]
    df = pd.DataFrame(columns=column_names)
    for item in results:
        idx = 0
        df.loc[idx] = item
        df.index += 1

    df = df.reset_index(drop = True)
    df.to_excel('stocks.xlsx')


    print(results)

if __name__ == "__main__":
    main()