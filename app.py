import streamlit as st 
st.header("1st Project :sunglasses:")
st.write("# Welcome to Sales Dashboard App 👋")
st.title(":red[Innomatics] Research Labs :sunglasses:")
st.markdown(""" App by :red[Neeraj] """)
st.snow()

btn_click = st.button("click Me!")

if btn_click == True:
    st.subheader("Go to :red[dashboard sales] 👋")
    st.balloons()