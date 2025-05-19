from view.tela_sistema import TelaSistema
from controller.controlador_carreira import ControladorCarreira
from controller.controlador_usuario import ControladorUsuario
from controller.controlador_skills import ControladorSkill

class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_carreira = ControladorCarreira(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_skills = ControladorSkill(self)
    
    @property
    def controlador_carreira(self):
        return self.__controlador_carreira
    
    @property
    def controlador_usuario(self):
        return self.__controlador_usuario
    
    @property
    def controlador_skills(self):
        return self.__controlador_skills
    
    @property
    def controlador_skills(self):
        return self.__controlador_skills
    
    def cadastra_carreira(self):
        self.__controlador_carreira.abre_tela()
    
    def cadastra_usuario(self):
        self.__controlador_usuario.abre_tela()
    
    def cadastra_skill(self):
        self.controlador_skills.abre_tela()
    
    def cadastra_skill(self):
        self.controlador_skills.abre_tela()
    
    def encerra_sistema(self):
        exit(0)
    
    def abre_tela(self):
        opcoes = {3: self.cadastra_usuario, 1: self.cadastra_carreira, 0: self.encerra_sistema, 2:self.cadastra_skill}
        
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = opcoes[opcao_escolhida]  
            funcao_escolhida()
