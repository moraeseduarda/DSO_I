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