import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt

#타이타닉 데이터 분석 실습
st.title("타이타닉 생존자 분석 대시보드")
st.write("이 대시보드는 타이타닉 승객들의 생존 여부를 분석합니다.")

#데이터 로드
@st.cache_data
def load_data():
    time.sleep(2)
    data=pd.read_csv(r"C:\Users\유수빈\OneDrive\Desktop\AI인재교육\오프라인 교육\2일차_Streamlit 기초\2-3일차 실습자료\titanic.csv")
    return data

st.write(load_data())
data=pd.DataFrame(load_data())

#데이터 통계 요약
st.write(data.describe())

#성별 간 생존율 차이 시각화
survival=data.groupby('Sex')["Survived"].mean()
#plt.plot(survival)

#연령 분포 시각화
plt.hist(data["Age"].dropna(),bins=30)
st.pyplot(plt)

#데이터 필터링 기능
selected_class=st.selectbox("select class",data["Pclass"].unique())
gender=st.radio("select gender",data["Sex"].unique())
filtered_data=data[(data["Pclass"]==selected_class)&(data["Sex"]==gender)]
st.write(filtered_data)

#필터링된 데이터 다운로드
st.download_button(
    "필터링된 데이터 다운로드",
    data=filtered_data.to_csv().encode("utf-8"),
    filename="filtered_data.csv",
    mine="text/csv"
)