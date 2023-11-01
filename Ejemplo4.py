import streamlit as st
from PIL import Image

# Side bar

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

with st.container():
    st.title("Equip de Pitch&Putt Senior Olimpics")
    st.header("Competim a la lliga SEMAR de 3ª divisió")
    st.header("Juguem al camp de P&P del Canal Olímpic. Castelldefels")
    st.subheader("Som uns apassionats del esport del Pitch & Putt")

# Ocultar leyenda Streamlit
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)