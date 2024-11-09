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
st.image(image="separador.png", use_column_width='auto')

full_stars = "⭐" * rating
empty_stars = "⭕" * (5 - rating)
stars = full_stars + empty_stars

def one_piece():
    rating=
    st.title("One Piece")
    st.write(stars)
    st.image(image="one-piece.jpg", width=None)
    st.write("Escrever sobre one piece aqui.")

def megami_sama():
    rating=
    st.title("A! Megami Sama!")
    st.write(stars)
    st.image("megamisama.png", width=None)
    st.write("Escrever sobre  aqui.")

def teste_1():
    st.title("Teste 1")
    st.write("Wraughthrrjjrbf")

def teste_2():
    st.title("Teste 2")
    st.write("This is the teste2.")

def teste_1():
    st.title("Teste 1")
    st.write("Wraughthrrjjrbf")

def teste_1():
    st.title("Teste 1")
    st.write("Wraughthrrjjrbf")

def teste_1():
    st.title("Teste 1")
    st.write("Wraughthrrjjrbf")

def teste_1():
    st.title("Teste 1")
    st.write("Wraughthrrjjrbf")

def teste_1():
    st.title("Teste 1")
    st.write("Wraughthrrjjrbf")

def teste_1():
    st.title("Teste 1")
    st.write("Wraughthrrjjrbf")
page = st.sidebar.selectbox("De qual anime você quer ler sobre?", ["Teste 1", "Teste 2"])

if page == "Teste 1":
    teste_1()
elif page == "Teste 2":
    teste_2()
