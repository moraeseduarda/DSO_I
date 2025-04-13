class Status:
    def __init__(self, status: str):
        if isinstance(status, str):
          self.__status = status

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status: str):
        if isinstance(status, str):
          self.__status = status

# Instâncias globais de Status
STATUS_NAO_INICIADO = Status("Não Iniciado")
STATUS_EM_PROGRESSO = Status("Em Progresso")
STATUS_CONCLUIDO = Status("Concluído")