from model.skill import Skill

class Carreira:
    """Representa uma carreira profissional."""
    def __init__(self, id: int, nome: str, descricao: str):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__skills_requeridas = []

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise ValueError("A descrição deve ser uma string.")

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

    def adicionar_skill(self, skill):
        """Adiciona uma Skill à lista de skills requeridas."""
        if isinstance(skill, Skill):
            if skill not in self.__skills_requeridas:
                self.__skills_requeridas.append(skill)
            else:
                print(f"A Skill '{skill.nome}' já está associada à carreira {self.nome}.")
        else:
            print(f"Erro: Só é possível adicionar objetos Skill à carreira {self.nome}.")

    def remover_skill(self, skill):
        """Remove uma Skill da lista de skills requeridas."""
        if isinstance(skill, Skill):
            if skill in self.__skills_requeridas:
                self.__skills_requeridas.remove(skill)
            else:
                print(f"A Skill '{skill.nome}' não está associada à carreira {self.nome}.")
        else:
            print(f"Erro: Só é possível remover objetos Skill da carreira {self.nome}.")

    def listar_skills(self):
        """Retorna uma lista com os nomes das skills associadas à carreira."""
        return [skill.nome for skill in self.__skills_requeridas]

    def __str__(self):
        skills = ", ".join(self.listar_skills()) if self.__skills_requeridas else "Nenhuma"
        return (
            f"Carreira: {self.nome} (ID: {self.id})\n"
            f"Descrição: {self.__descricao}\n"
            f"Skills Requeridas: {skills}"
        )
