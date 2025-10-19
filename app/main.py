import streamlit as st
from parser import parse_plano_estudo

st.set_page_config(page_title="AIA Mentora", page_icon="🤖", layout="centered")
st.title("🤖 AIA Mentora — Sistema de Recomendação de Estudos")

st.markdown("Cole abaixo o plano de estudo gerado pelo ChatGPT 👇")

texto = st.text_area("Plano de estudo", height=300)

if st.button("Gerar estrutura"):
    if texto.strip() != "":
        df = parse_plano_estudo(texto)
        st.dataframe(df)
        st.download_button("📥 Baixar como CSV", df.to_csv(index=False), "trilha.csv")
    else:
        st.warning("Cole um plano de estudo antes de continuar.")
