from model.material_estudo import MaterialEstudo
from model.nivel_proficiencia import NivelProficiencia


class Skill:
    def __init__(self, nome: str, id: int, descricao: str, material_estudo, nivel_proficiencia):
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

        self.__material_estudo = material_estudo
        self.__nivel_proficiencia = nivel_proficiencia
            
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

    @property
    def nivel_proficiencia(self):
        return self.__nivel_proficiencia
    
    @nivel_proficiencia.setter
    def nivel_proficiencia(self, nivel_proficiencia):
        if isinstance(nivel_proficiencia, NivelProficiencia):
            self.__nivel_proficiencia = nivel_proficiencia
        else:
            raise TypeError("nivel_proficiencia deve ser um objeto NivelProficiencia")
