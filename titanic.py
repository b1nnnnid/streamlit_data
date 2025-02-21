import streamlit as st
import pandas as pd
import time
##캐시랑 세션스테이트 실습
st.title("타이타닉 생존자 분석 대시보드")
st.write("이 대시보드는 타이타닉 승객들의 생존 여부를 분석합니다.")

#캐시 미적용
def load_data_without_cache():
    #time.sleep(2)
    data=pd.read_csv(r"C:\Users\유수빈\OneDrive\Desktop\AI인재교육\오프라인 교육\2일차_Streamlit 기초\2-3일차 실습자료\titanic.csv")
    return data
#캐시 적용
@st.cache_data
def load_data():
    #time.sleep(2)
    data=pd.read_csv(r"C:\Users\유수빈\OneDrive\Desktop\AI인재교육\오프라인 교육\2일차_Streamlit 기초\2-3일차 실습자료\titanic.csv")
    return data

st.write(load_data_without_cache())
st.write(load_data())

#세션스테이트 활용
if "counter" not in st.session_state:
    st.session_state.counter=0
    
if st.button("증가"):
    st.session_state.counter+=1
    
st.write(f"현재 카운터값: {st.session_state.counter}")


df=pd.DataFrame({
    "name":['a','b','c'],
    "age":[10,20,30]
})
#데이터프레임 초기화
if 'final_df' not in st.session_state:
    st.session_state["final_df"]=df
    
st.subheader("변경 전 데이터")
st.table(st.session_state.final_df)

if st.button("행 추가"):
    new_row=pd.DataFrame({"name":['d'],"age":[40]})
    st.session_state.final_df=pd.concat(
        [st.session_state.final_df,new_row],
        ignore_index=True
    )
    
st.subheader("변경 후 데이터") #원래 df는 변경x
st.table(st.session_state.final_df)