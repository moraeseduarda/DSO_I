from abc import ABC, abstractmethod

class Cadastro(ABC):
    """
    Classe abstrata para cadastro de pessoas.
    """
    
    def __init__(self, nome: str, id: int):
        self.__nome = nome
        self.__id = id
        if not nome or id is None:
            raise ValueError("Nome e ID não podem ser nulos.")
        
    @property
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,id):
        self.__id = id
    
    @abstractmethod
    def __str__(self):
        pass
