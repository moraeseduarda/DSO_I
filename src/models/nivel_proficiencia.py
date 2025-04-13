class NivelProficiencia:
    def __init__(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    def __str__(self):
        return self.descricao
