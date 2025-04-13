from models.status import Status
from models.skill import Skill

class ProjetosPessoais:
    def __init__(self, nome: str, descricao: str, skill_relacionada_obj, status):
        
        if isinstance(nome, str):
            self.__nome = nome

        if isinstance(descricao, str):
            self.__descricao = descricao

        if isinstance(skill_relacionada_obj, Skill):
            self.__skill_relacionada = skill_relacionada_obj

        if isinstance(status, Status):
            self.__status = status

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def skill_relacionada(self):
        return self.__skill_relacionada

    @skill_relacionada.setter
    def skill_relacionada(self, skill_relacionada_obj):
        if isinstance(skill_relacionada_obj, Skill):
            self.__skill_relacionada = skill_relacionada_obj

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if isinstance(status, Status):
            self.__status = status

    def __str__(self):
        skill_nome = self.__skill_relacionada.nome if self.__skill_relacionada else "Nenhuma"
        return (
            f"Projeto '{self.__nome}': (Associado a Skill: {skill_nome}). "
            f"Descrição: {self.__descricao}. Status: {self.__status.status}"
        )
