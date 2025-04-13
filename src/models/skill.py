from models.material_estudo import MaterialEstudo
from models.nivel_proficiencia import NivelProficiencia
from models.modelo_cadastro import ModeloCadastro

class Skill(ModeloCadastro):
    def __init__(self, nome: str, id: int, descricao: str, material_estudo, nivel_proficiencia):
        super().__init__(nome, id) 

        if isinstance(descricao, str):
            self.__descricao = descricao
  
        if isinstance(material_estudo, list) and all(isinstance(m, MaterialEstudo) for m in material_estudo):
            self.__material_estudo = material_estudo

        if isinstance(nivel_proficiencia, NivelProficiencia):
            self.__nivel_proficiencia = nivel_proficiencia

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
    