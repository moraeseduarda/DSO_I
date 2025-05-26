from view.tela_admin_usuarios import TelaAdminUsuario 

class ControladorAdmin:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_admin_view = TelaAdminUsuario() 

    def abre_tela_principal_admin(self): 
        """Abre o menu principal do administrador (Carreiras, Skills, Usuários)."""
        opcoes_menu_admin = {
            1: self.__controlador_sistema.controlador_carreira.abre_tela,
            2: self.__controlador_sistema.controlador_skills.abre_tela,
            3: self.abre_tela_gerenciamento_usuarios, 
            0: self.retornar_ao_menu_sistema 
        }
        while True:
            opcao_admin = self.__tela_admin_view.tela_opcoes_admin() # Chamada ao método
            if opcao_admin == 0: 
                break 
            
            funcao_escolhida = opcoes_menu_admin.get(opcao_admin)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_admin_view.mostra_mensagem("Opção inválida. Tente novamente.")

    def abre_tela_gerenciamento_usuarios(self): # Antigo abre_tela, agora focado em usuários
        """Abre o submenu para gerenciamento de usuários (Listar, etc.)."""
        lista_opcoes = {
            1: self.listar_e_mostrar_usuarios, 
            0: self.retornar_ao_menu_admin_principal 
        }
        while True:
            opcao = self.__tela_admin_view.tela_opcoes_admin_usuarios()
            if opcao == 0:
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
        input("\nPressione ENTER para continuar...")


    def retornar_ao_menu_admin_principal(self):
        pass

    def retornar_ao_menu_sistema(self):
        pass