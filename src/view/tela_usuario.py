import PySimpleGUI as sg

class TelaUsuario:
    def usuario_retornar(self):
        sg.popup('Saindo do menu usuário...\n')

    def entrada_invalida(self):
        sg.popup("Entrada inválida. Digite apenas números.")

    def mostrar_ranking(self, ranking_usuarios):
        texto = "--- RANKING DE APRENDIZADO ---\n"
        texto += "---------------------------------\n"
        texto += f"{'Posição':<10}{'Usuário':<20}{'Número de Skills aprendidas'}\n"
        texto += "---------------------------------\n"
        for posicao, (username, qtd_skills) in enumerate(ranking_usuarios, start=1):
            texto += f"{posicao:<10}{username:<20}{qtd_skills}\n"
        texto += "---------------------------------\n"
        sg.popup_scrolled(texto, title="Ranking de Aprendizado", size=(50, 15))

    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem)

    def solicitar_username(self):
        layout = [
            [sg.Text("Digite seu USERNAME para entrar: @")],
            [sg.InputText(key="username")],
            [sg.Submit("Entrar"), sg.Cancel("Cancelar")]
        ]
        window = sg.Window("Login de Usuário", layout)
        event, values = window.read()
        window.close()
        if event == "Entrar" and values["username"]:
            return values["username"].strip().lower()
        else:
            return None

    def mostrar_menu_usuario_logado(self, nome_usuario):
        layout = [
            [sg.Text('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')],
            [sg.Text(f"--- Bem-vindo(a), {nome_usuario}! ---")],
            [sg.Button('1 - Ver informações do usuário e carreiras escolhidas', key='1')],
            [sg.Button('2 - Ver percentual concluído', key='2')],
            [sg.Button('3 - Aprender skill', key='3')],
            [sg.Button('4 - Gerenciar projetos pessoais', key='4')],
            [sg.Button('0 - Sair (Deslogar)', key='0')],
            [sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Menu Usuário Logado', layout)
        while True:
            event, _ = window.read()
            if event in (None, 'Cancelar', sg.WIN_CLOSED):
                window.close()
                return '0'
            if event in ('0', '1', '2', '3', '4'):
                window.close()
                return event
            else:
                sg.popup("Opção inválida. Por favor, escolha uma opção entre 0 e 4.")

    def mensagem_username_vazio(self):
        sg.popup("Username não pode ser vazio. Tente novamente.\n")

    def mensagem_usuario_nao_encontrado(self, tentativas):
        sg.popup(f"Usuário não encontrado. Tente novamente. ({tentativas}/3 tentativas)\n")

    def mensagem_muitas_tentativas(self):
        sg.popup("Muitas tentativas inválidas. Retornando...\n")

    def mensagem_opcao_invalida(self):
        sg.popup("Opção inválida. Tente novamente.\n")

    def mensagem_deslogando(self, nome_usuario):
        sg.popup(f"Deslogando usuário {nome_usuario}...\n")
        

    def menu_projetos_pessoais(self):
        layout = [
            [sg.Text("--- GERENCIAR PROJETOS PESSOAIS ---")],
            [sg.Button('1 - Adicionar projeto pessoal', key='1')],
            [sg.Button('2 - Ver projetos pessoais', key='2')],
            [sg.Button('3 - Alterar projeto pessoal', key='3')],
            [sg.Button('4 - Excluir projeto pessoal', key='4')],
            [sg.Button('5 - Concluir projeto pessoal', key='5')],
            [sg.Button('0 - Voltar ao menu anterior', key='0')],
            [sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Projetos Pessoais', layout)
        while True:
            event, _ = window.read()
            if event in (None, 'Cancelar', sg.WIN_CLOSED):
                window.close()
                return '0'
            if event in ('0', '1', '2', '3', '4', '5'):
                window.close()
                return event
            else:
                sg.popup("Opção inválida. Por favor, escolha uma opção entre 0 e 5.")

    def mensagem_opcao_invalida(self):
        sg.popup("Opção inválida. Tente novamente.")
        

    def mostra_info_carreira(self, info):
        texto = "---- Informações do Usuário ----\n"
        texto += f"Nome: {info['nome']}\n"
        texto += f"Username: @{info['username']}\n"
        if not info["carreiras"]:
            texto += "Usuário não está associado a nenhuma carreira.\n"
        else:
            texto += "--- INFORMAÇÕES DAS CARREIRAS ESCOLHIDAS PELO USUÁRIO ---\n"
            for carreira in info["carreiras"]:
                texto += f"\nCarreira Escolhida: {carreira['nome']}\n"
                texto += f"Descrição: {carreira['descricao']}\n"
                skills = carreira["skills"]
                texto += f"Skills da Carreira: {', '.join(skills) if skills else 'Nenhuma skill cadastrada.'}\n"
        sg.popup_scrolled(texto, title="Informações do Usuário", size=(60, 20))
            
    def mostra_percentual_concluido(self, dados_carreiras):
        if not dados_carreiras:
            sg.popup("Usuário não está associado a nenhuma carreira.\n")
            return

        texto = ""
        for dados in dados_carreiras:
            carreira = dados["carreira"]
            aprendidas = dados["aprendidas"]
            para_aprender = dados["para_aprender"]
            percentual = dados["percentual"]

            texto += f"\n--- Skills já aprendidas ---\n"
            if aprendidas:
                for idx, skill in enumerate(aprendidas, start=1):
                    texto += f"{idx}. {skill.nome}\n"
            else:
                texto += "Nenhuma skill aprendida ainda.\n"

            texto += f"\nPercentual concluído na carreira {carreira.nome}: {percentual:.2f}%\n"

            texto += "\n--- Skills disponíveis para aprender ---\n"
            if para_aprender:
                for idx, skill in enumerate(para_aprender, start=1):
                    texto += f"{idx}. {skill.nome}\n"
            else:
                texto += "Nenhuma skill disponível para aprender.\n"
            texto += "-------\n"
        sg.popup_scrolled(texto, title="Progresso nas Carreiras", size=(60, 20))
            
    def mostrar_projetos_pessoais(self, projetos):
        if not projetos:
            sg.popup("Nenhum projeto pessoal cadastrado.\n")
            return

        texto = "\n--- Projetos Pessoais do Usuário ---\n"
        for projeto in projetos:
            texto += f"Nome: {projeto['nome']}\n"
            texto += f"Descrição: {projeto['descricao']}\n"
            texto += f"Status: {projeto['status']}\n"
            texto += "-" * 30 + "\n"
        sg.popup_scrolled(texto, title="Projetos Pessoais", size=(60, 20))

    def solicitar_dados_projeto(self):
        layout = [
            [sg.Text("Nome do projeto:"), sg.Input(key="nome")],
            [sg.Text("Descrição do projeto:"), sg.Input(key="descricao")],
            [sg.Text("Status inicial (A_FAZER, EM_ANDAMENTO, CONCLUIDO):"), sg.Input(key="status")],
            [sg.Submit("OK"), sg.Cancel("Cancelar")]
        ]
        window = sg.Window("Adicionar Projeto Pessoal", layout)
        event, values = window.read()
        window.close()
        if event == "OK" and values["nome"].strip():
            return {
                "nome": values["nome"].strip(),
                "descricao": values["descricao"].strip(),
                "status": values["status"].strip().upper()
            }
        else:
            sg.popup("Nome do projeto não pode ser vazio.")
            return None

    def mensagem_erro_projeto_duplicado(self, nome):
        sg.popup(f"Erro: Um projeto com o nome '{nome}' já existe.")

    def mensagem_erro_status(self, erro):
        sg.popup(f"Erro no status: {erro}")

    def mensagem_projeto_adicionado(self):
        sg.popup("Projeto pessoal adicionado com sucesso!\n")
        
    def solicitar_nome_projeto_para_alterar(self):
        layout = [[sg.Text("Nome do projeto a ser alterado:")], [sg.Input(key="nome")], [sg.Submit(), sg.Cancel()]]
        window = sg.Window("Alterar Projeto", layout)
        event, values = window.read()
        window.close()
        return values["nome"].strip() if event == "Submit" and values["nome"].strip() else None

    def mensagem_projeto_nao_encontrado(self, nome):
        sg.popup(f"Projeto '{nome}' não encontrado.")

    def solicitar_novos_dados_projeto(self, projeto):
        layout = [
            [sg.Text(f"Novo nome (deixe em branco para manter '{projeto.nome}'):"), sg.Input(key="novo_nome")],
            [sg.Text("Nova descrição (deixe em branco para manter):"), sg.Input(key="nova_descricao")],
            [sg.Text(f"Novo status (deixe em branco para manter '{projeto.status.status}'):"), sg.Input(key="novo_status_str")],
            [sg.Submit(), sg.Cancel()]
        ]
        window = sg.Window("Editar Projeto", layout)
        event, values = window.read()
        window.close()
        if event == "Submit":
            return {
                "novo_nome": values["novo_nome"].strip(),
                "nova_descricao": values["nova_descricao"].strip(),
                "novo_status_str": values["novo_status_str"].strip().upper()
            }
        else:
            return None

    def mensagem_erro_nome_duplicado(self, novo_nome):
        sg.popup(f"Erro: Já existe um projeto com o nome '{novo_nome}'. Alteração de nome cancelada.")

    def mensagem_erro_status(self, erro):
        sg.popup(f"Erro no novo status: {erro}. Status não alterado.")

    def mensagem_projeto_atualizado(self, nome_final):
        sg.popup(f"Projeto '{nome_final}' atualizado com sucesso!\n")
        
    def solicitar_nome_projeto_para_excluir(self):
        layout = [[sg.Text("Nome do projeto a ser excluído:")], [sg.Input(key="nome")], [sg.Submit(), sg.Cancel()]]
        window = sg.Window("Excluir Projeto", layout)
        event, values = window.read()
        window.close()
        return values["nome"].strip() if event == "Submit" and values["nome"].strip() else None

    def mensagem_projeto_nao_encontrado(self, nome):
        sg.popup(f"Projeto '{nome}' não encontrado.")

    def mensagem_projeto_excluido(self, nome):
        sg.popup(f"Projeto '{nome}' excluído com sucesso!\n")
        
    def mostrar_projetos_pendentes(self, projetos):
        if not projetos:
            sg.popup("Nenhum projeto pendente.")
            return
        texto = "Projetos pessoais pendentes:\n"
        for projeto in projetos:
            texto += f"Nome: {projeto['nome']}\n"
            texto += f"Descrição: {projeto['descricao']}\n"
            texto += f"Status: {projeto['status']}\n"
            texto += "-" * 30 + "\n"
        sg.popup_scrolled(texto, title="Projetos Pendentes", size=(60, 20))

    def solicitar_nome_projeto_para_concluir(self):
        layout = [[sg.Text("Nome do projeto a ser concluído:")], [sg.Input(key="nome")], [sg.Submit(), sg.Cancel()]]
        window = sg.Window("Concluir Projeto", layout)
        event, values = window.read()
        window.close()
        return values["nome"].strip() if event == "Submit" and values["nome"].strip() else None

    def mensagem_nenhum_projeto_pendente(self):
        sg.popup("Nenhum projeto pessoal pendente para concluir.\n")

    def mensagem_projeto_nao_encontrado_ou_concluido(self, nome):
        sg.popup(f"Projeto '{nome}' não encontrado ou já está concluído.")

    def mensagem_erro_status_concluido(self, erro):
        sg.popup(f"Erro ao definir status como CONCLUIDO: {erro}")

    def mensagem_projeto_concluido(self, nome):
        sg.popup(f"Projeto '{nome}' marcado como CONCLUÍDO!\n")

    def mensagem_sem_carreira(self):
        sg.popup("Usuário não está associado a nenhuma carreira.\n")

    def mostrar_skills_disponiveis(self, skills):
        if not skills:
            sg.popup("Nenhuma skill disponível.")
            return
        texto = "Skills disponíveis:\n"
        for skill in skills:
            texto += f"ID: {skill['id']} - Nome: {skill['nome']}\n"
        sg.popup_scrolled(texto, title="Skills Disponíveis", size=(50, 15))

    def mensagem_sem_skills_disponiveis(self):
        sg.popup("Não há skills disponíveis para aprender.\n")

    def solicitar_id_skill(self):
        layout = [[sg.Text("Digite o ID da skill que deseja aprender:")],
                  [sg.Input(key="id")],
                  [sg.Submit(), sg.Cancel()]]
        window = sg.Window("Aprender Skill", layout)
        event, values = window.read()
        window.close()
        if event == "Submit":
            try:
                return int(values["id"])
            except ValueError:
                self.mensagem_entrada_invalida()
                return None
        return None

    def mensagem_id_invalido(self):
        sg.popup("ID inválido. Tente novamente.")

    def mensagem_entrada_invalida(self):
        sg.popup("Entrada inválida. Digite um número.")

    def mensagem_skill_aprendida(self, nome_skill):
        sg.popup(f"\nParabéns! Você aprendeu a skill: {nome_skill}")