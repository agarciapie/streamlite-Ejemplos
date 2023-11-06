import streamlit as st
from streamlit_option_menu import option_menu

# Ocultar leyenda Streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Menu principal", ["Home", 'Calendario', 'Resultados'], 
        icons=['house', ':open_book:', "gear"],  
        menu_icon="cast", 
        default_index=1)
    selected
