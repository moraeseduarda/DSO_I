from model.status import Status


class ProjetoPessoal:
    def __init__(self, nome: str, descricao: str, status):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("nome deve ser uma string")

        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError("descricao deve ser uma string")

        if isinstance(status, Status):
            self.__status = status
        else:
            raise TypeError("status deve ser um objeto Status")

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
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError("descricao deve ser uma string")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if isinstance(status, Status):
            self.__status = status
        else:
            raise TypeError("status deve ser um objeto Status")
