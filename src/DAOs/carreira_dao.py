from DAOs.dao import DAO
from model.carreira import Carreira
import os

#cada entidade terá uma classe dessa, implementação bem simples.
class CarreiraDAO(DAO):
    def __init__(self):
        caminho = os.path.join('DAOs', 'prs', 'carreira.pkl')
        super().__init__(caminho)

    def add(self, carreira: Carreira):
        if((carreira is not None) and isinstance(carreira, Carreira) and isinstance(carreira.id, int)):
            super().add(carreira.id, carreira)

    def update(self, carreira: Carreira):
        if((carreira is not None) and isinstance(carreira, Carreira) and isinstance(carreira.id, int)):
            super().update(carreira.id, carreira)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key, int)):
            return super().remove(key)