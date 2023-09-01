
# # 한국어 형태소 분석기를 생성
# okt = Okt()

# # 형태소 분석 함수를 정의


# def tokenizer(text):
#     return okt.morphs(text)


# # 한국어 불용어 리스트를 정의
# stop_words = [...]  # 여기에 불용어를 리스트 형태로 입력

# # TF-IDF 벡터라이저를 생성
# vectorizer = TfidfVectorizer(tokenizer=tokenizer, stop_words=stop_words)

# # 리뷰 데이터에 대해 TF-IDF 벡터라이저를 적용
# tfidf_matrix = vectorizer.fit_transform(reviews)

# # 각 키워드와 그에 대한 tf-idf 점수를 가져옴
# keywords = vectorizer.get_feature_names_out()
# scores = tfidf_matrix.toarray().sum(axis=0)

# # # 향수의 어코드에 대한 키워드 리스트를 정의
# # accord_keywords = ["시트러스", "시트러스향"]  # 여기에 어코드 키워드를 리스트 형태로 입력

# # # 키워드와 점수를 함께 출력
# # for keyword, score in zip(keywords, scores):
# #     if keyword in accord_keywords:
# #         print(f"{keyword}: {score}")

# # 키워드와 점수를 함께 출력
# for keyword, score in zip(keywords, scores):
#     print(f"{keyword}: {score}")

# # # LDA 모델을 생성
# # lda_model = LatentDirichletAllocation(
# #     n_components=10, random_state=0)  # n_components는 추출할 토픽의 수를 설정

# # # 리뷰 데이터에 대해 LDA 모델을 적용
# # lda_top = lda_model.fit_transform(tfidf_matrix)

# # # 각 토픽과 그에 대한 키워드를 출력
# # for idx, topic in enumerate(lda_model.components_):
# #     print(f"Topic #{idx+1}:")
# #     print([(vectorizer.get_feature_names_out()[i], topic[i])
# #           for i in topic.argsort()[:-10 - 1:-1]])# 각 토픽의 상위 10개 키워드를 출력
