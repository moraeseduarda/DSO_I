class Carreira:
    def __init__(self, id: int, nome: str, descricao: str):
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
        
        self.__skills_requeridas = []

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
    def skills_requeridas(self):
        return self.__skills_requeridas

    def adicionar_skill(self, skill):
        """Adiciona uma skill à lista de skills requeridas da carreira."""
        if skill not in self.__skills_requeridas:
            self.__skills_requeridas.append(skill)

    def remover_skill(self, skill):
        """Remove uma skill da lista de skills requeridas da carreira."""
        if skill in self.__skills_requeridas:
            self.__skills_requeridas.remove(skill)