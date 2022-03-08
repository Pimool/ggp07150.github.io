import pandas as pd
pd.set_option("display.max_columns", None)
import os

#---------------------------------------------------------------------------------------------------------------------

domain_list = ["EN", "SV", "DM", "MH", "PE", "VS", "EG", "LB", "IE", "RN", "IP", "DA", "EX", "CM", "AE", "DS", "SN"]

for domain in domain_list:
    globals()[domain] = {}

path = "C:/Users/CRS-P-135/Desktop/SDTM/DB spec 전달"

f = open(path + "/db_file_counted.txt", "r+")
file_counted = f.readlines()
if file_counted != []:
    for i in range(len(file_counted)-1):
        file_counted[i] = file_counted[i].replace("\n", "")

db_count = pd.read_csv(path+"/db_count.csv", encoding = "CP949")


file_list = os.listdir(path)
file_list_csv = [file for file in file_list if file.endswith(".csv")]

for i in range(len(file_counted)):
    file_list_csv.remove(file_counted[i])

print("file list_csv : ", format(file_list_csv))

#---------------------------------------------------------------------------------------------------------------------

for row in range(len(db_count)):
  eval(db_count.at[row, "DOMAIN"])[db_count.at[row, "ITEMID"]]=[db_count.at[row, "COUNT"], db_count.at[row, "ITEM_LABEL"]]
#EN = { "ICDTC" : [3, "등록일"]}
#---------------------------------------------------------------------------------------------------------------------

for index in range(len(file_list_csv)):
    db_spec_name = path + "/" + file_list_csv[index]
    db_spec = pd.read_csv(db_spec_name, encoding = "CP949")

    print(file_list_csv[index], "파일입니다")
    print(db_spec.head())

    column_list = db_spec.columns.values.tolist()

    print("column들은 다음과 같습니다.", column_list)
    while True:

        Domain_column = input("Dataframe에서 Domain에 해당하는 Label을 입력해주세요 : ")

        if Domain_column not in column_list:
            print("입력하신 column은 존재하지 않습니다.")
        else:
            while True:
                ITEMID_column = input("Dataframe에서 ITEMID에 해당하는 Label을 입력해주세요 : ")

                if ITEMID_column not in column_list:
                    print("입력하신 column은 존재하지 않습니다.")

                else:
                    while True:
                        Item_Label_column = input("Dataframe에서 Item_Label에 해당하는 Label을 입력해주세요 : ")

                        if Item_Label_column not in column_list:
                            print("입력하신 column은 존재하지 않습니다.")

                        else:
                            break
                    break
            break

    for row in range(len(db_spec)):
        domain_tmp = db_spec.at[row, Domain_column]
        ITEMID_tmp = db_spec.at[row, ITEMID_column]
        Item_Label_tmp = db_spec.at[row, Item_Label_column]

        if domain_tmp not in domain_list:
            pass

        else:
            if ITEMID_tmp not in eval(domain_tmp):
                eval(domain_tmp)[ITEMID_tmp] = [1, Item_Label_tmp]

            else:
                eval(domain_tmp)[ITEMID_tmp][0] += 1


    f.write("\n"+file_list_csv[index])


    # PGNM, TB_NAME, CRF_NM
    # ITEMID, NAME, VARIABLE_ID

#---------------------------------------------------------------------------------------------------------------------
#ITEMID 나오지 않은 것에 대한 행 추가

"""
new_ID = {"DOMAIN" : 1, "ITEMID" : 2, "COUNT" : 3}
db_count = db_count.append(new_ID, ignore_index = True)
"""

#---------------------------------------------------------------------------------------------------------------------

dic_tot = {"DOMAIN" : [], "ITEMID" : [], "COUNT" : [], "ITEM_LABEL" : []}
for domain_dic in domain_list:
    for ITEMID in eval(domain_dic):
        dic_tot["DOMAIN"].append(domain_dic)
        dic_tot["ITEMID"].append(ITEMID)
        dic_tot["COUNT"].append(eval(domain_dic)[ITEMID][0])
        dic_tot["ITEM_LABEL"].append(eval(domain_dic)[ITEMID][1])


df = pd.DataFrame(dic_tot)


for i in range(len(domain_list)):
    print(domain_list[i], ":", eval(domain_list[i]))

f.close()
df.to_csv(path+"/db_count.csv", encoding = "euc-kr", index = False)