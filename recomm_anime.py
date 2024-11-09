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

def teste_1():
    st.title("Teste 1")
    st.write("Teste.")

def teste_2()
st.title("Teste 2")
st.write("Teste.")

page = st.sidebar.selectbox("De qual anime você quer ler sobre?", ["Teste 1", "Teste 2"])

if page == "Teste 1"
    teste_1()
elif page == "Teste 2"
    teste_2()
