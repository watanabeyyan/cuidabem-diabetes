import streamlit as st

#título
st.title("Título da página")

#cabeçalho
st.header("Cabeçalho da página")

#Subcabeçalho
st.subheader("1ª Seção")
#Texto
st.text("Primeira seção do texto")

#Subcabeçalho
st.subheader("2ª Seção")
#Escrever
st.write("Para escrever uma passagem")

#Traço para separar uma seção
st.divider()

#Markdown - Subtítulo
st.markdown("# Subtítulo, basta usar '#' que estipula o nível no subtítulo - Nível 1")
st.markdown("## Subtítulo, basta usar '#' que estipula o nível no subtítulo - Nível 2")
st.markdown("### Subtítulo, basta usar '#' que estipula o nível no subtítulo - Nível 3")