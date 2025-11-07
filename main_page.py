import streamlit as st
from financeiro import mostrar_financeiro
from faturamento import mostrar_faturamento
from controladoria import mostrar_controladoria
from gestao_usuarios.interface import mostrar_usuarios
from supabase_config import supabase

def testar_conexao_supabase():
    try:
        resposta = supabase.table("usuarios").select("*").limit(1).execute()
        return resposta.data or "Conexão OK, mas nenhum dado encontrado."
    except Exception as e:
        return f"Erro na conexão: {e}"

# Configuração da página
st.set_page_config(page_title="ERP - Sistema de Gestão", layout="wide", page_icon="📊")

# Cabeçalho principal
st.markdown("""
    <style>
        .titulo-principal {
            font-size: 40px;
            font-weight: bold;
            color: #2c3e50;
        }
        .subtitulo {
            font-size: 20px;
            color: #7f8c8d;
        }
    </style>
    <div class="titulo-principal">📊 ERP - Sistema de Gestão Empresarial</div>
    <div class="subtitulo">Organize, controle e cresça com eficiência</div>
""", unsafe_allow_html=True)

# Menu lateral
menu = st.sidebar.radio(
                            "📁 Navegação"
                            , [
                                    "🏠 Início"
                                    ,"👤Gestão de Usuários"
                                    ,"🗂️ Cadastros"
                                    , "🧾 Faturamento"
                                    , "💰 Financeiro"
                                    , "📈 Controladoria"
                            ]
                    )

# Conteúdo principal
if menu == "🏠 Início":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("👋 Bem-vindo ao ERP")
        st.markdown("""
        Este sistema foi desenvolvido para facilitar a gestão financeira e operacional da sua empresa.
        
        **Funcionalidades disponíveis:**
        - 💰 Controle Financeiro
        - 🧾 Faturamento
        - 📈 Relatórios de Controladoria

        Use o menu lateral para navegar entre os módulos.
        """)
    with col2:
        st.image("https://cdn-icons-png.flaticon.com/512/2920/2920257.png", width=150)

elif menu == "👤Gestão de Usuários":
    mostrar_usuarios()

elif menu == "🧾 Faturamento":
    mostrar_faturamento()

elif menu == "💰 Financeiro":
    mostrar_financeiro()

elif menu == "📈 Controladoria":
    mostrar_controladoria()

st.markdown("### 🔌 Teste de conexão com Supabase")
resultado = testar_conexao_supabase()
st.write(resultado)
