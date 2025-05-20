from model.carreira import Carreira

class Usuario():
    def __init__(self, id: int, nome: str, carreira_escolhida: Carreira):
        self.__id = id
        self.__nome = nome
        self.__carreira_escolhida = carreira_escolhida
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: int):
        if isinstance(id, int):
            self.__id = id
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def carreira_escolhida(self):
        return self.__carreira_escolhida

    @carreira_escolhida.setter
    def carreira_escolhida(self, carreira: Carreira):
        if isinstance(carreira, Carreira):
            self.__carreira_escolhida = carreira
