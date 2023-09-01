from konlpy.tag import Okt
import gensim
from gensim.models import Word2Vec

# 형태소 분석기를 초기화
okt = Okt()

# 텍스트를 형태소 단위로 분리
text = "향수에 대한 키워드, 사람이 가지고 싶은 분위기의 키워드를 매칭해볼 거 거든"
words = okt.morphs(text)

# Word2Vec 모델을 로드
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format(
    '/path/to/ko.bin', binary=True)

# 텍스트를 워드 임베딩 모델로 임베딩
word_embedding = word2vec_model[words[0]]
