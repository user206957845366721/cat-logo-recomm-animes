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

def one_piece():
    st.title("One Piece")
    st.image(image="one-piece.jpg", width=None)
    st.write("Escrever sobre one piece aqui.")

def about_page():
    st.title("About Page")
    st.write("This is the about page.")

def contact_page():
    st.title("Contact Page")
    st.write("This is the contact page.")

page = st.sidebar.selectbox("Select a page", ["Home", "About", "Contact"])

if page == "Home":
    home_page()
elif page == "About":
    about_page()
elif page == "Contact":
    contact_page()
