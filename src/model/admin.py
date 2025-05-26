from model.pessoa_sistema import PessoaSistema

class Admin(PessoaSistema):
    def __init__(self, username: str, nome: str):
        super().__init__(username, nome)