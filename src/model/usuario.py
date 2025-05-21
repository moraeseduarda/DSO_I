from model.carreira import Carreira

class Usuario():
    def __init__(self, id: int, nome: str, carreiras):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError("id deve ser um inteiro")

        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("nome deve ser uma string")
        
        self.carreiras = carreiras
        self.__skills_para_aprender = []
        self.__skills_aprendidas = []
        self.__projetos_pessoais = {}
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError("id deve ser um inteiro")
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("nome deve ser uma string")

    @property
    def carreira_escolhida(self):
        return self.__carreira_escolhida

    @carreira_escolhida.setter
    def carreira_escolhida(self, carreira: Carreira):
        if isinstance(carreira, Carreira):
            self.__carreira_escolhida = carreira
        else:
            raise TypeError("carreira_escolhida deve ser um objeto Carreira")