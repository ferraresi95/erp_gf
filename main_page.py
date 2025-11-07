import streamlit as st
from financeiro import mostrar_financeiro
from faturamento import mostrar_faturamento
from controladoria import mostrar_controladoria

st.set_page_config(page_title="ERP - Sistema de Gestão", layout="wide")
st.title("📊 ERP - Sistema de Gestão Empresarial")

menu = st.sidebar.radio("Navegação", ["🏠 Início", "🧾 Faturamento", "💰 Financeiro", "📈 Controladoria"])

if menu == "🏠 Início":
    st.subheader("Bem-vindo ao ERP")
    st.markdown("""
    Escolha um módulo no menu lateral para começar.
    """)
elif menu == "🧾 Faturamento":
    mostrar_faturamento()
elif menu == "💰 Financeiro":
    mostrar_financeiro()
elif menu == "📈 Controladoria":
    mostrar_controladoria()
