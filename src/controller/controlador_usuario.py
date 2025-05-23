from view.tela_admin_usuarios import TelaAdminUsuario
from view.tela_menu_usuario import TelaMenuUsuario
from model.usuario import Usuario

class ControladorUsuario():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_admin_usuario = TelaAdminUsuario()
        self.__tela_menu_usuario = TelaMenuUsuario()
        self.__usuarios = []
    
    # Métodos gerais  
    def pega_usuario_por_username(self, username: str):
        for usuario in self.__usuarios:
            if usuario.username == username:
                return usuario
        return None
    
    # Métodos usado em Tela Admin Usuários            
    def lista_usuarios(self):
        if not self.__usuarios:
            print('Nenhum usuário cadastrado.\n')
        else:
            for usuario in self.__usuarios:
                self.__tela_admin_usuario.mostra_usuario({'username': usuario.username, 'nome': usuario.nome, 'carreira': [carreira.nome for carreira in usuario.carreiras]})

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
        usuario = self.pega_usuario_por_username(dados_usuario['username'])

        # Não há nenhum usuário com esse username cadastrado anteriormente, logo pode avançar no processo de cadastro.
        if usuario is None:
            controlador_carreira = self.__controlador_sistema.controlador_carreira
            carreiras_disponiveis = controlador_carreira.carreiras

            if not carreiras_disponiveis:
                self.__tela_menu_usuario.mostra_mensagem("Nenhuma carreira cadastrada. Não é possível cadastrar o usuário sem ao menos uma carreira.")
                return
            controlador_carreira.lista_carreira()
            ids_carreiras = self.__tela_menu_usuario.seleciona_carreiras(carreiras_disponiveis)

             # Buscar objetos Carreira válidos (sem duplicatas)
            carreiras_escolhidas = []
            for id_carreira in ids_carreiras:
                carreira = controlador_carreira.pega_carreira_por_id(id_carreira)
                if carreira and carreira not in carreiras_escolhidas:
                    carreiras_escolhidas.append(carreira)

            novo_usuario = Usuario(dados_usuario['username'], dados_usuario['nome'], carreiras_escolhidas)
            self.__usuarios.append(novo_usuario)
            self.__tela_menu_usuario.mostra_mensagem('Usuário cadastrada com sucesso!')
        else:
            self.__tela_menu_usuario.mostra_mensagem("ATENCAO: Usuário com esse USERNAME já existe. Cadastre novamente, com outro USERNAME.")    
    
    def abre_tela_usuario(self):
        lista_opcoes = {1: self.cadastrar_usuario, 2: self.login_usuario, 0: self.usuario_retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_menu_usuario.tela_opcoes()]()
            
    def usuario_retornar(self):
        print('Saindo do menu usuário...\n')
        self.__controlador_sistema.menu_administrador() 
        
    def login_usuario(self):
        print("===== LOGIN DE USUÁRIO =====")
        while True:
            try:
                username_usuario = input("Digite seu USERNAME para entrar: @").strip().lower()
            except ValueError:
                print("Valor inválido.\n")
                continue

            usuario = self.pega_usuario_por_username(username_usuario)
            if usuario is None:
                print("Usuário não encontrado. Tente novamente.\n")
            else:
                break
        
        print(f"\n--- Bem-vindo(a), {usuario.nome}! ---")

        while True:
            print("1 - Ver informações da carreira")
            print("2 - Ver mapa de aprendizado")
            print("3 - Ver percentual concluído")
            print("4 - Aprender skill")
            print("0 - Sair")

            opcao = input("Digite a opção desejada: ").strip()

            if opcao == '1':
                self.mostra_info_carreira(usuario)
            elif opcao == '2':
                self.mostra_mapa_aprendizado(usuario)
            elif opcao == '3':
                self.mostra_percentual_concluido(usuario)
            elif opcao == '4':
                pass
            elif opcao == '0':
                print("Retornando ao menu principal...\n")
                break
            else:
                print("Opção inválida. Tente novamente.\n")

    def mostra_info_carreira(self, usuario):
        if not usuario.carreiras:
            print("Usuário não está associado a nenhuma carreira.\n")
            return
        
        # Para simplificar, mostra todas as carreiras do usuário
        for carreira in usuario.carreiras:
            print(f"\nCarreira Escolhida: {carreira.nome}")
            print(f"Descrição: {carreira.descricao}")
            skills_nomes = [skill.nome for skill in getattr(carreira, 'skills', [])]
            print(f"Skills da Carreira: {skills_nomes if skills_nomes else 'Nenhuma skill cadastrada.'}\n")

    def mostra_mapa_aprendizado(self, usuario):
        if not usuario.carreiras:
            print("Usuário não está associado a nenhuma carreira.\n")
            return
        
        # Para simplificar, mostra skills e status de todas as carreiras
        for carreira in usuario.carreiras:
            print(f"\nMapa de aprendizado para a carreira: {carreira.nome}")
            if not hasattr(carreira, 'skills') or not carreira.skills:
                print("Nenhuma skill cadastrada para esta carreira.\n")
                continue

            for skill in carreira.skills:
                # Presumindo que Usuario tem métodos status_skill e nivel_skill, ou pode-se adaptar
                status = getattr(usuario, 'status_skill', lambda s: "Status desconhecido")(skill)
                nivel = getattr(usuario, 'nivel_skill', lambda s: "Nível desconhecido")(skill)
                print(f"Skill: {skill.nome}, Status: {status}, Nível: {nivel}")
            print()

    def mostra_percentual_concluido(self, usuario):
        if not usuario.carreiras:
            print("Usuário não está associado a nenhuma carreira.\n")
            return
        
        for carreira in usuario.carreiras:
            if not hasattr(carreira, 'skills') or not carreira.skills:
                print(f"A carreira {carreira.nome} não possui skills cadastradas.\n")
                continue
            
            total = len(carreira.skills)
            concluidas = 0
            for skill in carreira.skills:
                status = getattr(usuario, 'status_skill', lambda s: "Status desconhecido")(skill)
                if status == "Concluído":
                    concluidas += 1
            
            percentual = (concluidas / total) * 100 if total > 0 else 0
            print(f"\nPercentual concluído na carreira {carreira.nome}: {percentual:.2f}%\n")

