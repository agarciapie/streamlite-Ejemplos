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

def menu_change(key):
    selection = st.session_state[key]
    if selection == "Home":
        st.write(f"El menu ha cambiado a {selection}")
        
    if selection == "Calendario":
        st.write(f"El menu ha cambiado a {selection}")
        
    if selection == "Resultados":
        st.write(f"El menu ha cambiado a {selection}")

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Menu principal", ["Home", 'Calendario', 'Resultados'], 
        icons=['house', 'book', 'gift'],  
        menu_icon="cast", 
        default_index=1,
        on_change=menu_change,
        key="0")
    
