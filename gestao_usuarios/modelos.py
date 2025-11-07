class Usuario:
    def __init__(self, nome, email, senha, perfil):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.perfil = perfil

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "perfil": self.perfil
        }
