class TelaUsuario:
    def usuario_retornar(self):
        print('Saindo do menu usuário...\n')

    def entrada_invalida(self):
        print("Entrada inválida. Digite apenas números.")

    def mostrar_ranking(self, ranking_usuarios):
            print("\n--- RANKING DE APRENDIZADO ---")
            print("---------------------------------")
            print(f"{'Posição':<10}{'Usuário':<20}{'Número de Skills aprendidas'}")
            print("---------------------------------")
            for posicao, (username, qtd_skills) in enumerate(ranking_usuarios, start=1):
                print(f"{posicao:<10}{username:<20}{qtd_skills}")
            print("---------------------------------\n")
            
            
    def mostra_mensagem(self, mensagem):
        print(mensagem)


    def solicitar_username(self):
        return input("Digite seu USERNAME para entrar: @").strip().lower()

    def mostrar_menu_usuario_logado(self, nome_usuario):
        print('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')
        print(f"\n--- Bem-vindo(a), {nome_usuario}! ---")
        print("1 - Ver informações do usuário e carreiras escolhidas")
        print("2 - Ver percentual concluído")
        print("3 - Aprender skill")
        print("4 - Gerenciar projetos pessoais")
        print("0 - Sair (Deslogar)")
        return input("Digite a opção desejada: ").strip()

    def mensagem_username_vazio(self):
        print("Username não pode ser vazio. Tente novamente.\n")

    def mensagem_usuario_nao_encontrado(self, tentativas):
        print(f"Usuário não encontrado. Tente novamente. ({tentativas}/3 tentativas)\n")

    def mensagem_muitas_tentativas(self):
        print("Muitas tentativas inválidas. Retornando...\n")

    def mensagem_opcao_invalida(self):
        print("Opção inválida. Tente novamente.\n")

    def mensagem_deslogando(self, nome_usuario):
        print(f"Deslogando usuário {nome_usuario}...\n")
        

    def menu_projetos_pessoais(self):
        print("\n--- GERENCIAR PROJETOS PESSOAIS ---")
        print("1 - Adicionar projeto pessoal")
        print("2 - Ver projetos pessoais")
        print("3 - Alterar projeto pessoal")
        print("4 - Excluir projeto pessoal")
        print("5 - Concluir projeto pessoal")
        print("0 - Voltar ao menu anterior")
        return input("Escolha uma opção: ").strip()

    def mensagem_opcao_invalida(self):
        print("Opção inválida. Tente novamente.")
        

    def mostra_info_carreira(self, info):
        print("---- Informações do Usuário ----")
        print(f"Nome: {info['nome']}")
        print(f"Username: @{info['username']}")
        if not info["carreiras"]:
            print("Usuário não está associado a nenhuma carreira.\n")
            return
        print("--- INFORMAÇÕES DAS CARREIRAS ESCOLHIDAS PELO USUÁRIO")
        for carreira in info["carreiras"]:
            print(f"\nCarreira Escolhida: {carreira['nome']}")
            print(f"Descrição: {carreira['descricao']}")
            skills = carreira["skills"]
            print(f"Skills da Carreira: {', '.join(skills) if skills else 'Nenhuma skill cadastrada.'}\n")
            
    def mostra_percentual_concluido(self, dados_carreiras):
        if not dados_carreiras:
            print("Usuário não está associado a nenhuma carreira.\n")
            return
        for dados in dados_carreiras:
            carreira = dados["carreira"]
            aprendidas = dados["aprendidas"]
            para_aprender = dados["para_aprender"]
            percentual = dados["percentual"]

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
            
    def mostrar_projetos_pessoais(self, projetos):
        print("\n--- Projetos Pessoais do Usuário ---")
        if not projetos:
            print("Nenhum projeto pessoal cadastrado.\n")
            return
        for projeto in projetos:
            print(f"Nome: {projeto['nome']}")
            print(f"Descrição: {projeto['descricao']}")
            print(f"Status: {projeto['status']}")
            print("-" * 30)

    def solicitar_dados_projeto(self):
        print("\n--- Adicionar Novo Projeto Pessoal ---")
        nome = input("Nome do projeto: ").strip()
        if not nome:
            print("Nome do projeto não pode ser vazio.")
            return None
        descricao = input("Descrição do projeto: ").strip()
        status_str = input("Status inicial do projeto (ex: A_FAZER, EM_ANDAMENTO, CONCLUIDO): ").strip().upper()
        return {"nome": nome, "descricao": descricao, "status": status_str}

    def mensagem_erro_projeto_duplicado(self, nome):
        print(f"Erro: Um projeto com o nome '{nome}' já existe.")

    def mensagem_erro_status(self, erro):
        print(f"Erro no status: {erro}")

    def mensagem_projeto_adicionado(self):
        print("Projeto pessoal adicionado com sucesso!\n")
        
    def solicitar_nome_projeto_para_alterar(self):
        print("\n--- Alterar Projeto Pessoal ---")
        return input("Nome do projeto a ser alterado: ").strip()

    def mensagem_projeto_nao_encontrado(self, nome):
        print(f"Projeto '{nome}' não encontrado.")

    def solicitar_novos_dados_projeto(self, projeto):
        print(f"Alterando projeto: {projeto.nome}")
        novo_nome = input(f"Novo nome (deixe em branco para manter '{projeto.nome}'): ").strip()
        nova_descricao = input("Nova descrição (deixe em branco para manter): ").strip()
        status_atual = projeto.status.status if hasattr(projeto.status, 'status') else projeto.status
        novo_status_str = input(f"Novo status (deixe em branco para manter '{status_atual}'): ").strip().upper()
        return {"novo_nome": novo_nome, "nova_descricao": nova_descricao, "novo_status_str": novo_status_str}

    def mensagem_erro_nome_duplicado(self, novo_nome):
        print(f"Erro: Já existe um projeto com o nome '{novo_nome}'. Alteração de nome cancelada.")

    def mensagem_erro_status(self, erro):
        print(f"Erro no novo status: {erro}. Status não alterado.")

    def mensagem_projeto_atualizado(self, nome_final):
        print(f"Projeto '{nome_final}' atualizado com sucesso!\n")
        
    def solicitar_nome_projeto_para_excluir(self):
        print("\n--- Excluir Projeto Pessoal ---")
        return input("Nome do projeto a ser excluído: ").strip()

    def mensagem_projeto_nao_encontrado(self, nome):
        print(f"Projeto '{nome}' não encontrado.")

    def mensagem_projeto_excluido(self, nome):
        print(f"Projeto '{nome}' excluído com sucesso!\n")
        
    def mostrar_projetos_pendentes(self, projetos):
        print("Projetos pessoais pendentes:")
        for projeto in projetos:
            print(f"Nome: {projeto['nome']}")
            print(f"Descrição: {projeto['descricao']}")
            print(f"Status: {projeto['status']}")
            print("-" * 30)

    def solicitar_nome_projeto_para_concluir(self):
        return input("Nome do projeto a ser concluído: ").strip()

    def mensagem_nenhum_projeto_pendente(self):
        print("Nenhum projeto pessoal pendente para concluir.\n")

    def mensagem_projeto_nao_encontrado_ou_concluido(self, nome):
        print(f"Projeto '{nome}' não encontrado ou já está concluído.")

    def mensagem_erro_status_concluido(self, erro):
        print(f"Erro ao definir status como CONCLUIDO: {erro}")

    def mensagem_projeto_concluido(self, nome):
        print(f"Projeto '{nome}' marcado como CONCLUÍDO!\n")

    def mensagem_sem_carreira(self):
        print("Usuário não está associado a nenhuma carreira.\n")

    def mostrar_skills_disponiveis(self, skills):
        for skill in skills:
            print(f"ID: {skill['id']} - Nome: {skill['nome']}")

    def mensagem_sem_skills_disponiveis(self):
        print("Não há skills disponíveis para aprender.\n")

    def solicitar_id_skill(self):
        try:
            return int(input("\nDigite o ID da skill que deseja aprender: "))
        except ValueError:
            return None

    def mensagem_id_invalido(self):
        print("ID inválido. Tente novamente.")

    def mensagem_entrada_invalida(self):
        print("Entrada inválida. Digite um número.")

    def mensagem_skill_aprendida(self, nome_skill):
        print(f"\nParabéns! Você aprendeu a skill: {nome_skill}")