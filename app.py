import streamlit as st

st.set_page_config(
    page_title="Lineu Data Stories",
    page_icon=":books:",
    # page_icon="images/logo.png",
    layout="centered",
    initial_sidebar_state="auto",
)

pages = {
    "Portfolio": [
        st.Page("pages/home.py", title="Home", icon="🏡"), #house_with_garden
        st.Page("pages/about.py", title="About", icon="📖"), #open_book
        st.Page("pages/languages.py", title="Languages", icon="🌍"), #earth_africa
        st.Page("pages/contact.py", title="Contact", icon="📞"), #telephone_receiver
    ],
    # "Projects": [
    #      st.Page("pages/example_three.py", title="Learn about us"),
    #      st.Page("pages/example_two.py", title="Try it out"),
    # ],
}

pg = st.navigation(pages)

pg.run()
