import streamlit as st

def mostrar_faturamento():
    st.subheader("🧾 Módulo de Faturamento")

    cliente = st.text_input("Cliente")
    produto_servico = st.text_input("Produto/Serviço")
    valor = st.number_input("Valor da fatura", min_value=0.0, format="%.2f")
    data_emissao = st.date_input("Data de emissão")
    vencimento = st.date_input("Data de vencimento")

    if st.button("Emitir fatura"):
        # Aqui você pode integrar com Supabase futuramente
        st.success(f"Fatura emitida para {cliente} no valor de R$ {valor:.2f}")
