from model.abstract_pessoa_sistema import PessoaSistema 

class Admin(PessoaSistema):
    def __init__(self):
        super().__init__("admin")