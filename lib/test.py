from selenium import webdriver
import os
import pickle
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# # 네이버 로그인 정보를 환경 변수에서 가져옴
# naver_id = os.getenv('NAVER_ID')
# naver_pw = os.getenv('NAVER_PW')

# ChromeDriver의 절대 경로를 지정
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# Your Chrome Driver path
chrome_driver = "Users/juny/Downloads/chromedriver-mac-x64/chromedriver"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

driver.get("https://cafe.naver.com/perfumelove/1011149")

driver.switch_to.frame('cafe_main')
time.sleep(1)

# BeautifulSoup 객체를 생성
soup = BeautifulSoup(driver.page_source, 'html.parser')
time.sleep(30)

# # 선택된 div 요소 안의 모든 p 요소의 텍스트를 합침
# text = ' '.join(p.get_text() for p in soup.select('div.article_viewer p'))
# # 텍스트를 출력
# print(text)

# # 웹 드라이버를 종료
# driver.quit()

# # 리뷰 데이터
# reviews = [text]  # 스크래핑한 텍스트를 리뷰 데이터로 사용
# print(reviews)
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

# # LDA 모델을 생성
# lda_model = LatentDirichletAllocation(
#     n_components=10, random_state=0)  # n_components는 추출할 토픽의 수를 설정

# # 리뷰 데이터에 대해 LDA 모델을 적용
# lda_top = lda_model.fit_transform(tfidf_matrix)

# # 각 토픽과 그에 대한 키워드를 출력
# for idx, topic in enumerate(lda_model.components_):
#     print(f"Topic #{idx+1}:")
#     print([(vectorizer.get_feature_names_out()[i], topic[i])
#           for i in topic.argsort()[:-10 - 1:-1]])# 각 토픽의 상위 10개 키워드를 출력
