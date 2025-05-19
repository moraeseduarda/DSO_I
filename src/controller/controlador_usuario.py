from model.skill import Skill
from view.tela_usuario import TelaUsuario

class ControladorUsuario():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_usuario = TelaUsuario()
        self.__usuarios = []
        
    def pega_usuario_por_id(self, id: int):
        for usuario in self.__usuarios:
            if usuario.id == id:
                return usuario
        return None
    
    
    
    