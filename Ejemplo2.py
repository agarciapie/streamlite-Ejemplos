import streamlit as st
from PIL import Image


#config
st.set_page_config(page_title="Ejemplo2", page_icon="🤖", layout="wide")


with st.container():
    st.subheader("Equipo Pitch&Putt Seniors Canal Olimpic :wave:")
    st.title("Jugamos la liga SEMAR en 3ª división")
    st.write(
        "Somos unos apasionados del deporte del Pitch & Putt."
    )
    st.write("[Saber más >](http://www.pipcat.com/seniorsponent/index.php?mod=pip&op=LlistarPag&fid=1)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Calendario")
        st.write("[Calendario 2023-24 >](http://www.pipcat.com/seniorsponent/uplds/220/20231003_Calendari_Intercamps_Oest.pdf)")
    with right_column:
        st.header("Resultados")
        st.write("[Ver resultados >](http://www.pitchputt.cat/noticies/noticia.php?id=46745)")
        