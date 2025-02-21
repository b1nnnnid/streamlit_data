import streamlit as st

st.title("MBTI 성격 유형")
st.header("16가지 성격 유형 중 나는 무엇일까요?")
st.markdown("본인이 해당하는 성향에 체크해주세요!")

col1,col2=st.columns(2)

with col1:
    opt1=st.radio("에너지를 얻는 방법",['E(외향)','I(내향)'])
    opt2=st.radio("정보를 인식하는 방법",['S(직관)','N(감각)'])
    
with col2:
    opt3=st.radio("공감과 이해의 방법",['F(감정)','T(이성)'])
    opt4=st.radio("일을 실행하는 방법",['P(즉흥)','J(계획)'])
    
mbti=opt1[0]+opt2[0]+opt3[0]+opt4[0]

st.subheader(f":orange[{mbti}]")