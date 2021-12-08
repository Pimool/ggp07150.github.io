import pandas as pd
import numpy as np
import tkinter
import zipfile
import matplotlib.pyplot as plt
import time
from konlpy.tag import Okt, Mecab
import os
from sklearn.feature_extraction.text import CountVectorizer



start = time.time()
pd.set_option('display.max_rows', 500)

db_spec = pd.read_csv("C:/Users/CRS-P-135/Desktop/Study/Study_01/Study_01_DB Specification_V2.2.csv", encoding = 'CP949')
SDTM = pd.read_csv("C:/Users/CRS-P-135/Desktop/SDTM.csv")   #엑셀로 열면 깨짐 -> csv파일을 손봐야함. 모든 specification은 xlsx형식인가? 그리고 결측치는 어떻게 할 것인지?
os.mkdir("C:/Users/CRS-P-135/Desktop/Study/Study_01/Conversion_files")
mapping_rule_data = []


# print(SDTM.loc[:,'Variable Name'])

dictionary = []
suffix_dic = []

for x in SDTM.loc[:, "Variable Name"]:
    dictionary.append(x)
    if x[0]+x[1] == "__":
        suffix_dic.append(x)
    
# for i in range(len(dictionary)-1):
#     for j in range(i+1,len(dictionary)):
#         if dictionary[i] == dictionary[j]:
#             print("In ", i, ", " , j, dictionary[i], " are same")
#             break
#             break
        
# 중복 존재 -> 같은 item id이더라도 다른 의미를 가질 수 있다.
# 따라서, item id로 먼저 찾고 dictionary에 여러 개가 있다면 description 중 유사도가 제일 높은 것 사용(어짜피 itemid는 같지만 이후 다른데에 사용될 수 있으니)

            
# print(dictionary)
# print(suffix_dic)

domain_standard = ['EN', 'SV', 'DM', 'MH', 'PE', 'VS', 'EG', 'LB', 'IE', 'RN', 'IP', 'DA', 'EX', 'CM', 'AE', 'DS', 'SN']
Domain = []


for i in range(len(db_spec)):
    if db_spec.iloc[i,1] in domain_standard:
        if (not((db_spec.iloc[i, 0], db_spec.iloc[i, 1]) in Domain)):
            Domain.append((db_spec.iloc[i, 0], db_spec.iloc[i, 1]))
#Domain에 넣음
# print(Domain)

#밑에 좀 비효율적인 알고리즘 같은데
for (x, y) in Domain:
    path = "C:/Users/CRS-P-135/Desktop/Study/Study_01/DataSetCsv_20210722092440/"+ x + ".csv"
    df = pd.read_csv(path)
    data_labels = []
    for s in df.columns:
        data_labels.append(s)
    # print(data_labels)
    

    conversion_result = df.copy()     #변환 후 new_csv라는 이름으로 저장할 것   
    # print(new_csv)

    for s in data_labels:
        ss = s
        if s in dictionary:
            # print(s," is in dictionary")
            pass

        elif s[0]+s[1]==x or s[0]+s[1]==y:
            if ("__"+s[2:]) in dictionary:
                pass
                # print(s, s[2:],"is in dictionary")
            else:
                # print(s, "is not in domain dictionary")    #여기도 NLP 필요함
                '''
                #s[4:]도 확인? 아니면 dictionary에 있는 것을 s에 있는지 확인?
                후자로 할거면 s[2:]부터 찾으면 될듯 (s[0]+s[1]==x or s[0]+s[1]==y)==True 인 상황이니
                그러면 시간복잡도가 커져서 계산시간이 너무 오래걸림
                '''
                
                for id in dictionary:
                    if id in s[2:]:
                        pass
                        # print(", but don't need NLP.")
        
        else:
            pass
        mapping_rule_data.append([x, y, s, ss])
            # print(s, "Need NLP")
        
        #conversion_result.rename(columns = {s : "바꿀 이름"}, inplace = True)
    #break   #코드 완성전 하나씩만 돌려보려고
    conversion_result.to_csv("C:/Users/CRS-P-135/Desktop/Study/Study_01/Conversion_files/"+ x + ".csv", encoding = "utf-8-sig", index = False)

mapping_rule = pd.DataFrame(mapping_rule_data, columns = ["DOMAIN", "PGNM", "Before", "After"])
mapping_rule.to_csv("C:/Users/CRS-P-135/Desktop/Study/Study_01/Mapping_rule.csv", encoding = "utf-8-sig", index = False)

class NLP:
    def __init__(self, object, target):     #hyperparameter?
        self.object = object
        self.target = target
    def similarity(self, object, target):
        '''
        
        일단 코사인 유사도 생각
        추후에 높은 성능으로 바꾸도록 한다.
        '''
        pass




end = time.time()
print("걸린 시간 : ", end-start, "s")
    

# #프레임만 있어도 path받아올 수 있음 굳이 tkinter 안써도 됨.
# #어쩌피 csv 경로만 가져올 것이기 때문.
# window = tkinter.Tk()   #가장 상위 레벨의 윈도우 창 생성
# import tkinter.filedialog as fd

# window.title("EDC To SDTM") #프로그램 창의 이름
# window.geometry("1280x800+100+100")  #프로그램 크기, 위치
# window.resizable(True, True)    #프로그램 창 가로, 세로 조정 해도 되는지


# label = tkinter.Label(window, text = "What do you want to convert?")
# label.pack()    #label.pack을 해야 위젯이 배치됨.

# frame = tkinter.Frame(window)
# frame.pack()

# path1 = fd.askopenfilename(initialdir = '/', title = "파일 탐색기", filetypes = (("Python files", "*.py"), ("csv files", "*.csv"), ("all files", "*.*")))

# print(path1)

# window.mainloop()   #윈도우 창을 윈도우가 종료될 때까지 실행
