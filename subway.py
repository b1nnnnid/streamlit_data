import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
import plotly.express as px

# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # Windows의 기본 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지지 않도록 설정

st.title("지하철 혼잡도 분석 및 시각화")

def load_data():
    df = pd.read_csv(r"C:\Users\유수빈\OneDrive\Desktop\AI인재교육\오프라인 교육\2일차_Streamlit 기초\2-3일차 실습자료\subway_congestion.csv", encoding="utf-8")
    df_melted= df.melt(id_vars=["요일구분", "호선", "역번호", "출발역","상하구분"], var_name="시간대", value_name="혼잡도")
    df_melted['시간대'] = df_melted['시간대'].str.replace("시", ":").str.replace("분","")
    return df_melted
df = load_data()

# 사이드바 설정
st.sidebar.title("혼잡도 설정")
selected_day = st.sidebar.selectbox("요일 선택", options=df["요일구분"].unique())
selected_line = st.sidebar.selectbox("지하철 호선 선택", options=sorted(df["호선"].unique()))

# 데이터 필터링
filtered_data = df[(df["요일구분"] == selected_day) & (df["호선"] == selected_line)]

# 피벗 테이블 생성 (출발역 기준, 시간대별 평균 혼잡도 계산)
heatmap_data = filtered_data.pivot_table(index="출발역", columns="시간대", values="혼잡도", aggfunc="mean")

# 히트맵 시각화
st.subheader(f"{selected_day} - {selected_line}호선 혼잡도 히트맵")
if not heatmap_data.empty:
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, annot=False, cmap="YlOrRd", cbar=True)  
    st.pyplot(plt)
else:
    st.warning("선택한 요일과 호선에 대한 데이터가 없습니다.")
