import streamlit as st

st.title('Languages')

st.divider()

col1, mid, col2 = st.columns([5, 1, 20])
with col1:
    st.image('images/united-kingdom-flag.svg', width=100)
with col2:
    en = st.slider("English", 0, 100, 95)
    st.write("I have studied English in England for 2 years. I also taught English for 6 years.")

st.write("###")

col1, mid, col2 = st.columns([5, 1, 20])
with col1:
    st.image('images/brazil-flag.svg', width=100)
with col2:
    en = st.slider("Portuguse", 0, 100, 100)
    st.write("Well, I am from Brazil, so Portuguese is my native language. :grin:")

st.write("###")

col1, mid, col2 = st.columns([5, 1, 20])
with col1:
    st.image('images/spain-flag.svg', width=100)
with col2:
    en = st.slider("Spanish", 0, 100, 50)
    st.write("I can manage a conversation in Spanish.")