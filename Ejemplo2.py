import streamlit as st
from PIL import Image

foto_equipo = Image.open("Imagenes/Equip_P&P_2023-24.jpg")
logo_co = Image.open("Imagenes/logo_equip.JPG")

#config
st.set_page_config(page_title="Senior Olimpics P&P", page_icon="⛳", layout="wide")

st.image(foto_equipo)

with st.container():
    left_column, right_column = st.columns([0.7, 0.3])
    with left_column:
        st.title("Equip de Pitch&Putt Senior Olimpics")
    with right_column:
        st.image(logo_co)
    st.header("Competim a la lliga SEMAR de 3ª divisió")
    st.header("Juguem al camp de P&P del Canal Olímpic. Castelldefels")
    st.subheader("Som uns apassionats del esport del Pitch & Putt")
    st.write("[Saber mès >](http://www.pipcat.com/seniorsponent/index.php?mod=pip&op=LlistarPag&fid=1)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Calendari")
        st.write("[Calendari 2023-24 >](http://www.pipcat.com/seniorsponent/uplds/220/20231022_Calendari_Intercamps_Oest.pdf)")
    with right_column:
        st.header("Resultats")
        st.write("[Veure resultats SP >](http://pitch.cat/noticies/noticia.php?id=46944)")
        st.write("[Veure resultats MP >](http://www.pitchputt.cat/noticies/noticia.php?id=46838)")
