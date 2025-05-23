from model.carreira import Carreira

class Usuario:
    def __init__(self, username: str, nome: str, carreiras):
        if isinstance(username, str):
            self.__username = username
        else:
            raise TypeError("username deve ser do tipo string")

        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("nome deve ser do tipo string")
        
        self.carreiras = carreiras
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