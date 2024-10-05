import streamlit as st

st.title('Languages')

st.divider()

col1, col2,col3 = st.columns(3)
with col2:
    uk_flag="images/united-kingdom-flag.svg"
    st.image(uk_flag, width=250)

en = st.slider("English", 0, 100, 95)

st.write("I have studied English in England for 2 years. I also taught English for 6 years.")

st.write("###")

pt = st.slider("Portuguese", 0, 100, 100)

st.write("Well, I am from Brazil, so Portuguese is my native language. :grin:")

st.write("###")

es = st.slider("Spanich", 0, 100, 50)

st.write("I can manage a conversation in Spanish.")
