import streamlit as st

from PIL import Image

foto_equipo = Image.open("Imagenes/Equip_P&P_2023-24_1.jpg")
logo_co = Image.open("Imagenes/logo_equip.JPG")

#config
st.set_page_config(page_title="Senior Olimpics P&P", page_icon="⛳")

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

st.sidebar.success("Selecciona una opció")