from DAOs.dao import DAO
from model.usuario import Usuario


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuario.pkl')

    def add(self, usuario: Usuario):
        if((usuario is not None) and isinstance(usuario, Usuario) and isinstance(usuario.username, int)):
            super().add(usuario.username, usuario)

    def update(self, usuario: Usuario):
        if((usuario is not None) and isinstance(usuario, Usuario) and isinstance(usuario.username, int)):
            super().update(usuario.username, usuario)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)