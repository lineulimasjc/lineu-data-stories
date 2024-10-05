import streamlit as st

st.title('Contact')

st.divider()

col1, mid, col2 = st.columns([1, 1, 20])
with col1:
    st.image('images/github.svg', width=48)
with col2:
    st.write("GitHub:https://github.com/lineulimasjc")


col1, mid, col2 = st.columns([1, 1, 20])
with col1:
    st.image('images/LinkedIn.svg', width=48)
with col2:
    st.write("LinkedIn: https://www.linkedin.com/in/lineulima/")
