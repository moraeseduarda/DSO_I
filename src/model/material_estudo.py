class MaterialEstudo:
    def __init__(self, titulo: str, descricao: str, tipo: str):
        if isinstance(titulo, str):
            self.__titulo = titulo

        if isinstance(descricao, str):
            self.__descricao = descricao
        
        if isinstance(tipo, str):
            self.__tipo = tipo

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo: str):
        if isinstance(titulo, str): 
            self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao: str):
        if isinstance(descricao, str):
            self.__descricao = descricao

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo

    def __str__(self):
        return f"{self.__titulo} ({self.__tipo})"