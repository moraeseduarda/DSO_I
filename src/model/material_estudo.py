class MaterialEstudo:
    def __init__(self, titulo: str, descricao: str, tipo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo
        else:
            raise TypeError("titulo deve ser uma string")

        if isinstance(descricao, str):
            self.__descricao = descricao
        else:
            raise TypeError("descricao deve ser uma string")
        
        if isinstance(tipo, str):
            self.__tipo = tipo
        else:
            raise TypeError("tipo deve ser uma string")

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str): 
            self.__titulo = titulo
        else:
            raise TypeError("titulo deve ser uma string")

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
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo
        else:
            raise TypeError("tipo deve ser uma string")
