class Status:
    def __init__(self, status: str):
        if isinstance(status, str):
          self.__status = status
        else:
            raise TypeError("status deve ser uma string")

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status: str):
        if isinstance(status, str):
          self.__status = status
        else:
            raise TypeError("status deve ser uma string")
