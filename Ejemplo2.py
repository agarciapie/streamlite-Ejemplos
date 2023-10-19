import streamlit as st
from PIL import Image

foto_equipo = Image.open("Imagenes/Equip_P&P_2023-24.jpg")
logo_co = Image.open("Imagenes/logo_equip.JPG")

#config
st.set_page_config(page_title="Ejemplo2", page_icon="🤖", layout="wide")


with st.container():
    left_column, right_column = st.columns(0.7, 0.3)
    with left_column:
        st.title("Equipo Pitch&Putt Senior Olimpics")
    with right_column:
        st.image(logo_co)
    st.header("Participamos en la liga SEMAR de 3ª división")
    st.header("Jugamos en el campo de P&P del Canal Olímpico. Castelldefels")
    st.subheader("Somos unos apasionados del deporte del Pitch & Putt.")

    st.write("[Saber más >](http://www.pipcat.com/seniorsponent/index.php?mod=pip&op=LlistarPag&fid=1)")

    st.image(foto_equipo)

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Calendario")
        st.write("[Calendario 2023-24 >](http://www.pipcat.com/seniorsponent/uplds/220/20231003_Calendari_Intercamps_Oest.pdf)")
    with right_column:
        st.header("Resultados")
        st.write("[Ver resultados >](http://pitch.cat/noticies/noticia.php?id=46944)")
