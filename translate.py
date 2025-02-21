import requests
import streamlit as st

# Hugging Face API 설정
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-ko-en"

# 번역 함수
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

# Streamlit UI
st.title("한국어-영어 번역 챗봇")
st.write("한국어로 메시지를 입력하면 영어로 번역해 드립니다.")

# 사용자 입력
user_input = st.text_input("메시지를 입력하세요", "")
# 번역하기 버튼을 누르면 번역을 진행하고 번역 결과를 출력해줍니다.
if st.button("번역하기"):
    st.write(translate_text(user_input))
