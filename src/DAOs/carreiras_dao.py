from DAOs.dao import DAO
from model.carreira import Carreira


class CarreiraDAO(DAO):
    def __init__(self):
        super().__init__('carreira.pkl')

    def add(self, carreira: Carreira):
        if((carreira is not None) and isinstance(carreira, Carreira) and isinstance(carreira.id, int)):
            super().add(carreira.id, carreira)

    def update(self, carreira: Carreira):
        if((carreira is not None) and isinstance(carreira, Carreira) and isinstance(carreira.id, int)):
            super().update(carreira.id, carreira)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)