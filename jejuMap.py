import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster

st.title("제주도 핫플레이스")

df=pd.read_csv(r"C:\Users\유수빈\OneDrive\Desktop\AI인재교육\오프라인 교육\2일차_Streamlit 기초\2-3일차 실습자료\jeju_place.csv")

tab1,tab2=st.tabs(["최다등록 장소","위치정보 조회"])

with tab1:

    m=folium.Map([sum(df["위도"])/len(df["위도"]),sum(df["경도"])/len(df["경도"])],zoom_start=9)
    marker_cluster=MarkerCluster().add_to(m)

    for i,j in zip(df["위도"],df["경도"]):
     folium.CircleMarker(
            [i,j]
     ).add_to(marker_cluster)

    folium_static(m)

with tab2:
    
    df[["lat","lon"]]=df[["위도","경도"]]
    st.map(df)

