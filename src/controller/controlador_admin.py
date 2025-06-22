from view.tela_admin_usuarios import TelaAdminUsuario
from view.console_utils import limpar_console


class ControladorAdmin:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_admin_view = TelaAdminUsuario() 

    def autenticar_admin(self):
        """Solicita a palavra-chave do admin antes de liberar o menu."""
        tentativa = self.__tela_admin_view.solicitar_palavra_chave_admin()
        if tentativa == "admin":
            return True
        else:
            self.__tela_admin_view.mostra_mensagem("Palavra-chave incorreta! Retornando ao menu principal.\n")
            return False

    def abre_tela_principal_admin(self): 
        """Abre o menu principal do administrador (Carreiras, Skills, Usuários)."""
        if not self.autenticar_admin():
            return # Sai se não autenticar
        
        opcoes_menu_admin = {
            1: self.__controlador_sistema.controlador_carreira.abre_tela,
            2: self.__controlador_sistema.controlador_skills.abre_tela,
            3: self.abre_tela_gerenciamento_usuarios, 
        }
        while True:
            try:
                opcao_admin = self.__tela_admin_view.tela_opcoes_admin() # Chamada ao método
                if opcao_admin == 0: 
                    limpar_console()
                    break 
                
                funcao_escolhida = opcoes_menu_admin.get(opcao_admin)
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    self.__tela_admin_view.mostra_mensagem("Opção inválida. Tente novamente.")
            except ValueError:
                self.__tela_admin_view.mostra_mensagem("Entrada inválida. Digite apenas números.")

    def abre_tela_gerenciamento_usuarios(self): # Antigo abre_tela, agora focado em usuários
        """Abre o submenu para gerenciamento de usuários (Listar, etc.)."""
        lista_opcoes = {
            1: self.listar_e_mostrar_usuarios, 
        }
        while True:
            opcao = self.__tela_admin_view.tela_opcoes_admin_usuarios()
            if opcao == 0:
                limpar_console()
                break 
            
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_admin_view.mostra_mensagem("Opção inválida. Tente novamente.")

    def listar_e_mostrar_usuarios(self):
        dados_usuarios = self.__controlador_sistema.controlador_usuario.lista_usuarios_dados()
        if not dados_usuarios:
            self.__tela_admin_view.mostra_mensagem("Nenhum usuário cadastrado!")
            return
        
        self.__tela_admin_view.mostra_mensagem("\n--- LISTA DE USUÁRIOS ---")
        for dados_usuario in dados_usuarios:
            self.__tela_admin_view.mostra_usuario(dados_usuario) # mostra_usuario da TelaAdminUsuario

