from view.tela_admin_usuarios import TelaAdminUsuario
from view.tela_menu_usuario import TelaMenuUsuario
from model.usuario import Usuario
from model.projeto_pessoal import ProjetoPessoal
from model.status import Status
from view.console_utils import limpar_console

class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_menu_usuario = TelaMenuUsuario()
        self.__usuarios = []
    
    @property
    def usuarios(self):
        return self.__usuarios

    # Métodos gerais  
    def pega_usuario_por_username(self, palavra_chave: str):
        for usuario in self.__usuarios:
            if usuario.palavra_chave == palavra_chave:
                return usuario
        return None
           
    # O método lista_usuarios pode ser chamado pelo ControladorAdmin.
    # Se a exibição for feita pela TelaAdminUsuario, o ControladorAdmin pode chamar este método
    def lista_usuarios_dados(self):
        if not self.__usuarios:
            return [] # Retorna lista vazia para o ControladorAdmin tratar
        
        dados_usuarios = []
        for usuario in self.__usuarios:
            dados_usuarios.append({
                'username': usuario.palavra_chave, 
                'nome': usuario.nome, 
                'carreiras': [carreira.nome for carreira in usuario.carreiras], # Ajuste conforme necessário
                'skills_aprendidas': [skill.nome for skill in usuario.skills_aprendidas] # Ajuste
            })
        return dados_usuarios

   
    def cadastrar_usuario(self):
        dados_usuario = self.__tela_menu_usuario.pega_dados_cadastro_usuario()
        usuario = self.pega_usuario_por_username(dados_usuario['username'])

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
                    
            novo_usuario = Usuario(dados_usuario['username'], dados_usuario['nome'], carreiras_escolhidas , [])
            self.__usuarios.append(novo_usuario)
            self.__tela_menu_usuario.mostra_mensagem('Usuário cadastrada com sucesso!')
        else:
            self.__tela_menu_usuario.mostra_mensagem("ATENCAO: Usuário com esse USERNAME já existe. Cadastre novamente, com outro USERNAME.")    
    
    def usuario_retornar(self):
        print('Saindo do menu usuário...\n')
        
    def abre_tela_usuario(self):
        lista_opcoes = {
            1: self.cadastrar_usuario, 
            2: self.login_usuario, 
            3: self.ranking
        }
        
        while True:
            try:
                opcao = self.__tela_menu_usuario.tela_opcoes()
                if opcao == 0:
                    self.usuario_retornar()
                    break

                funcao_escolhida = lista_opcoes.get(opcao)
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    self.__tela_menu_usuario.mostra_mensagem("Opção inválida. Digite um número entre 0 e 3.")
            except ValueError:
                limpar_console()
                print("Entrada inválida. Digite apenas números.")

            
            
    def ranking(self):
        print("\n--- RANKING DE APRENDIZADO ---")
        print("---------------------------------")
        print(f"{'Posição':<10}{'Usuário':<20}{'Número de Skills aprendidas'}")
        print("---------------------------------")

        ranking_usuarios = [
            (usuario.palavra_chave, len(usuario.skills_aprendidas))
            for usuario in self.__usuarios
        ]

        ranking_usuarios.sort(key=lambda x: x[1], reverse=True)

        for posicao, (username, qtd_skills) in enumerate(ranking_usuarios, start=1):
            print(f"{posicao:<10}{username:<20}{qtd_skills}")

        print("---------------------------------\n")
    
        
    def login_usuario(self):
        print("===== LOGIN DE USUÁRIO =====")
        tentativas = 0
        usuario = None # Inicializa usuario
        while True:
            try:
                username_usuario = input("Digite seu USERNAME para entrar: @").strip().lower()
                if not username_usuario: # Verifica se a entrada é vazia
                    print("Username não pode ser vazio. Tente novamente.\n")
                    continue
            except ValueError: # Embora input() retorne string, é boa prática manter
                print("Valor inválido.\n")
                continue

            usuario = self.pega_usuario_por_username(username_usuario)
            if usuario is None:
                tentativas += 1
                print(f"Usuário não encontrado. Tente novamente. ({tentativas}/3 tentativas)\n")
                if tentativas >= 3:
                    print("Muitas tentativas inválidas. Retornando...\n")
                    return  # Volta para o menu de abre_tela_usuario
            else:
                break # Usuário encontrado, sai do loop de tentativa de login

        # Loop do menu do usuário logado
        while True:
            print('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')
            print(f"\n--- Bem-vindo(a), {usuario.nome}! ---")
            print("1 - Ver informações do usuário e carreiras escolhidas")
            print("2 - Ver percentual concluído")
            print("3 - Aprender skill")
            print("4 - Gerenciar projetos pessoais")
            print("0 - Sair (Deslogar)") 

            opcao = input("Digite a opção desejada: ").strip()
            limpar_console()

            if opcao == '1':
                self.mostra_info_carreira(usuario)
            elif opcao == '2':
                self.mostra_percentual_concluido(usuario)
            elif opcao == '3':
                self.aprender_skill(usuario)
            elif opcao == '4':
                self.menu_projetos_pessoais(usuario)
            elif opcao == '0':
                print(f"Deslogando usuário {usuario.nome}...\n")
                return # Termina o método login_usuario, voltando para o loop de abre_tela_usuario
            else:
                limpar_console()
                print("Opção inválida. Tente novamente.\n")

    def menu_projetos_pessoais(self, usuario):
        while True:
            print("\n--- GERENCIAR PROJETOS PESSOAIS ---")
            print("1 - Adicionar projeto pessoal")
            print("2 - Ver projetos pessoais")
            print("3 - Alterar projeto pessoal")
            print("4 - Excluir projeto pessoal")
            print("5 - Concluir projeto pessoal")
            print("0 - Voltar ao menu anterior")

            opcao = input("Escolha uma opção: ").strip()
            limpar_console()

            if opcao == '1':
                self.adicionar_projeto_pessoal(usuario)
            elif opcao == '2':
                self.listar_projetos_pessoais(usuario)
            elif opcao == '3':
                self.alterar_projeto_pessoal(usuario)
            elif opcao == '4':
                self.excluir_projeto_pessoal(usuario)
            elif opcao == '5':
                self.concluir_projeto_pessoal(usuario)
            elif opcao == '0':
                break
            else:
                print("Opção inválida. Tente novamente.")


    def mostra_info_carreira(self, usuario):
        print("---- Informações do Usuário ----")
        print(f"Nome: {usuario.nome}")
        print(f"Username: @{usuario.palavra_chave}")
        
        if not usuario.carreiras:
            print("Usuário não está associado a nenhuma carreira.\n")
            return
        
        print("--- INFORMAÇÕES DAS CARREIRAS ESCOLHIDAS PELO USUÁRIO")
        for carreira in usuario.carreiras:
            print(f"\nCarreira Escolhida: {carreira.nome}")
            print(f"Descrição: {carreira.descricao}")
            skills_nomes = [skill.nome for skill in carreira.skills_requeridas]
            print(f"Skills da Carreira: {', '.join(skills_nomes) if skills_nomes else 'Nenhuma skill cadastrada.'}\n")

    def mostra_percentual_concluido(self, usuario):
        if not usuario.carreiras:
            print("Usuário não está associado a nenhuma carreira.\n")
            return
        
        for carreira in usuario.carreiras:
            if not carreira.skills_requeridas:
                print(f"A carreira {carreira.nome} não possui skills cadastradas.\n")
                continue

            # Filtra as skills aprendidas e para aprender relacionadas à carreira
            aprendidas = [s for s in usuario.skills_aprendidas if s in carreira.skills_requeridas]
            para_aprender = [s for s in carreira.skills_requeridas if s not in usuario.skills_aprendidas]

            total = len(carreira.skills_requeridas)
            concluidas = len(aprendidas)
            percentual = (concluidas / total) * 100 if total > 0 else 0

            print("\n--- Skills já aprendidas ---")
            if aprendidas:
                for idx, skill in enumerate(aprendidas, start=1):
                    print(f"{idx}. {skill.nome}")
            else:
                print("Nenhuma skill aprendida ainda.")

            print(f"\nPercentual concluído na carreira {carreira.nome}: {percentual:.2f}%\n")

            print("\n--- Skills disponíveis para aprender ---")
            if para_aprender:
                for idx, skill in enumerate(para_aprender, start=1):
                    print(f"{idx}. {skill.nome}")
            else:
                print("Nenhuma skill disponível para aprender.\n")
            print("-------\n")

    def listar_projetos_pessoais(self, usuario: Usuario):
        print("\n--- Projetos Pessoais do Usuário ---")
        # O getter usuario.projetos_pessoais retorna uma lista de objetos ProjetoPessoal
        projetos_do_usuario = usuario.projetos_pessoais
        if not projetos_do_usuario:
            print("Nenhum projeto pessoal cadastrado.\n")
            return
        for projeto in projetos_do_usuario:
            print(f"Nome: {projeto.nome}")
            print(f"Descrição: {projeto.descricao}")
            print(f"Status: {projeto.status.status if hasattr(projeto.status, 'status') else projeto.status}") # Lida com Status obj ou string
            print("-" * 30)

    def adicionar_projeto_pessoal(self, usuario: Usuario):
        print("\n--- Adicionar Novo Projeto Pessoal ---")
        nome = input("Nome do projeto: ").strip()
        if not nome:
            print("Nome do projeto não pode ser vazio.")
            return
        
        descricao = input("Descrição do projeto: ").strip()
        status_str = input("Status inicial do projeto (ex: A_FAZER, EM_ANDAMENTO, CONCLUIDO): ").strip().upper()

        # Validação do nome do projeto (para evitar duplicatas)
        lista_projetos_atual = usuario.projetos_pessoais # GETTER
        if any(p.nome == nome for p in lista_projetos_atual):
            print(f"Erro: Um projeto com o nome '{nome}' já existe.")
            return

        try:
            status_obj = Status(status_str) # Assume que Status pode ser instanciado com a string
        except ValueError as e: # Se Status() levantar erro para valor inválido
            print(f"Erro no status: {e}")
            return

        novo_projeto = ProjetoPessoal(nome, descricao, status_obj)
        lista_projetos_atual.append(novo_projeto)
        usuario.projetos_pessoais = lista_projetos_atual # SETTER
        print("Projeto pessoal adicionado com sucesso!\n")

    def alterar_projeto_pessoal(self, usuario: Usuario):
        print("\n--- Alterar Projeto Pessoal ---")
        nome_antigo = input("Nome do projeto a ser alterado: ").strip()

        lista_projetos_atual = usuario.projetos_pessoais # GETTER
        projeto_para_alterar = usuario._encontrar_projeto_na_lista(lista_projetos_atual, nome_antigo) # Helper opcional

        if not projeto_para_alterar:
            print(f"Projeto '{nome_antigo}' não encontrado.")
            return

        print(f"Alterando projeto: {projeto_para_alterar.nome}")
        novo_nome = input(f"Novo nome (deixe em branco para manter '{projeto_para_alterar.nome}'): ").strip()
        nova_descricao = input(f"Nova descrição (deixe em branco para manter): ").strip()
        novo_status_str = input(f"Novo status (deixe em branco para manter '{projeto_para_alterar.status.status if hasattr(projeto_para_alterar.status, 'status') else projeto_para_alterar.status}'): ").strip().upper()

        nome_final = novo_nome if novo_nome else projeto_para_alterar.nome

        
        if novo_nome and novo_nome != nome_antigo:
            if any(p.nome == novo_nome for p in lista_projetos_atual if p.nome != nome_antigo):
                print(f"Erro: Já existe um projeto com o nome '{novo_nome}'. Alteração de nome cancelada.")
                novo_nome = "" 
                nome_final = nome_antigo

        
        if novo_nome and novo_nome != nome_antigo: 
            projeto_para_alterar.nome = novo_nome
        if nova_descricao:
            projeto_para_alterar.descricao = nova_descricao
        if novo_status_str:
            try:
                projeto_para_alterar.status = Status(novo_status_str)
            except ValueError as e:
                print(f"Erro no novo status: {e}. Status não alterado.")
        
    
        usuario.projetos_pessoais = lista_projetos_atual 
        print(f"Projeto '{nome_final}' atualizado com sucesso!\n")


    def excluir_projeto_pessoal(self, usuario: Usuario):
        print("\n--- Excluir Projeto Pessoal ---")
        nome_projeto = input("Nome do projeto a ser excluído: ").strip()

        lista_projetos_atual = usuario.projetos_pessoais 
        projeto_para_excluir = usuario._encontrar_projeto_na_lista(lista_projetos_atual, nome_projeto)

        if not projeto_para_excluir:
            print(f"Projeto '{nome_projeto}' não encontrado.")
            return

        lista_projetos_atual.remove(projeto_para_excluir)
        usuario.projetos_pessoais = lista_projetos_atual 
        print(f"Projeto '{nome_projeto}' excluído com sucesso!\n")

    def concluir_projeto_pessoal(self, usuario: Usuario):
        print("\n--- Concluir Projeto Pessoal ---")
        # Filtra apenas projetos que NÃO estão concluídos
        projetos_nao_concluidos = [p for p in usuario.projetos_pessoais if p.status.status != "CONCLUIDO"]

        if not projetos_nao_concluidos:
            print("Nenhum projeto pessoal pendente para concluir.\n")
            return

        print("Projetos pessoais pendentes:")
        for projeto in projetos_nao_concluidos:
            print(f"Nome: {projeto.nome}")
            print(f"Descrição: {projeto.descricao}")
            print(f"Status: {projeto.status.status}")
            print("-" * 30)

        nome_projeto = input("Nome do projeto a ser concluído: ").strip()
        projeto_para_concluir = next((p for p in projetos_nao_concluidos if p.nome == nome_projeto), None)

        if not projeto_para_concluir:
            print(f"Projeto '{nome_projeto}' não encontrado ou já está concluído.")
            return

        try:
            projeto_para_concluir.status = Status("CONCLUIDO")
        except ValueError as e:
            print(f"Erro ao definir status como CONCLUIDO: {e}")
            return

        usuario.projetos_pessoais = usuario.projetos_pessoais  # Atualiza a lista, se necessário
        print(f"Projeto '{nome_projeto}' marcado como CONCLUÍDO!\n")

    def aprender_skill(self, usuario):
        if not usuario.carreiras:
            print("Usuário não está associado a nenhuma carreira.\n")
            return

        # Mostrar todas as skills disponíveis nas carreiras do usuário
        skills_disponiveis = []
        for carreira in usuario.carreiras:
            for skill in carreira.skills_requeridas:
                if skill not in usuario.skills_aprendidas and skill not in skills_disponiveis:
                    skills_disponiveis.append(skill)
                    print(f"ID: {skill.id} - Nome: {skill.nome}")

        if not skills_disponiveis:
            print("Não há skills disponíveis para aprender.\n")
            return

        # Selecionar skill para aprender
        while True:
            try:
                id_skill = int(input("\nDigite o ID da skill que deseja aprender: "))
                skill_selecionada = next((skill for skill in skills_disponiveis if skill.id == id_skill), None)
                if skill_selecionada:
                    break
                print("ID inválido. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

        # Adicionar à lista de skills aprendidas
        usuario.skills_aprendidas.append(skill_selecionada)
        # Remover da lista de skills para aprender se estiver lá
        if skill_selecionada in usuario.skills_para_aprender:
            usuario.skills_para_aprender.remove(skill_selecionada)
        
        print(f"\nParabéns! Você aprendeu a skill: {skill_selecionada.nome}")