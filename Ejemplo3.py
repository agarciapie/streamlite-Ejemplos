import streamlit as st
from PIL import Image
from st_row_buttons import st_row_buttons
from st_btn_select import st_btn_select


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


st.button('Imagen', on_click=click_button, type="primary", help="Muestra Imagen")
st.button('Texto')

if st.session_state.button:
    # The message and nested widget will remain on the page
    st.image(logo_co)
    
else:
    st.write('')

option = st_btn_select(('option1', 'option2', 'option3', 'option4'), index=2)
st.write(f'Selected option: {option}')

selection = st_row_buttons(('option 1', 'option 2', 'option 3'))
st.write(f'Opcion seleccionada: {selection}')
