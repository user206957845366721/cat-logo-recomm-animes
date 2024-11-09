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
    rating= 5
    full_stars = "⭐" * rating
    empty_stars = "⭕" * (5 - rating)
    stars = full_stars + empty_stars
    st.title("One Piece")
    st.image(image="one-piece.jpg", width=None)
    st.write(stars)
    st.write("Escrever sobre one piece aqui.")

def megami_sama():
    rating= 5
    full_stars = "⭐" * rating
    empty_stars = "⭕" * (5 - rating)
    stars = full_stars + empty_stars
    st.title("A! Megami Sama!")
    st.image(image="megamisama.png", width=None)
    st.write(stars)
    st.write("Escrever sobre megami sama aqui.")

def taihou_shichauzo():
    rating= 5
    full_stars = "⭐" * rating
    empty_stars = "⭕" * (5 - rating)
    stars = full_stars + empty_stars
    st.title("Taihou Shichauzo/You're Under Arrest!")
    st.image(image="taihou-shichauzo.jpg", width=None)
    st.write(stars)
    st.write("Escrever sobre taihou shichauzo aqui.")

def akage_ann():
    rating= 5
    full_stars = "⭐" * rating
    empty_stars = "⭕" * (5 - rating)
    stars = full_stars + empty_stars
    st.title("Akage no Ann")
    st.image(image="akage-no-ann.jpg", width=None)
    st.write(stars)
    st.write("Escrever sobre akage aqui.")

def cardcaptor_sakura():
    rating= 5
    full_stars = "⭐" * rating
    empty_stars = "⭕" * (5 - rating)
    stars = full_stars + empty_stars
    st.title("Cardcaptor Sakura")
    st.image(image="cardcaptor-sakura.jpg", width=None)
    st.write(stars)
    st.write("Escrever sobre sakura aqui.")

def dragon_ball():
    rating= 5
    full_stars = "⭐" * rating
    empty_stars = "⭕" * (5 - rating)
    stars = full_stars + empty_stars
    st.title("Dragon Ball")
    st.image(image="dragon-ball.jpg", width=None)
    st.write(stars)
    st.write("Escrever sobre dragon ball aqui.")

def inuyasha():
    rating= 5
    full_stars = "⭐" * rating
    empty_stars = "⭕" * (5 - rating)
    stars = full_stars + empty_stars
    st.title("Inuyasha")
    st.image(image="inuyasha.jpg", width=None)
    st.write(stars)
    st.write("Escrever sobre inuyasha aqui.")

def naruto():
    rating= 5
    full_stars = "⭐" * rating
    empty_stars = "⭕" * (5 - rating)
    stars = full_stars + empty_stars
    st.title("Naruto (Clássico)")
    st.image(image="naruto.jpg", width=None)
    st.write(stars)
    st.write("Escrever sobre naruto aqui.")

def dungeon_meshi():
    rating= 5
    full_stars = "⭐" * rating
    empty_stars = "⭕" * (5 - rating)
    stars = full_stars + empty_stars
    st.title("Dungeon Meshi")
    st.image(image="dungeon-meshi.png", width=None)
    st.write(stars)
    st.write("Escrever sobre dungeon meshi aqui.")

def sword_art():
    rating= 5
    full_stars = "⭐" * rating
    empty_stars = "⭕" * (5 - rating)
    stars = full_stars + empty_stars
    st.title("Sword Art Online")
    st.image(image="sword-art.jpg", width=None)
    st.write(stars)
    st.write("Escrever sobre sword art aqui.")


page = st.sidebar.selectbox("Sobre qual anime você quer ler?", ["One Piece", "A! Megami Sama!", "Taihou Shichauzo/You're Under Arrest!", "Akage no Ann", "Cardcaptor Sakura", "Dragon Ball", "Inuyasha", "Naruto (Clássico)", "Dungeon Meshi", "Sword Art Online"])

if page == "One Piece":
    one_piece()
elif page == "A! Megami Sama!":
    megami_sama()
elif page == "Taihou Shichauzo/You're Under Arrest!":
    taihou_shichauzo()
elif page == "Akage no Ann":
    akage_ann()
elif page == "Cardcaptor Sakura":
    cardcaptor_sakura()
elif page == "Dragon Ball":
    dragon_ball()
elif page == "Inuyasha":
    inuyasha()
elif page == "Naruto (Clássico)":
    naruto()
elif page == "Dungeon Meshi":
    dungeon_meshi()
elif page == "Sword Art Online":
    sword_art()

#END OF THE CODE.
    
