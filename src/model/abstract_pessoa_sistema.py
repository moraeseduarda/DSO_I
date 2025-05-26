from abc import ABC, abstractmethod

class PessoaSistema(ABC):
    def __init__(self, username: str, nome: str):
        if isinstance(username, str):
            self.__username = username
        else:
            raise TypeError("username deve ser do tipo string")

        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("nome deve ser do tipo string")

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