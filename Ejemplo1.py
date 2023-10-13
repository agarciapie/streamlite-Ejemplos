
import streamlit as st
from PIL import Image



#config
#comentario
st.set_page_config(page_title="Ejemplo1", page_icon="🤖", layout="wide")

with st.container():
    st.subheader("Hola, somos Valerapp :wave:")
    st.title("Creamos soluciones para acelerar tu negocio")
    st.write(
        "Somos unos apasionados de la tecnología y la innovación, especializados en el sector de la digitalización y automatización de negocios. Nos gusta crear soluciones para resolver problemas y mejorar procesos."
    )
    st.write("[Saber más >](https://valerapp.com/)")