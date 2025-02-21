import streamlit as st

st.title("Animals")
st.header("What's your pick?")

option=st.selectbox("Which animal do you like?",("cat","dog","owl"))
st.write("You selected a",option)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    
if st.button("Anything else?"):
    st.write("Sorry, we'll be prepared soon.")

if st.text_input("Please give us some feedbacks!"):
    st.markdown("Thank you!")
    
st.caption("This page is made for test.")