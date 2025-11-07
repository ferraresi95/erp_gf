from supabase_config import supabase
from gestao_usuarios.modelos import Usuario
from datetime import datetime

def cadastrar_usuario(nome, email, senha, perfil):
    try:
        usuario = Usuario(nome, email, senha, perfil)
        dados = usuario.to_dict()
        resposta = supabase.table("usuarios").insert(dados).execute()
        return resposta.data
    except Exception as e:
        return f"Erro ao cadastrar usuário: {e}"

def listar_usuarios():
    try:
        resposta = supabase.table("usuarios").select("*").order("nome", ascending=True).execute()
        return resposta.data or []
    except Exception as e:
        return f"Erro ao listar usuários: {e}"

def excluir_usuario(id_usuario):
    try:
        supabase.table("usuarios").delete().eq("id", id_usuario).execute()
    except Exception as e:
        return f"Erro ao excluir usuário: {e}"

def autenticar_usuario(email, senha):
    try:
        resposta = supabase.table("usuarios").select("*").eq("email", email).eq("senha", senha).single().execute()
        return resposta.data
    except Exception as e:
        return None

def registrar_log_acesso(id_usuario, nome, perfil):
    try:
        supabase.table("logs_acesso").insert({
            "id_usuario": id_usuario,
            "nome": nome,
            "perfil": perfil,
            "data_hora": datetime.now().isoformat()
        }).execute()
    except Exception as e:
        print(f"Erro ao registrar log: {e}")