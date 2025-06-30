import PySimpleGUI as sg


class TelaSkill:
    def tela_opcoes(self):
        while True:
            layout = [
                [sg.Text('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')],
                [sg.Text('===== MENU SKILLS =====')],
                [sg.Button('Incluir habilidade', key='1')],
                [sg.Button('Excluir habilidade', key='2')],
                [sg.Button('Listar habilidades', key='3')],
                [sg.Button('Adicionar material de estudo', key='4')],
                [sg.Button('Associar skill a carreira', key='5')],
                [sg.Button('Retornar', key='0')]
            ]
            window = sg.Window('Menu Skills', layout)
            event, _ = window.read()
            window.close()
            if event in ('0', sg.WIN_CLOSED):
                return 0
            elif event in ('1', '2', '3', '4', '5'):
                return int(event)

    def pega_dados_skill(self):
        layout = [
            [sg.Text('-----HABILIDADE-----')],
            [sg.Text('ID da habilidade:'), sg.Input(key='id')],
            [sg.Text('Nome da habilidade:'), sg.Input(key='nome')],
            [sg.Text('Descrição da habilidade:'), sg.Input(key='descricao')],
            [sg.Button('OK'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Cadastrar Habilidade', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None
            try:
                id = int(values['id'])
                nome = values['nome'].upper()
                descricao = values['descricao'].upper()
                window.close()
                return {'id': id, 'nome': nome, 'descricao': descricao}
            except (ValueError, TypeError):
                sg.popup("ID inválido. Digite um número.")

    def pega_dados_material_estudo(self):
        tipos = {1: 'LIVRO', 2: 'VIDEO', 3: 'CURSO', 4: 'ARTIGO'}
        layout = [
            [sg.Text('-----MATERIAL DE ESTUDO-----')],
            [sg.Text('Título do material:'), sg.Input(key='titulo')],
            [sg.Text('Descrição do material:'), sg.Input(key='descricao')],
            [sg.Text('Tipo do material:')],
            [sg.Combo(['LIVRO', 'VIDEO', 'CURSO', 'ARTIGO'], key='tipo')],
            [sg.Button('OK')]
        ]
        window = sg.Window('Cadastrar Material de Estudo', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                return None
            titulo = values['titulo']
            descricao = values['descricao']
            tipo = values['tipo']
            if not titulo or not descricao or not tipo:
                sg.popup("Todos os campos são obrigatórios.")
                continue
            if tipo in tipos.values():
                window.close()
                return {
                    'titulo': titulo.upper(),
                    'descricao': descricao.upper(),
                    'tipo': tipo
                }
            sg.popup("Opção inválida. Escolha um tipo de material.")

    def mostra_skill(self, lista_dados_skill):
        # lista_dados_skill deve ser uma lista de dicionários, um para cada skill
        if not lista_dados_skill:
            sg.popup_scrolled("Nenhuma skill cadastrada!", title="Skills", size=(60, 20))
            return

        linhas = []
        for dados_skill in lista_dados_skill:
            materiais = '\n'.join(
                [f"- {m['titulo']} ({m['tipo']})" for m in dados_skill.get('material_estudo', [])]
            ) if dados_skill.get('material_estudo') else "Nenhum material cadastrado"
            carreiras = '\n'.join(
                [f"- {c}" for c in dados_skill.get('carreiras', [])]
            ) if dados_skill.get('carreiras') else "Nenhuma carreira associada"
            mensagem = (
                f"=== DETALHES DA SKILL ===\n"
                f"ID: {dados_skill['id']}\n"
                f"NOME: {dados_skill['nome']}\n"
                f"DESCRIÇÃO: {dados_skill['descricao']}\n"
                f"MATERIAIS DE ESTUDO:\n{materiais}\n"
                f"CARREIRAS ASSOCIADAS:\n{carreiras}\n"
                f"------------------------"
            )
            linhas.append(mensagem)

        sg.popup_scrolled(
            *linhas,
            title="Skills",
            size=(60, 20)
        )

    def seleciona_skill(self):
        layout = [
            [sg.Text('Digite o ID da habilidade:'), sg.Input(key='id')],
            [sg.Button('OK')]
        ]
        window = sg.Window('Selecionar Skill', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                return None
            try:
                id = int(values['id'])
                window.close()
                return id
            except (ValueError, TypeError):
                sg.popup("ID inválido. Digite um número.")

    def confirma_exclusao(self):
        layout = [
            [sg.Text('Confirma a exclusão da skill?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]
        window = sg.Window('Confirmar Exclusão', layout)
        event, _ = window.read()
        window.close()
        return event == 'Sim'

    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem)

    def seleciona_carreira(self):
        layout = [
            [sg.Text('Digite o ID da carreira desejada:'), sg.Input(key='id')],
            [sg.Button('OK')]
        ]
        window = sg.Window('Selecionar Carreira', layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                window.close()
                return None
            try:
                id = int(values['id'])
                window.close()
                return id
            except (ValueError, TypeError):
                sg.popup("ID inválido. Digite um número.")

    def mostra_carreiras_disponiveis(self, carreiras):
        if carreiras:
            texto = '\n'.join([f'ID: {c["id"]} - Nome: {c["nome"]}' for c in carreiras])
        else:
            texto = "Nenhuma carreira cadastrada!"
        sg.popup('=== CARREIRAS DISPONÍVEIS ===\n' + texto + '\n---------------------------')

    def mostra_skills_disponiveis(self, skills):
        if skills:
            lista = [f'ID: {s["id"]} - Nome: {s["nome"]}' for s in skills]
        else:
            lista = ["Nenhuma skill cadastrada!"]
        sg.popup_scrolled(
            *lista,
            title='SKILLS DISPONÍVEIS',
            size=(60, 20)
        )

    def enter(self):
        sg.popup('Pressione OK para continuar...')

    def retornar(self):
        sg.popup("Retornando ao menu administrador...")