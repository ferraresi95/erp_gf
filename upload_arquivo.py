import streamlit as st
from supabase import create_client

# Conexão Supabase
url = "https://<sua-url>.supabase.co"
key = "<sua-chave>"
supabase = create_client(url, key)

# Upload de comprovante
uploaded_file = st.file_uploader("📎 Anexe o comprovante", type=["jpg", "png", "pdf"])
if uploaded_file:
    file_bytes = uploaded_file.read()
    file_name = f"comprovantes/{uploaded_file.name}"
    res = supabase.storage.from_("comprovantes").upload(file_name, file_bytes)
    st.success("Arquivo enviado com sucesso!")
    arquivo_url = f"{url}/storage/v1/object/public/{file_name}"
