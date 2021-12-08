import pandas as pd
from konlpy.tag import Okt, Mecab

okt = Okt()
mecab = Mecab(dicpath = r"C:\mecab\mecab-ko-dic")

stopwords = ["\n"]      #불용어 (i.e. 문장에서 뺄 단어들)

def add_stopwords(word):
    stopwords.append(word)

def description_csv_to_list(path):
    study = pd.read_csv(path, encoding = "CP949")
    term = study["ITEMID"]
    term_description = study["ITEM_LABEL"]

    term_description_Okt = []
    term_description_Mecab = []
    term_description_mix = []       #Okt와 Mecab 합칠 것



    for word in stopwords:
        for list in term_description_Okt:
            if word in list:
                while word in list:
                    list.remove(word)
        for list in term_description_Mecab:
            if word in list:
                while word in list:
                    list.remove(word)

def tokenize(list):
    term_description_Okt = []
    term_description_Mecab = []

    for i in range(len(term_description)):
        term_description_Okt.append(okt.morphs(list[i]))
        term_description_Mecab.append(mecab.morphs(list[i]))


Okt_clone = term_description_Okt[:]
Mecab_clone = term_description_Mecab[:]

for i in range(len(term_description)):
    index = 0
    while (Okt_clone[i] != Mecab_clone[i]):

        if index == min(len(Okt_clone[i])-1, len(Mecab_clone[i])-1):
            if Okt_clone[i][index] == Mecab_clone[i][index]:
                index += 1

            else:
                token_short = (Okt_clone[i], Mecab_clone[i]) [index != len(Okt_clone[i])-1]
                token_long = (Okt_clone[i], Mecab_clone[i]) [token_short == Okt_clone[i]]
                token_long[index] += token_long[index+1]
                del token_long[index+1]

        else:
            if Okt_clone[i][index] == Mecab_clone[i][index]:
                index += 1

            elif Okt_clone[i][index] + Okt_clone[i][index + 1] in Mecab_clone[i][index] + Mecab_clone[i][index + 1]:
                Okt_clone[i][index] += Okt_clone[i][index + 1]
                del Okt_clone[i][index + 1]

            else:
                Mecab_clone[i][index] += Mecab_clone[i][index + 1]
                del Mecab_clone[i][index + 1]


term_description_mix = Okt_clone

for i in range(len(term_description)):
    print(eval("term_description["+str(i)+"]"), eval("term_description_mix["+str(i)+"]"))
