from gestao_usuarios.modelos import Usuario
from gestao_usuarios import supabase  # se você inicializou no __init__.py

def cadastrar_usuario(nome, email, senha, perfil):
    dados = {
        "nome": nome,
        "email": email,
        "senha": senha,  # idealmente criptografar no futuro
        "perfil": perfil
    }
    supabase.table("usuarios").insert(dados).execute()

def listar_usuarios():
    response = supabase.table("usuarios").select("*").execute()
    if response.data:
        return response.data
    return []

def excluir_usuario(id_usuario):
    supabase.table("usuarios").delete().eq("id", id_usuario).execute()
