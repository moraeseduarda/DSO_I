from view.tela_admin import TelaAdmin
from model.admin import Admin


class ControladorAdmin:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_admin_view = TelaAdmin() 
        self.__admin_model = Admin()

    def autenticar_admin(self):
        """Confere se tentativa é igual a palavra-chave do acesso administrativo"""
        tentativa = self.__tela_admin_view.solicitar_palavra_chave_admin()
        if self.__admin_model.autenticar(tentativa):
            return True
        else:
            self.__tela_admin_view.mostra_mensagem("Palavra-chave incorreta! Retornando ao menu principal.\n")
            return False
        
    def mostrar_informacoes_admin(self):
        """Mostra informações admin"""
        info = self.__admin_model.exibir_informacoes()
        self.__tela_admin_view.mostra_mensagem(info)

    def login_e_mostrar_info(self):
        """Faz login do admin, autentica e depois mostra informações do admin"""
        if self.autenticar_admin():
            self.mostrar_informacoes_admin()
            return True
        return False


    def abre_tela_principal_admin(self): 
        """Abre o menu principal do administrador (Carreiras, Skills, Usuários)."""
        if not self.login_e_mostrar_info():
            return # Sai se não autenticar
        
        opcoes_menu_admin = {
            1: self.__controlador_sistema.controlador_carreira.abre_tela,
            2: self.__controlador_sistema.controlador_skills.abre_tela,
            3: self.abre_tela_gerenciamento_usuarios,
        }
        while True:
            try:
                opcao_admin = self.__tela_admin_view.tela_opcoes_admin()
                if opcao_admin == 0:
                    break 
                
                funcao_escolhida = opcoes_menu_admin.get(opcao_admin)
                try:
                    funcao_escolhida()
                except KeyError:
                    self.__tela_admin_view.mostra_mensagem("Opção inválida. Tente novamente.")
            except ValueError:
                self.__tela_admin_view.mostra_mensagem("Entrada inválida. Digite apenas números.")

    def abre_tela_gerenciamento_usuarios(self):
        """Abre o submenu para gerenciamento de usuários (Listar, etc.)."""
        lista_opcoes = {
            1: self.listar_e_mostrar_usuarios, 
        }
        while True:
            opcao = self.__tela_admin_view.tela_opcoes_admin_usuarios()
            if opcao == 0:
                break 
                
            try:
                funcao_escolhida = lista_opcoes.get(opcao)
                try: 
                    funcao_escolhida()
                except KeyError:
                    self.__tela_admin_view.mostra_mensagem("Opção inválida. Tente novamente.")
            except ValueError:
                self.__tela_sistema.mostra_mensagem("Entrada inválida. Digite apenas números.")

    def listar_e_mostrar_usuarios(self):
        """Método de lista usuários cadastrados no sistema, imprime o nome"""
        dados_usuarios = self.__controlador_sistema.controlador_usuario.lista_usuarios_dados()
        if not dados_usuarios:
            self.__tela_admin_view.mostra_mensagem("Nenhum usuário cadastrado!")
            return
        
        self.__tela_admin_view.mostra_mensagem("\n--- LISTA DE USUÁRIOS ---")
        for dados_usuario in dados_usuarios:
            self.__tela_admin_view.mostra_usuario(dados_usuario) # mostra_usuario da TelaAdminUsuario

