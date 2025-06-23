from model.abstract_pessoa_sistema import PessoaSistema 

class Admin(PessoaSistema):
    def __init__(self):
        super().__init__("admin")

    
    def exibir_informacoes(self):
        return "Perfil: Administrador"
    
    def autenticar(self, tentativa: str) -> bool:
        senha_correta = "admin"
        return tentativa == senha_correta