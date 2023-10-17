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
        st.write(
            """
            Aqui va el calendario
            
            """
        )
