import streamlit as st
from parser import parse_plano_estudo

st.set_page_config(page_title="AIA Mentora", page_icon="🤖", layout="centered")

st.title("🎓 Recomendação de Estudos — AIA Mentora")
st.markdown("Cole abaixo o **plano de estudo gerado pelo ChatGPT** 👇")

texto = st.text_area("Plano de estudo", height=300)

if st.button("Gerar estrutura"):
    if texto.strip() != "":
        df = parse_plano_estudo(texto)

        if df.empty:
            st.warning("Não foi possível identificar módulos. Verifique o formato do texto.")
        else:
            st.success("✅ Estrutura de aprendizado identificada!")
            total_horas = df['duracao_horas'].dropna().sum()
            st.write(f"**Carga horária total estimada:** {int(total_horas)} horas")

            st.dataframe(df)

            st.download_button("📥 Baixar plano como CSV", df.to_csv(index=False), "trilha.csv")
    else:
        st.warning("Cole um plano de estudo antes de continuar.")
