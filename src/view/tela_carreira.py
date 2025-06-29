import PySimpleGUI as sg


class TelaCarreira:    
    def tela_opcoes(self):
        layout = [
            [sg.Text('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====', font=('Arial', 16), justification='center')],
            [sg.Text('--- CARREIRAS ---', font=('Arial', 14))],
            [sg.Button('1 - Cadastrar nova carreira')],
            [sg.Button('2 - Alterar carreira existente')],
            [sg.Button('3 - Excluir uma carreira')],
            [sg.Button('4 - Listar todas as carreiras cadastradas')],
            [sg.Button('0 - Retornar')],
        ]
        window = sg.Window('Menu Carreiras', layout)
        while True:
            event, _ = window.read()
            if event in (sg.WIN_CLOSED, '0 - Retornar'):
                window.close()
                return 0
            elif event == '1 - Cadastrar nova carreira':
                window.close()
                return 1
            elif event == '2 - Alterar carreira existente':
                window.close()
                return 2
            elif event == '3 - Excluir uma carreira':
                window.close()
                return 3
            elif event == '4 - Listar todas as carreiras cadastradas':
                window.close()
                return 4

    def pega_dados_carreira(self, cadastro):
        titulo = '---------- CADASTRO CARREIRA ----------' if cadastro else '---------- CARREIRA ----------'
        layout = [
            [sg.Text(titulo, font=('Arial', 14))],
            [sg.Text('Digite o ID da carreira:'), sg.Input(key='id')],
            [sg.Text('Digite o nome da carreira:'), sg.Input(key='nome')],
            [sg.Text('Digite a descrição da carreira:'), sg.Input(key='descricao')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Cadastro Carreira', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None
            elif event == 'Confirmar':
                try:
                    id = int(values['id'])
                except (ValueError, TypeError):
                    sg.popup('ID inválido. Digite um número inteiro.')
                    continue
                nome = values['nome'].strip().upper()
                descricao = values['descricao'].strip().upper()
                if not nome or not descricao:
                    sg.popup('Nome e descrição não podem ser vazios.')
                    continue
                window.close()
                return {'id': id, 'nome': nome, 'descricao': descricao}

    def mostra_lista_carreiras(self, lista_carreiras):
        if not lista_carreiras:
            sg.popup("Nenhuma carreira cadastrada.")
            return
        texto = ""
        for carreira in lista_carreiras:
            texto += f"ID: {carreira['id']}\nNome: {carreira['nome']}\nDescrição: {carreira['descricao']}\n------------------------------\n"
        sg.popup_scrolled(texto, title="Lista de Carreiras", size=(50, 15))

    def seleciona_carreira(self):
        layout = [
            [sg.Text('Digite o ID da carreira:'), sg.Input(key='id')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Selecionar Carreira', layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None
            try:
                id = int(values['id'])
                window.close()
                return id
            except (ValueError, TypeError):
                sg.popup("Entrada inválida. Digite um número inteiro.")

    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem)

    def mensagem_inicio_alteracao(self):
        sg.popup("-- Alterando uma carreira, informe o ID... --")

    def mensagem_altere_campos(self):
        sg.popup("-- Agora, altere os campos para os valores que você deseja: --")
        
    def retornar(self):
        sg.popup("Retornando ao menu administrador...")
        
    def mostra_ids_carreiras_validas(self, ids_validos):
        if not ids_validos:
            sg.popup("Nenhum ID válido encontrado.")
        else:
            sg.popup("IDs de carreiras válidas selecionadas:\n" + ", ".join(str(id_) for id_ in ids_validos))
