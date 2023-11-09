import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

foto_equipo = Image.open("Imagenes/Equip_P&P_2023-24_1.jpg")
logo_co = Image.open("Imagenes/logo_equip.JPG")

#config
st.set_page_config(page_title="Senior Olimpics P&P", page_icon="⛳", layout="wide")

# Ocultar leyenda Streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.container():
    left_column, right_column = st.columns([0.7, 0.3])
    with left_column:
        st.title("Equip de Pitch&Putt Senior Olimpics")
    with right_column:
        st.image(logo_co)

st.image(foto_equipo)

def menu_change(key):
    selection = st.session_state[key]
    if selection == "Home":
        st.write(f"El menu ha cambiado a {selection}")
        
    if selection == "Calendario":
        #st.write(f"El menu ha cambiado a {selection}")
        st.header("Calendari")
        st.write("[Calendari 2023-24 >](http://www.pipcat.com/seniorsponent/uplds/220/20231022_Calendari_Intercamps_Oest.pdf)")
        
    if selection == "Resultados":
        #st.write(f"El menu ha cambiado a {selection}")
        st.header("Resultats")
        st.write("[Veure resultats SP >](http://pitch.cat/noticies/noticia.php?id=46944)")
        st.write("[Veure resultats MP >](http://www.pitchputt.cat/noticies/noticia.php?id=46838)")

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Menu principal", ["Home", 'Calendario', 'Resultados'], 
        icons=['house', 'book', 'gift'],  
        menu_icon="cast", 
        default_index=1,
        on_change=menu_change,
        key="0")
    
