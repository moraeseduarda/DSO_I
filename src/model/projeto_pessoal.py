from model.status import Status
from model.skill import Skill


class ProjetoPessoal:
    def __init__(self, nome: str, descricao: str, skill_relacionada_obj, status):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("nome deve ser uma string")

        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError("descricao deve ser uma string")

        self.__skill_relacionada = skill_relacionada_obj
        self.__status = status

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
    def skill_relacionada(self):
        return self.__skill_relacionada

    @skill_relacionada.setter
    def skill_relacionada(self, skill_relacionada_obj):
        if isinstance(skill_relacionada_obj, Skill):
            self.__skill_relacionada = skill_relacionada_obj
        else:
            raise TypeError("skill_relacionada_obj deve ser um objeto Skill")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if isinstance(status, Status):
            self.__status = status
        else:
            raise TypeError("status deve ser um objeto Status")

