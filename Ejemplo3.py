import streamlit as st
from PIL import Image

foto_equipo = Image.open("Imagenes/Equip_P&P_2023-24.jpg")
logo_co = Image.open("Imagenes/logo_equip.JPG")

#config
st.set_page_config(
    page_title="Ejemplo3", 
    page_icon="⛳", 
    layout="centered"
   )

with st.container():
    left_column, right_column = st.columns([0.7, 0.3])
    with left_column:
        st.title("Equipo Pitch&Putt Senior Olimpics")
    with right_column:
        st.image(logo_co)
    st.header("Participamos en la liga SEMAR de 3ª división")



if 'boton_imagen' not in st.session_state:
    st.session_state.boton_imagen = False

def click_boton_imagen():
    st.session_state.boton_imagen = not st.session_state.boton_imagen

st.boton_imagen('Imagen', on_click=click_boton_imagen, type="primary")

if st.session_state.boton_imagen:
    # The message and nested widget will remain on the page
    st.image(logo_co)
    
else:
    st.write('')
    