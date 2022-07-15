import pandas as pd
import requests
import urllib.request
from urllib import parse
from bs4 import BeautifulSoup
import ssl

def sponsor():
    pd.set_option("mode.chained_assignment", None)      #copy할 때 나오는 경고문 무시
    df = pd.read_csv("C:/Users/CRS-P-135/Desktop/clinicaltrials_gov_data.csv", encoding = "utf-8-sig")

    df_sponsor = df.copy()
    df_sponsor = df_sponsor.drop_duplicates(['Sponsor'])[['Sponsor', 'Study_Country']].reset_index(drop = True)
    df_sponsor.to_csv("C:/Users/CRS-P-135/Desktop/sponsor_list.csv", encoding = 'utf-8-sig')
    print(df_sponsor)

def crawl():
    url = 'https://www.google.com'
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)
    
    else:
        print(response.status_code)

if __name__ == '__main__':
    context = ssl._create_unverified_context()
    sponsor_name = 'Hanmi Pharmaceutical Company Limited'

    for row in range(len(df)):
        sponsor_name = df.iloc([row])
    sponsor_name = df.iloc([1, row])

    url = f'http://www.google.com/search?q={parse.quote(sponsor_name)}&hl=en'

    #쌈바 쌈바 쌈바 쌈바

    d
    print(url)
    html = urllib.request.urlopen(url, context = context).read()
    # print(html)

    