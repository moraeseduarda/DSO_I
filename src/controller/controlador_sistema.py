from view.tela_sistema import TelaSistema
from controller.controlador_carreira import ControladorCarreira
from controller.controlador_usuario import ControladorUsuario

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_carreira = ControladorCarreira(self)
        self.__controlador_usuario = ControladorUsuario(self)
    
    @property
    def controlador_carreira(self):
        return self.__controlador_carreira
    
    @property
    def controlador_usuario(self):
        return self.__controlador_usuario
    
    def cadastra_carreira(self):
        self.__controlador_carreira.abre_tela()
    
    def cadastra_usuario(self):
        self.__controlador_usuario.abre_tela()
    
    def encerra_sistema(self):
        exit(0)
    
    def abre_tela(self):
        opcoes = {2: self.cadastra_usuario, 1: self.cadastra_carreira, 0: self.encerra_sistema}
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = opcoes[opcao_escolhida]  
            funcao_escolhida()
