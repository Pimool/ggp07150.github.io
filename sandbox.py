import Tokenizer as Tok
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

'''
size = 워드 벡터의 특징 값. 즉, 임베딩 된 벡터의 차원
window = context 윈도우 크기
min_count = 단어 최소 빈도 수 제한
workers = 학습을 위한 프로세스 수
sg 0 -> CBOW, 1 -> Skip-gram
'''

contents = Tok.tokenize(Tok.description_csv_to_list("C:/Users/CRS-P-135/Desktop/Study/Study_01/Study_01_DB Specification_V2.2.csv"))

# print(contents)

model = Word2Vec(sentences = contents, vector_size = 100, window = 5, min_count = 5, workers = 10, sg = 0)


print(model.wv.most_similar(["고혈압"]))
# model_result = model.wv.most_similar("방문")
# print(model_result)

# model.wv.save_word2vec_format("EDC_Description")

