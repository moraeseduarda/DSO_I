from view.tela_admin_usuarios import TelaAdminUsuario
from view.tela_menu_usuario import TelaMenuUsuario
from model.usuario import Usuario

class ControladorUsuario():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_admin_usuario = TelaAdminUsuario()
        self.__tela_menu_usuario = TelaMenuUsuario()
        self.__usuarios = []
        
    def pega_usuario_por_id(self, id: int):
        for usuario in self.__usuarios:
            if usuario.id == id:
                return usuario
        return None
    
    # Métodos usado em Tela Admin Usuários            
    def lista_usuarios(self):
        if not self.__usuarios:
            print('Nenhum usuário cadastrado.\n')
        else:
            for usuario in self.__usuarios:
                self.__tela_admin_usuario.mostra_usuario({'id': usuario.id, 'nome': usuario.nome})


    def abre_tela_admin(self):
        lista_opcoes = {1: self.lista_usuarios, 0: self.admin_retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_admin_usuario.tela_opcoes()]()
     
    def admin_retornar(self):
        print('Saindo do menu de administração de usuários...\n')
        self.__controlador_sistema.abre_tela() 

    # Métodos usados em Tela do Usuário       
    def cadastrar_usuario(self):
        dados_usuario = self.__tela_menu_usuario.pega_dados_cadastro_usuario()
        usuario = self.pega_usuario_por_id(dados_usuario['id'])

        # Não há nenhum usuário com esse id cadastrado anteriormente, logo pode-se avançar no processo de cadastro
        if usuario is None:
            # Carreira como None pq não temos esse cadastro ainda
            novo_usuario = Usuario(dados_usuario['id'], dados_usuario['nome'], None)
            self.__usuarios.append(novo_usuario)
            self.__tela_menu_usuario.mostra_mensagem('Usuário cadastrada com sucesso!')
        else:
            self.__tela_menu_usuario.mostra_mensagem("ATENCAO: Usuário com esse ID já existe. Cadastre novamente, com outro ID.")    
        
    def login_usuario(self):
        pass
    
    def seleciona_carreira(self):
        pass
    
    # Display de telas do menu do usuário
    def abre_tela_usuario(self):
        lista_opcoes = {1: self.cadastrar_usuario, 2: self.login_usuario, 0: self.usuario_retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_menu_usuario.tela_opcoes()]()
            
    def usuario_retornar(self):
        print('Saindo do menu principal...\n')
        self.__controlador_sistema.abre_tela() 