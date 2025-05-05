from view.tela_sistema import TelaSistema
from controller.controlador_carreira import ControladorCarreira

class ControladorSistema:
    def __init__(self):
        self.controlador__carreira = ControladorCarreira(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_carreira(self):
        return self.controlador__carreira
    
    def cadastra_carreira(self):
        self.controlador__carreira.abre_tela()
    
    def encerra_sistema(self):
        exit(0)
    
    def abre_tela(self):
        opcoes = {1: self.cadastra_carreira, 0: self.encerra_sistema}
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = opcoes[opcao_escolhida]  
            funcao_escolhida()
