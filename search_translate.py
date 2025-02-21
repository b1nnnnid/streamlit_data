import requests
import streamlit as st
from serpapi import GoogleSearch

# Hugging Face API 설정
API_TOKEN = "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"  # Hugging Face API 토큰 입력
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ko-en"
  # Hugging Face 번역 API URL 입력

# SerpAPI 설정
serp_key = "08dcbf03dd0b765a58670d4fdecd8db54f31990a2b00ab4c9e8a334b1fcebc8d" # SerpAPI API 키 입력

# 뉴스 검색 함수 (tbm : nws)
def search_news(keyword):
    params = {
        "q": keyword,  # 검색어
        "location": "Korea",  # 검색 위치
        "hl": "ko",  # 검색 결과 언어 (한글)
        "gl": "kr",  # 국가 설정 (한국)
        "google_domain": "google.com",  # 검색 엔진 도메인
        "api_key": serp_key  # 발급받은 API 키
    }
    search = GoogleSearch(params)
    results = search.get_dict()

    # 뉴스 제목 및 링크만 추출하여 최대 3개만 반환
    if 'organic_results' in results:
        final_res = results['organic_results'][:3]
    else:
        final_res = []

    return final_res

# Hugging Face 번역 함수
def translate_text(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        result = response.json()
        if result and "translation_text" in result[0]:
            return result[0]["translation_text"]
        else:
            st.error("번역 결과 형식이 예상과 다릅니다.")
            return None
    else:
        st.error(f"Translation Error: {response.status_code}")
        return None

# Streamlit 앱
st.title("뉴스 검색 및 번역")
st.write("뉴스를 검색하고 첫 번째 뉴스 제목을 번역합니다.")

# 키워드 입력
keyword = st.text_input("검색할 뉴스 키워드를 입력하세요", "기술 뉴스")

if st.button("뉴스 검색 및 번역"):
    with st.spinner("뉴스 검색 중..."):
        news_results = search_news(keyword)
        if news_results:
            st.subheader("검색된 뉴스 기사")
            for i, news in enumerate(news_results):
                st.write(f"{i+1}. [{news['title']}]({news['link']})")

            st.subheader("첫 번째 뉴스 제목 번역")
            # 첫 번째 뉴스 제목만 번역
            translated_title = translate_text(news_results[0]['title'])
            if translated_title:
                st.write(f"원본 제목: {news_results[0]['title']}")
                st.write(f"번역된 제목: {translated_title}")
        else:
            st.warning("뉴스 검색 결과가 없습니다. 키워드를 다시 입력하세요.")
