class NivelProficiencia:
    def __init__(self, descricao):
        self.__descricao = descricao
    def __str__(self):
        return self.descricao
    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

NIVEL_BASICO = NivelProficiencia("Básico")
NIVEL_INTERMEDIARIO = NivelProficiencia("Intermediário")
NIVEL_AVANCADO = NivelProficiencia("Avançado")
