from view.tela_admin_usuarios import TelaAdminUsuario
from view.tela_menu_usuario import TelaMenuUsuario

class ControladorUsuario():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_admin_usuario = TelaAdminUsuario()
        self.__tela_menu_usuario = TelaMenuUsuario()
        self.__usuarios = []
                
    def lista_usuarios(self):
        if not self.__usuarios:
            print('Nenhum usuário cadastrado.\n')
        else:
            for usuario in self.__usuarios:
                self.__tela_admin_usuario.mostra_usuario({'id': usuario.id, 'nome': usuario.nome})
                
    def cadastrar_usuario(self):
        pass
    
    def acessar_usuario(self):
        pass
    
    def menu_usuario(self):
        opcoes = {
            1: self.cadastrar_usuario,
            2: self.acessar_usuario,
        }

        while True:
            opcao = self.__tela_menu_usuario.tela_opcoes()
            if opcao == 0:
                break
            funcao = opcoes.get(opcao)
            if funcao:
                funcao()
            else:
                print("Opção inválida.")
            
    def retornar(self):
        print('Saindo do menu de administração de usuários...\n')
        self.__controlador_sistema.abre_tela() 
        
    def abre_tela(self):
        lista_opcoes = {1: self.lista_usuarios, 0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_admin_usuario.tela_opcoes()]()
