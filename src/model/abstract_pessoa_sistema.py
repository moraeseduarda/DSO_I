from abc import ABC, abstractmethod


class PessoaSistema(ABC):
    def __init__(self, palavra_chave: str):
        if isinstance(palavra_chave, str):
            self.__palavra_chave = palavra_chave
        else:
            raise TypeError("palavra_chave deve ser do tipo string")

    @property
    def palavra_chave(self):
        return self.__palavra_chave
    
    @palavra_chave.setter
    def palavra_chave(self, palavra_chave: str):
        if isinstance(palavra_chave, str):
            self.__palavra_chave = palavra_chave
        else:
            raise TypeError("palavra_chave deve ser do tipo string")

    @abstractmethod
    def exibir_informacoes(self):
        pass

