string = ('휴일 인 오늘 도 서쪽 을 중심 으로 폭염 이 이어졌는데요, 내일 은 반가운 비 소식 이 있습니다.','폭염 을 피해서 휴일 에 놀러왔다가 갑작스런 비 로 인해 망연자실 하고 있습니다.')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

###단어 벡터화###
#객체 생성
tfidf_vectorizer = TfidfVectorizer()

#대상 벡터화 진행
tfidf_matrix = tfidf_vectorizer.fit_transform(string)

#각 단어
text = tfidf_vectorizer.get_feature_names()

#각 단어의 벡터 값
idf = tfidf_vectorizer.idf_

###코사인 유사도 값###
print(cosine_similarity(tfidf_matrix[0:1],tfidf_matrix[1:2]))

##출처 url : https://soyoung-new-challenge.tistory.com/34