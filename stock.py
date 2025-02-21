import streamlit as st
import FinanceDataReader as fdr
import datetime
import time


# 앱 제목
st.title("주식시장 분석 그래프 📈")

# 기본 시작 날짜 설정 (1년 전으로 기본값 설정)
default_start_date = datetime.date.today() - datetime.timedelta(days=365)
start_date = st.date_input("시작 날짜 선택", value=default_start_date)

# 티커 입력
code = st.text_input("종목 코드를 입력하세요 (예: AAPL, 005930 등)", "")

# 데이터 조회 및 시각화
if code and start_date:
    #로딩바 출력
    bar=st.progress(0)
    with st.spinner("Loading..."):
        time.sleep(3)
        st.success("Completed")
    try:
        # 입력된 티커의 데이터 조회
        df = fdr.DataReader(code, start_date)

        # 데이터프레임 표시
        st.subheader(f"{code}의 주가 데이터")
        st.dataframe(df)

        # 주가 시각화 (종가 기준)
        st.subheader(f"{code}의 주가 그래프")
        st.line_chart(df['Close'])

        # S&P 500 데이터 추가 (비교용)
        sp500 = fdr.DataReader("US500", start_date)
        st.subheader("S&P 500 지수")
        st.line_chart(sp500['Close'])

    except Exception as e:
        st.error(f"데이터를 불러오는 데 문제가 발생했습니다: {e}")
else:
    st.warning("종목 코드와 시작 날짜를 입력해주세요.")

