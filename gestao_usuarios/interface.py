import streamlit as st
from gestao_usuarios.servicos import cadastrar_usuario, listar_usuarios
from gestao_usuarios.validacoes import validar_email, validar_senha

def mostrar_usuarios():
    st.subheader("👤 Gestão de Usuários")

    # Formulário de cadastro
    with st.expander("➕ Cadastrar novo usuário"):
        with st.form("form_usuario"):
            nome = st.text_input("Nome completo")
            email = st.text_input("E-mail")
            senha = st.text_input("Senha", type="password")
            perfil = st.selectbox("Perfil de acesso", ["Administrador", "Financeiro", "Faturamento", "Consulta"])
            enviar = st.form_submit_button("Cadastrar")

            if enviar:
                if not validar_email(email):
                    st.error("E-mail inválido.")
                elif not validar_senha(senha):
                    st.error("Senha fraca. Use pelo menos 6 caracteres.")
                else:
                    resultado = cadastrar_usuario(nome, email, senha, perfil)
                    if isinstance(resultado, str) and resultado.startswith("Erro"):
                        st.error(resultado)
                    else:
                        st.success("Usuário cadastrado com sucesso!")

    # Lista de usuários
    st.markdown("### 👥 Usuários cadastrados")
    usuarios = listar_usuarios()

    if isinstance(usuarios, list) and usuarios:
        st.table(usuarios)
    elif isinstance(usuarios, list):
        st.info("Nenhum usuário cadastrado ainda.")
    else:
        st.error(usuarios)
