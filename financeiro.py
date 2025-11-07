import streamlit as st
from supabase_config import supabase

def mostrar_financeiro():
    st.subheader("💰 Módulo Financeiro")

    tipo = st.selectbox("Tipo", ["entrada", "saida"])
    descricao = st.text_input("Descrição")
    valor = st.number_input("Valor", min_value=0.0, format="%.2f")
    data = st.date_input("Data")
    categoria = st.text_input("Categoria")
    empresa_id = "uuid_da_empresa"  # Pode vir de sessão ou login

    uploaded_file = st.file_uploader("📎 Anexe o comprovante", type=["jpg", "png", "pdf"])
    arquivo_url = None

    if uploaded_file:
        file_bytes = uploaded_file.read()
        file_name = f"comprovantes/{uploaded_file.name}"
        supabase.storage.from_("comprovantes").upload(file_name, file_bytes)
        arquivo_url = f"{supabase.rest_url}/storage/v1/object/public/{file_name}"
        st.success("Arquivo enviado com sucesso!")

    if st.button("Salvar movimentação"):
        supabase.table("movimentacoes_financeiras").insert({
            "empresa_id": empresa_id,
            "tipo": tipo,
            "descricao": descricao,
            "valor": valor,
            "data": str(data),
            "categoria": categoria,
            "arquivo_url": arquivo_url
        }).execute()
        st.success("Movimentação registrada com sucesso!")
