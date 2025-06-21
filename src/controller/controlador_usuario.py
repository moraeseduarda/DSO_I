from view.tela_menu_usuario import TelaMenuUsuario
from view.tela_usuario import TelaUsuario
from model.usuario import Usuario
from model.projeto_pessoal import ProjetoPessoal
from model.status import Status
from view.console_utils import limpar_console

class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_menu_usuario = TelaMenuUsuario()
        self.__tela_usuario = TelaUsuario()
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
                    self.__tela_usuario.usuario_retornar()
                    break

                lista_opcoes[opcao]()

            except KeyError:
                self.__tela_menu_usuario.mostra_mensagem("Opção inválida. Digite um número entre 0 e 3.")
            except ValueError:
                limpar_console()
                self.__tela_usuario.entrada_invalida()

            
            
    def ranking(self):
        ranking_usuarios = [
            (usuario.palavra_chave, len(usuario.skills_aprendidas))
            for usuario in self.__usuarios
        ]
        ranking_usuarios.sort(key=lambda x: x[1], reverse=True)
        self.__tela_usuario.mostrar_ranking(ranking_usuarios)
    
        
    def login_usuario(self):
        self.__tela_usuario.mostra_mensagem("===== LOGIN DE USUÁRIO =====")
        tentativas = 0
        usuario = None
        while True:
            username_usuario = self.__tela_usuario.solicitar_username()
            if not username_usuario:
                self.__tela_usuario.mensagem_username_vazio()
                continue

            usuario = self.pega_usuario_por_username(username_usuario)
            if usuario is None:
                tentativas += 1
                self.__tela_usuario.mensagem_usuario_nao_encontrado(tentativas)
                if tentativas >= 3:
                    self.__tela_usuario.mensagem_muitas_tentativas()
                    return
            else:
                break

        while True:
            opcao = self.__tela_usuario.mostrar_menu_usuario_logado(usuario.nome)
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
                self.__tela_usuario.mensagem_deslogando(usuario.nome)
                return
            else:
                limpar_console()
                self.__tela_usuario.mensagem_opcao_invalida()

    def menu_projetos_pessoais(self, usuario):
        while True:
            opcao = self.__tela_usuario.menu_projetos_pessoais()
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
                self.__tela_usuario.mensagem_opcao_invalida()


    def mostra_info_carreira(self, usuario):
        if not usuario.carreiras:
            info = {
                "nome": usuario.nome,
                "username": usuario.palavra_chave,
                "carreiras": []
            }
        else:
            info = {
                "nome": usuario.nome,
                "username": usuario.palavra_chave,
                "carreiras": [
                    {
                        "nome": carreira.nome,
                        "descricao": carreira.descricao,
                        "skills": [skill.nome for skill in carreira.skills_requeridas]
                    }
                    for carreira in usuario.carreiras
                ]
            }
        self.__tela_usuario.mostra_info_carreira(info)
    
    def mostra_percentual_concluido(self, usuario):
        dados_carreiras = []
        for carreira in usuario.carreiras:
            aprendidas = [s for s in usuario.skills_aprendidas if s in carreira.skills_requeridas]
            para_aprender = [s for s in carreira.skills_requeridas if s not in usuario.skills_aprendidas]
            total = len(carreira.skills_requeridas)
            concluidas = len(aprendidas)
            percentual = (concluidas / total) * 100 if total > 0 else 0
            dados_carreiras.append({
                "carreira": carreira,
                "aprendidas": aprendidas,
                "para_aprender": para_aprender,
                "percentual": percentual
            })
        self.__tela_usuario.mostra_percentual_concluido(usuario, dados_carreiras)

    def listar_projetos_pessoais(self, usuario):
        projetos_do_usuario = usuario.projetos_pessoais
        projetos = []
        for projeto in projetos_do_usuario:
            status = projeto.status.status if hasattr(projeto.status, 'status') else projeto.status
            projetos.append({
                "nome": projeto.nome,
                "descricao": projeto.descricao,
                "status": status
            })
        self.__tela_usuario.mostrar_projetos_pessoais(projetos)

    def adicionar_projeto_pessoal(self, usuario):
        dados = self.__tela_usuario.solicitar_dados_projeto()
        if not dados:
            return

        nome = dados["nome"]
        descricao = dados["descricao"]
        status_str = dados["status"]

        lista_projetos_atual = usuario.projetos_pessoais
        if any(p.nome == nome for p in lista_projetos_atual):
            self.__tela_usuario.mensagem_erro_projeto_duplicado(nome)
            return

        try:
            status_obj = Status(status_str)
        except ValueError as e:
            self.__tela_usuario.mensagem_erro_status(e)
            return

        novo_projeto = ProjetoPessoal(nome, descricao, status_obj)
        lista_projetos_atual.append(novo_projeto)
        usuario.projetos_pessoais = lista_projetos_atual
        self.__tela_usuario.mensagem_projeto_adicionado()

    def alterar_projeto_pessoal(self, usuario):
        nome_antigo = self.__tela_usuario.solicitar_nome_projeto_para_alterar()
        lista_projetos_atual = usuario.projetos_pessoais
        projeto_para_alterar = usuario._encontrar_projeto_na_lista(lista_projetos_atual, nome_antigo)

        if not projeto_para_alterar:
            self.__tela_usuario.mensagem_projeto_nao_encontrado(nome_antigo)
            return

        novos_dados = self.__tela_usuario.solicitar_novos_dados_projeto(projeto_para_alterar)
        novo_nome = novos_dados["novo_nome"]
        nova_descricao = novos_dados["nova_descricao"]
        novo_status_str = novos_dados["novo_status_str"]

        nome_final = novo_nome if novo_nome else projeto_para_alterar.nome

        if novo_nome and novo_nome != nome_antigo:
            if any(p.nome == novo_nome for p in lista_projetos_atual if p.nome != nome_antigo):
                self.__tela_usuario.mensagem_erro_nome_duplicado(novo_nome)
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
                self.__tela_usuario.mensagem_erro_status(e)

        usuario.projetos_pessoais = lista_projetos_atual
        self.__tela_usuario.mensagem_projeto_atualizado(nome_final)


    def excluir_projeto_pessoal(self, usuario):
        nome_projeto = self.__tela_usuario.solicitar_nome_projeto_para_excluir()
        lista_projetos_atual = usuario.projetos_pessoais
        projeto_para_excluir = usuario._encontrar_projeto_na_lista(lista_projetos_atual, nome_projeto)

        if not projeto_para_excluir:
            self.__tela_usuario.mensagem_projeto_nao_encontrado(nome_projeto)
            return

        lista_projetos_atual.remove(projeto_para_excluir)
        usuario.projetos_pessoais = lista_projetos_atual
        self.__tela_usuario.mensagem_projeto_excluido(nome_projeto)

    def concluir_projeto_pessoal(self, usuario):
        projetos_nao_concluidos = [
            p for p in usuario.projetos_pessoais if p.status.status != "CONCLUIDO"
        ]

        if not projetos_nao_concluidos:
            self.__tela_usuario.mensagem_nenhum_projeto_pendente()
            return

        projetos_info = [
            {"nome": p.nome, "descricao": p.descricao, "status": p.status.status}
            for p in projetos_nao_concluidos
        ]
        self.__tela_usuario.mostrar_projetos_pendentes(projetos_info)

        nome_projeto = self.__tela_usuario.solicitar_nome_projeto_para_concluir()
        projeto_para_concluir = next((p for p in projetos_nao_concluidos if p.nome == nome_projeto), None)

        if not projeto_para_concluir:
            self.__tela_usuario.mensagem_projeto_nao_encontrado_ou_concluido(nome_projeto)
            return

        try:
            projeto_para_concluir.status = Status("CONCLUIDO")
        except ValueError as e:
            self.__tela_usuario.mensagem_erro_status_concluido(e)
            return

        usuario.projetos_pessoais = usuario.projetos_pessoais  # Atualiza a lista, se necessário
        self.__tela_usuario.mensagem_projeto_concluido(nome_projeto)

    def aprender_skill(self, usuario):
        if not usuario.carreiras:
            self.__tela_usuario.mensagem_sem_carreira()
            return

        skills_disponiveis = []
        for carreira in usuario.carreiras:
            for skill in carreira.skills_requeridas:
                if skill not in usuario.skills_aprendidas and skill not in skills_disponiveis:
                    skills_disponiveis.append(skill)

        if not skills_disponiveis:
            self.__tela_usuario.mensagem_sem_skills_disponiveis()
            return

        skills_info = [{"id": skill.id, "nome": skill.nome} for skill in skills_disponiveis]
        self.__tela_usuario.mostrar_skills_disponiveis(skills_info)

        while True:
            id_skill = self.__tela_usuario.solicitar_id_skill()
            if id_skill is None:
                self.__tela_usuario.mensagem_entrada_invalida()
                continue
            skill_selecionada = next((skill for skill in skills_disponiveis if skill.id == id_skill), None)
            if skill_selecionada:
                break
            self.__tela_usuario.mensagem_id_invalido()

        usuario.skills_aprendidas.append(skill_selecionada)
        if skill_selecionada in usuario.skills_para_aprender:
            usuario.skills_para_aprender.remove(skill_selecionada)
        self.__tela_usuario.mensagem_skill_aprendida(skill_selecionada.nome)