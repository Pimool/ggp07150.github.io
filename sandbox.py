# import requests
# from bs4 import BeautifulSoup

# webpage = requests.get('http://www.google.com/search?q=JeilPharma&hl=en')
# soup = BeautifulSoup(webpage.content, "html.parser")

# print(soup.h)]

import pandas as pd

df = pd.read_csv('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/clinicaltrials_gov_data.csv', encoding = 'utf=8-sig')

def korea():
    df_korea = df[df['Study_Country'] == 'Korea, Republic of'].reset_index(drop = True)
    df_korea = df_korea.drop(['Unnamed: 0'], axis = 1)
    df_korea.to_csv('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/한국임상data.csv', encoding = 'utf-8-sig', index = False)


def country_frequency():
    df_country = df.groupby('Study_Country').size().reset_index(name = 'Frequency')
    df_country = df_country.sort_values('Frequency', ascending = False)
    df_country.reset_index(drop = True)
    df_country.to_csv('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/나라별data.csv', encoding = 'utf-8-sig', index = False)

def from_20_to_22():
    df_20_22 = df[df['Study_date_first'].str.contains('2020|2021|2022')]
    df_20_22 = df_20_22.drop(['Unnamed: 0'], axis = 1).reset_index(drop = True)
    # print(df_20_22.columns)
    df_sponsor = df_20_22.drop_duplicates(['Sponsor'])[['Sponsor', 'Study_Country']].reset_index(drop = True)
    df_usau = df_sponsor[df_sponsor['Study_Country'].isin(['United States', 'Australia'])].reset_index(drop = True)
    df_usau.index += 1
    #임상시험을 한국에서 한 sponsor 체크
    df_korea_20_22 = df_20_22[df_20_22['Study_Country'] == 'Korea, Republic of']
    df_korea_20_22 = df_korea_20_22.drop_duplicates(['Sponsor'])[['Sponsor']].reset_index(drop = True)    
    df_korea_20_22.index += 1 

    writer = pd.ExcelWriter('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/2020-2022.xlsx', engine = 'openpyxl')
    df_20_22.to_excel(writer, sheet_name = '총data', index = False)
    df_sponsor.to_excel(writer, sheet_name = 'Sponsor목록', index = False)
    df_korea_20_22.to_excel(writer, sheet_name = '한국임상sponsor목록')
    df_usau.to_excel(writer, sheet_name = 'US,Australia임상')
    df_usau.to_excel(writer, sheet_name = 'test')
    writer.save()

def test():
    df_tmp = pd.read_excel('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/2020-2022.xlsx', sheet_name = 'test')
    df_test = df_tmp[:0]
    sponsor_list_20_22 = []
    for index in range(len(df_tmp)):
        if str(df_tmp.loc[index][1]) != 'nan':
            sponsor_list_20_22.append(df_tmp.loc[index][1])
            df_test = df_test.append(df_tmp.loc[index])
    df_test = df_test[['Sponsor', 'Study_Country']].reset_index(drop = True)
    df_test.index += 1 
    df_test.to_csv('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/test.csv', encoding = 'utf-8-sig')


def quarter():

    year_quarter = {
        'Jan' : '1Q',
        'Feb' : '1Q',
        'Mar' : '1Q',
        'Apr' : '2Q',
        'May' : '2Q',
        'Jun' : '2Q',
        'Jul' : '3Q',
        'Aug' : '3Q',
        'Sep' : '3Q',
        'Oct' : '4Q',
        'Nov' : '4Q',
        'Dec' : '4Q'
    }
    df_quarter_US = pd.DataFrame({'1Q' : [0]*24, '2Q' : [0]*24, '3Q' : [0]*24, '4Q' : [0]*24}, index = range(1999, 2023))
    df_quarter_AU = pd.DataFrame({'1Q' : [0]*24, '2Q' : [0]*24, '3Q' : [0]*24, '4Q' : [0]*24}, index = range(1999, 2023))
    
    df_all = pd.read_csv('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/clinicaltrials_gov_data.csv', encoding = 'utf-8-sig')
    df_quarter_US_tmp = df_all[df_all['Study_Country'] == 'United States'] 
    df_quarter_AU_tmp = df_all[df_all['Study_Country'] == 'Australia']
    for row_US in range(len(df_quarter_US_tmp)):
        day_US = df_quarter_US_tmp.iloc[row_US]['Study_date_first']
        df_quarter_US.loc[int(day_US[-4:])][year_quarter[day_US[:3]]] += 1
    for row_AU in range(len(df_quarter_AU_tmp)):
        day_AU = df_quarter_AU_tmp.iloc[row_AU]['Study_date_first']
        df_quarter_AU.loc[int(day_AU[-4:])][year_quarter[day_AU[:3]]] += 1

    writer = pd.ExcelWriter('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/분기별 임상수_US_AU.xlsx', engine = 'openpyxl')
    df_quarter_US.to_excel(writer, sheet_name = 'United States')
    df_quarter_AU.to_excel(writer, sheet_name = 'Australia')
    writer.save()

def test_2():
    df_korea_tmp = pd.read_csv('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/test.csv', encoding = 'utf-8-sig')
    korean_sponsor_list = []
    for i in range(len(df_korea_tmp)):
        korean_sponsor_list.append(df_korea_tmp.loc[i][1])
    df_korea_ct = pd.read_excel('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/2020-2022.xlsx', sheet_name = '총data')
    df_korea_ct = df_korea_ct[df_korea_ct['Sponsor'].isin(korean_sponsor_list)].reset_index(drop = True)
    df_korea_ct = df_korea_ct[df_korea_ct['Study_Country'].isin(['United States', 'Australia'])].reset_index(drop = True)
    with pd.ExcelWriter('C:/Users/CRS-P-135/Desktop/Clinicaltrials_gov/2020-2022.xlsx', mode = 'a', engine = 'openpyxl') as writer:
        df_korea_ct.to_excel(writer, sheet_name = '한국bio')

# df_20_22.to_csv('C:/Users/CRS-P-135/Desktop/2020-2022.csv', encoding = 'utf-8-sig', index = False)
if __name__ == "__main__":
    quarter()