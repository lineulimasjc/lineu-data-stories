import streamlit as st

st.title('Welcome to my portfolio!')

st.write("###")

st.subheader("Here you will find my Data Analysis :bar_chart: projects.")

st.write("###")

st.subheader("Also, I will publish some tutorials :memo: in order to help the community. :wink:")

st.write("###")

col1, mid, col2 = st.columns([20, 10, 20])
with col1:
    st.image('images/big-data-database.svg', width=100)
with col2:
    st.image('images/analystics-business-chart.svg', width=100)