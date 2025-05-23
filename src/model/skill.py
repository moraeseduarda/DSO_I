from model.material_estudo import MaterialEstudo
from model.nivel_proficiencia import NivelProficiencia

class Skill:
    def __init__(self, nome: str, id: int, descricao: str, material_estudo=None, nivel_proficiencia=None):
        if isinstance(id, int):
            self.__id = id
        else:
            raise TypeError("id deve ser um inteiro")

        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("nome deve ser uma string")

        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError("descricao deve ser uma string")

        self.__material_estudo = material_estudo if material_estudo is not None else []
        self.__nivel_proficiencia = nivel_proficiencia
        self.__carreiras = []

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
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError("descricao deve ser uma string")

    @property
    def material_estudo(self):
        return self.__material_estudo

    @material_estudo.setter
    def material_estudo(self, material_estudo):
        if isinstance(material_estudo, list) and all(isinstance(m, MaterialEstudo) for m in material_estudo):
            self.__material_estudo = material_estudo
        else:
            raise TypeError("material_estudo deve ser uma lista de objetos MaterialEstudo")

    def adicionar_material_estudo(self, material):
        if isinstance(material, MaterialEstudo):
            self.__material_estudo.append(material)
        else:
            raise TypeError("material deve ser um objeto MaterialEstudo")

    def remover_material_estudo(self, material):
        if material in self.__material_estudo:
            self.__material_estudo.remove(material)

    @property
    def nivel_proficiencia(self):
        return self.__nivel_proficiencia

    @nivel_proficiencia.setter
    def nivel_proficiencia(self, nivel_proficiencia):
        if isinstance(nivel_proficiencia, NivelProficiencia) or nivel_proficiencia is None:
            self.__nivel_proficiencia = nivel_proficiencia
        else:
            raise TypeError("nivel_proficiencia deve ser um objeto NivelProficiencia")

    @property
    def carreiras(self):
        return self.__carreiras

    def adicionar_carreira(self, carreira):
        if carreira not in self.__carreiras:
            self.__carreiras.append(carreira)

    def remover_carreira(self, carreira):
        if carreira in self.__carreiras:
            self.__carreiras.remove(carreira)
