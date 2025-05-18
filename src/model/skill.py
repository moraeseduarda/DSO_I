from model.material_estudo import MaterialEstudo
from model.nivel_proficiencia import NivelProficiencia

class Skill:
    def __init__(self, nome: str, id: int, descricao: str, material_estudo, nivel_proficiencia):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__material_estudo = material_estudo
        self.__nivel_proficiencia = nivel_proficiencia
            
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
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def material_estudo(self):
        return self.__material_estudo
    
    @material_estudo.setter
    def material_estudo(self, material_estudo):
        if isinstance(material_estudo, list) and all(isinstance(m, MaterialEstudo) for m in material_estudo):
            self.__material_estudo = material_estudo  

    @property
    def nivel_proficiencia(self):
        return self.__nivel_proficiencia
    
    @nivel_proficiencia.setter
    def nivel_proficiencia(self, nivel_proficiencia):
        if isinstance(nivel_proficiencia, NivelProficiencia):
            self.__nivel_proficiencia = nivel_proficiencia

    def adicionar_material(self, material):
        if isinstance(material, MaterialEstudo):
            self.__material_estudo.append(material) 

    def __str__(self):
        materiais = (
            "\n".join(
                f"Título: {material.titulo}, Descrição: {material.descricao}, Tipo: {material.tipo}"
                for material in self.__material_estudo
            )
            if self.__material_estudo
            else "Nenhum"
        )
        return (
            f"Skill: {self.nome} (ID: {self.id}, Nível: {self.__nivel_proficiencia})\n"
            f"Materiais de Estudo:\n{materiais}"
        )
