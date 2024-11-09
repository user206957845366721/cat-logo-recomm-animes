import streamlit as st

st.set_page_config(
    page_title="Site de Recomendações de Anime!",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("Olá!")
st.write("Seja muito bem-vindo, ou vinda, ao meu site pessoal de recomendações de animes. Este site está sendo produzido para resguardar a criadora de recuperações e possíveis DPs. Espero que goste!")
st.sidebar.success("Select a page above.")

def page_1():
    st.title("Page 1")

pg = st.navigation([st.Page("Page1.py"),
pg.run()
