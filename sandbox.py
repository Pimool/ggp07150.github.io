# import requests
# from bs4 import BeautifulSoup

# webpage = requests.get('http://www.google.com/search?q=JeilPharma&hl=en')
# soup = BeautifulSoup(webpage.content, "html.parser")

# print(soup.h)]

import pandas as pd

df = pd.read_csv('C:/Users/CRS-P-135/Desktop/clinicaltrials_gov_data.csv', encoding = 'utf=8-sig')

def korea():
    df_korea = df[df['Study_Country'] == 'Korea, Republic of'].reset_index(drop = True)
    df_korea = df_korea.drop(['Unnamed: 0'], axis = 1)
    df_korea.to_csv('C:/Users/CRS-P-135/Desktop/한국임상data.csv', encoding = 'utf-8-sig', index = False)


def country_frequency():
    df_country = df.groupby('Study_Country').size().reset_index(name = 'Frequency')
    df_country = df_country.sort_values('Frequency', ascending = False)
    df_country.reset_index(drop = True)
    df_country.to_csv('C:/Users/CRS-P-135/Desktop/나라별data.csv', encoding = 'utf-8-sig', index = False)

def from_20_to_22():
    df_20_22 = df[df['Study_date_first'].str.contains('2020|2021|2022')]
    df_20_22 = df_20_22.drop(['Unnamed: 0'], axis = 1).reset_index(drop = True)
    # print(df_20_22.columns)
    df_sponsor = df_20_22.drop_duplicates(['Sponsor'])[['Sponsor', 'Study_Country']].reset_index(drop = True)
    df_us = df_sponsor[df_sponsor['Study_Country'].isin(['United States', 'Australia']) 'United States'].reset_index(drop = True)
    
    
    df_us.index += 1

    writer = pd.ExcelWriter('C:/Users/CRS-P-135/Desktop/2020-2022.xlsx', engine = 'openpyxl')
    df_20_22.to_excel(writer, sheet_name = '총data', index = False)
    df_sponsor.to_excel(writer, sheet_name = 'Sponsor목록', index = False)
    df_us.to_excel(writer, sheet_name = 'US,임상')
    df_us.to_excel(writer, sheet_name = '')
    writer.save()

# df_20_22.to_csv('C:/Users/CRS-P-135/Desktop/2020-2022.csv', encoding = 'utf-8-sig', index = False)
if __name__ == "__main__":
    from_20_to_22()