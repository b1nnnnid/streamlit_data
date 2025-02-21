import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import plotly.express as px

st.title("dataframe")

data_df=pd.DataFrame({
    "sales":[
        [10,20,30,40,50,60],
        [101,20,30,40,50,60],
        [102,20,30,40,50,60],
        [103,20,30,40,50,60],
    ],
    "appointment":["12:30pm","10:20pm","9:40am","7:10am"]
})

st.dataframe(data_df)

st.data_editor(
    data_df,
    column_config={
        "sales":st.column_config.BarChartColumn(
            "Sales(last 6months)", #column title
            help="helping comment",
            y_min=0,
            y_max=200
        )
    },
    hide_index=True
)

data_df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.bar_chart(data_df)


df = pd.read_csv(r"C:\Users\유수빈\OneDrive\Desktop\AI인재교육\오프라인 교육\2일차_Streamlit 기초\2-3일차 실습자료\avocado.csv")

df["date"]=df["date"].apply(lambda x: date.fromisoformat(x))
st.data_editor(df,
    column_config={
         "data":st.column_config.DateColumn("Date")
     })
st.dataframe(df)

    
plot_table = {"geography": ["Boston", "California", "Los Angeles"]}
line_chart = []

for region in plot_table['geography']:
    average_prices = df[df['geography'] == region]['average_price'].tolist()
    line_chart.append(average_prices)
    
plot_table['line'] = line_chart

st.dataframe(plot_table,
    column_config={
        "line": st.column_config.LineChartColumn(
            "Average Price",
            width="medium"
        )
    }
)

pivot_df=pd.pivot_table(df,index="date",columns="geography",values="average_price")
st.bar_chart(pivot_df[plot_table["geography"]])

pivot_df=pd.pivot_table(df,index="date",columns="geography",values="average_price")
st.line_chart(pivot_df[plot_table["geography"]])



selected_geography = st.selectbox(label='Geography', options=df['geography'].unique())
submitted = st.button('Submit')

if submitted:
    filtered_avocado = df[df['geography'] == selected_geography]
    line_fig = px.line(filtered_avocado, 
                      x='date', 
                      y='average_price', 
                      color='type', 
                      title=f'Avocado Prices in {selected_geography}')
    st.plotly_chart(line_fig)