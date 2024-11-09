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
st.image(image="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.1WDt6OUfRe3ghTwloclaJgHaFj%26pid%3DApi&f=1&ipt=c64fac50203b649d165abc8a8cb0224cb413b58117e090a215da26bc3a09717e&ipo=images", width=None)

def teste_1():
    st.title("Teste 1")
    st.write("Wraughthrrjjrbf")

def teste_2():
    st.title("Teste 2")
    st.write("This is the teste2.")
page = st.sidebar.selectbox("De qual anime você quer ler sobre?", ["Teste 1", "Teste 2"])

if page == "Teste 1":
    teste_1()
elif page == "Teste 2":
    teste_2()
