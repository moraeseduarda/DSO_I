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

    def menu_administrador(self):
        opcoes = {
            1: self.__controlador_carreira.abre_tela,
            2: self.__controlador_skills.abre_tela,
            3: self.__controlador_usuario.abre_tela_admin,
        }
        
        while True:
                opcao = self.__tela_sistema.tela_opcoes_admin()
                if opcao == 0:
                    self.abre_tela()
                funcao = opcoes.get(opcao)
                if funcao:
                    funcao()
                else:
                    print("Opção inválida.")
    
    def encerra_sistema(self):
        exit(0)
    
    def abre_tela(self):
        while True:
            opcoes = {
                0: self.encerra_sistema,
                1: self.menu_administrador,
                2: self.controlador_usuario.abre_tela_usuario,
            }

            escolha = self.__tela_sistema.tela_opcoes_iniciais()
            funcao = opcoes.get(escolha)

            if funcao:
                funcao()
            else:
                print("Opção inválida.")
