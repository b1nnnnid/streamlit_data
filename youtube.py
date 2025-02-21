import streamlit as st
from googleapiclient.discovery import build
import google.generativeai as genai
import os
#https://www.youtube.com/watch?v=J4vEoFVcguw



# API 키 가져오기(키 가져오는 방식에 따라 해당 부분 수정 필요합니다)
#with open("private") as f:
#    api_key = f.read().strip()

genai.configure(api_key="AIzaSyBA47UPEA6lfKAQXJc1-Qnq90ERt4PI1sU")

# [TODO]YouTube Data API 클라이언트 설정
YOUTUBE_API_KEY = "AIzaSyD0LbhvPKHojwZ1ilf_XK5LdeCGEG-NzEE"#
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def get_video_description(video_id):
    try:
        response = youtube.videos().list(part="snippet", id=video_id).execute()
        description = response["items"][0]["snippet"]["description"]
        return description if description else "비디오 설명이 없습니다."
    except Exception as e:
        st.error(f"비디오 설명을 가져오는 데 실패했습니다: {e}")
        return None

def summarize_text_with_gemini(text):
    try:
        # [TODO] 모델을 통한 요약 생성
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"다음 텍스트를 한국어로 간결하게 요약해줘:\n\n{text}"
        # 모델의 결과를 받고싶습니다
        response = model.generate_content(prompt)
        # 결과에서 텍스트만 출력하고 싶습니다
        summary = response.text
        return summary.strip()
    except Exception as e:
        st.error(f"요약 생성에 실패했습니다: {e}")
        return None

st.title("YouTube 비디오 설명 요약기")

video_url = st.text_input("YouTube 비디오 URL을 입력하세요")
if video_url:
    if "v=" in video_url:
        video_id = video_url.split("v=")[1].split("&")[0]
    else:
        st.error("유효한 YouTube URL을 입력하세요.")

    # [TODO] 버튼을 눌렀을때 하위 작업들이 작동되도록 해야함.
    if st.button:
        
        # [TODO] 비디오를 스트리밍하기 위한 iframe 생성에는 영상 주소가 필요합니다
        st.video(video_url)
        
        description = get_video_description(video_id)
        if description:
            summary = summarize_text_with_gemini(description)
            if summary:
                st.subheader("요약:")
                # [TODO] AI 요약을 출력(st)
                st.write(summary)
            else:
                st.warning("요약을 생성할 수 없습니다.")
