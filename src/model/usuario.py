from model.abstract_pessoa_sistema import PessoaSistema
from model.carreira import Carreira


class Usuario(PessoaSistema):
    def __init__(self, username: str, nome: str, carreiras, skills_para_aprender):
        super().__init__(username, nome)
        self.__carreiras = carreiras if isinstance(carreiras, list) else []
        self.__skills_para_aprender = []
        self.__skills_aprendidas = []
        self.__projetos_pessoais = {}
        
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username: str):
        if isinstance(username, str):
            self.__username = username
        else:
            raise TypeError("username deve ser do tipo string")
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("nome deve ser do tipo string")

    @property
    def carreira_escolhida(self):
        return self.__carreira_escolhida

    @carreira_escolhida.setter
    def carreira_escolhida(self, carreira: Carreira):
        if isinstance(carreira, Carreira):
            self.__carreira_escolhida = carreira
        else:
            raise TypeError("carreira_escolhida deve ser um objeto Carreira")

    @property
    def carreiras(self):
        return self.__carreiras
    
    @carreiras.setter 
    def carreiras(self, carreiras):
        if isinstance(carreiras, list):
            self.__carreiras = carreiras
        else:
            raise TypeError("carreiras deve ser uma lista")
    
    @property
    def skills_para_aprender(self):
        return self.__skills_para_aprender
    
    @skills_para_aprender.setter
    def skills_para_aprender(self, skills):
        if isinstance(skills, list):
            self.__skills_para_aprender = skills
        else:
            raise TypeError("skills_para_aprender deve ser uma lista")

    @property
    def skills_aprendidas(self):
        return self.__skills_aprendidas
    
    @skills_aprendidas.setter
    def skills_aprendidas(self, skills):
        if isinstance(skills, list):
            self.__skills_aprendidas = skills
        else:
            raise TypeError("skills_aprendidas deve ser uma lista")
