import re
from gensim.models import Word2Vec
import gensim
import torch
from transformers import BertTokenizer, BertModel
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.keys import Keys
import pickle
import time
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from selenium.webdriver.chrome.options import Options

# ChromeDriver의 절대 경로를 지정
options = Options()  # 셀레니움 웹드라이버 크롬 브라우저 옵션 설정
# add 실험실 옵션. 크롬 브라우저 디버거 주소를 9222로 설정 -> 크롬 브라우저에서 디버깅하게 하는듯
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Your Chrome Driver path
chrome_driver = "/Users/juny/Downloads/chromedriver-mac-x64/chromedriver"

# 웹 드라이버를 실행
driver = webdriver.Chrome(service=Service(chrome_driver), options=options)

# 네이버 카페 URL
driver.get("https://cafe.naver.com/perfumelove/1011149")

# 네이버 카페의 경우, 본문이 iframe 안에 있으므로 해당 프레임으로 전환
driver.switch_to.frame('cafe_main')
time.sleep(1)

# BeautifulSoup 객체를 생성
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 'div' 요소 내에서 'p' 태그(HTML 문단 태그)가 포함된 모든 텍스트를 결합합니다.
text = ' '.join(p.get_text() for p in soup.select('div.se-main-container p'))

# 웹 드라이버를 종료
driver.quit()

reviews = [text]  # 스크래핑한 텍스트를 리뷰 데이터로 사용
# -- 리뷰 가져오기 완료 --

# 한국어 형태소 분석기를 생성
okt = Okt()

# 한국어 불용어 리스트를 정의
stop_words = [...]  # 여기에 불용어를 리스트 형태로 입력


# 한국어 형태소 분석기를 생성
okt = Okt()

# 한국어 불용어 리스트를 정의
stop_words = [...]  # 여기에 불용어를 리스트 형태로 입력


def preprocess_review(review):
    # 특수 문자 제거
    review_text = re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]", "", review)

    # 형태소 분석을 통한 토큰화
    word_review = okt.morphs(review_text, stem=True)

    # 불용어 제거
    word_review = [token for token in word_review if not token in stop_words]

    return word_review


# 리뷰 데이터를 전처리하고 토큰화
reviews = [preprocess_review(review) for review in reviews]

print(reviews)
# Word2Vec 모델을 생성하고 훈련
word2vec_model = Word2Vec(
    sentences=reviews, vector_size=100, window=5, min_count=5, workers=4, sg=0)  # sentences = 데이터, vector_size = 임베딩 차원, window = 윈도우 크기, min_count = 최소 단어 개수, workers = 프로세스 개수, sg = 0은 CBOW, 1은 Skip-gram

# TF-IDF 벡터라이저를 생성
vectorizer = TfidfVectorizer()

# 리뷰 데이터에 대해 TF-IDF 벡터라이저를 적용
tfidf_matrix = vectorizer.fit_transform(
    [' '.join(review) for review in reviews])

# BERT 토크나이저를 로드
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')

# 리뷰 데이터를 BERT 토크나이저로 토큰화
inputs = tokenizer([' '.join(review) for review in reviews],
                   truncation=True, padding=True, max_length=512, return_tensors="pt")

# BERT 모델을 로드
model = BertModel.from_pretrained('bert-base-multilingual-cased')

# 토큰화된 리뷰 데이터를 BERT 모델로 임베딩
outputs = model(**inputs)

# TF-IDF 벡터라이저를 통해 얻은 피처 이름을 가져옵니다.
feature_names = vectorizer.get_feature_names_out()

# 각 리뷰에 대해
for i in range(len(reviews)):
    # 해당 리뷰의 TF-IDF 벡터를 가져옵니다.
    tfidf_vector = tfidf_matrix[i]

    # TF-IDF 벡터를 배열로 변환하고, 값이 큰 순서대로 정렬한 인덱스를 가져옵니다.
    sorted_indices = tfidf_vector.toarray().argsort()[0][::-1]

    # 상위 10개의 키워드와 그 TF-IDF 점수를 출력합니다.
    for idx in sorted_indices[:10]:
        print(
            f"Keyword: {feature_names[idx]}, TF-IDF score: {tfidf_vector[0, idx]}")
