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



if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('Click me', on_click=click_button)

if st.session_state.button:
    # The message and nested widget will remain on the page
    #st.write('Button is on!')
    st.slider('Select a value')
else:
    st.write('Button is off!')