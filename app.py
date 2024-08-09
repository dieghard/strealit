import streamlit as st
from  PIL import Image

st.set_page_config(page_title="🐍nake🐍osftDev", page_icon="🤖", layout="wide")
with st.container():
    st.header("Hola! ✋, somos 🐍nake🐍osftDev")
    st.title("Creamos las soluciones necesarias para acelerar tu negocio")
    st.write("En 🐍nake🐍osftDev, somos apasionados de la tecnologia, creemos que con ella podemos ayudar a las empresas y negocios a mejorar sus procesos  de crecimiento y toma de desiociones. ")
    st.write("[saber mas sobre nosotros->](https://www.nakeosftdev.com/)")

    #sobre nosotros
with st.container():
    st.write("---")
    text_colum, animation_column = st.columns(2)
    with text_colum:
        st.header("Sobre nosotros")
        st.write("""Somos una empresa de desarrollo de software, especializada en la creación de soluciones tecnológicas para empresas y negocios. Nuestro objetivo es ayudar a las empresas a mejorar sus procesos de crecimiento y toma de desiciones.

        - Desarrollo de software a medida
        - Desarrollo de aplicaciones web y móviles
        - Consultoría tecnológica
        - Diseño de interfaces
        - Automatización de procesos
        - Inteligencia artificial
        - Machine learning
        - Big data
        - Cloud computing
        - Ciberseguridad
        """)
    st.write("[saber mas sobre nosotros->](https://www.nakeosftdev.com/)")
    with animation_column:
        st.empty()
