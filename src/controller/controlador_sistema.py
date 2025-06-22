from view.tela_sistema import TelaSistema
from view.console_utils import limpar_console
from controller.controlador_carreira import ControladorCarreira
from controller.controlador_usuario import ControladorUsuario
from controller.controlador_skills import ControladorSkill
from controller.controlador_admin import ControladorAdmin 


class ControladorSistema:

    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_carreira = ControladorCarreira(self)
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_skills = ControladorSkill(self)
        self.__controlador_admin = ControladorAdmin(self) 
    
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
    def controlador_admin(self):
        return self.__controlador_admin

    def encerra_sistema(self):
        exit(0)
    
    def abre_tela(self):
        while True:
            opcoes = {
                1: self.controlador_admin.abre_tela_principal_admin, 
                2: self.controlador_usuario.abre_tela_usuario,
                0: self.encerra_sistema,
            }
            try:
                escolha = self.__tela_sistema.tela_opcoes_iniciais()
                try:
                    funcao = opcoes[escolha]
                    funcao()
                except KeyError:
                    self.__tela_sistema.mostra_mensagem("Opção inválida. Escolha 0, 1 ou 2.")
            except ValueError:
                limpar_console()
                self.__tela_sistema.mostra_mensagem("Entrada inválida. Digite apenas números.")