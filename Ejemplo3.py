import streamlit as st
from PIL import Image

foto_equipo = Image.open("Imagenes/Equip_P&P_2023-24.jpg")
logo_co = Image.open("Imagenes/logo_equip.JPG")

#config
st.set_page_config(
    page_title="Ejemplo3", 
    page_icon="💀", 
    layout="wide")

