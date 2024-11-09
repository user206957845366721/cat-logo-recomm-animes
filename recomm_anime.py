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
    rating= 5
    st.title("One Piece")
    st.write(stars)
    st.image(image="one-piece.jpg", width=None)
    st.write("Escrever sobre one piece aqui.")

def megami_sama():
    rating= 5
    st.title("A! Megami Sama!")
    st.write(stars)
    st.image(image="megamisama.png", width=None)
    st.write("Escrever sobre  aqui.")

def taihou_shichauzo():
    rating= 5
    st.image(image="taihou-shichauzo.jpg", width=None)
    st.title("Taihou Shichauzo/You're Under Arrest!")
    st.write("Escrever sobre  aqui.")

def akage_ann():
    rating= 5
    st.image(image="akage-no-ann.jpg", width=None)
    st.title("Akage no Ann")
    st.write("Escrever sobre  aqui.")
    
page = st.sidebar.selectbox("De qual anime você quer ler sobre?", ["One Piece", "A! Megami Sama!", "Taihou Shichauzo/You're Under Arrest!", "Akage no Ann"])

if page == "One Piece":
    one_piece()
elif page == "A! Megami Sama!":
    megami_sama()
elif page == "Taihou Shichauzo/You're Under Arrest!":
    taihou_shichauzo()
elif page == "Akage no Ann":
    akage_ann()
