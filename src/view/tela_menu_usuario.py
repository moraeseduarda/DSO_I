import PySimpleGUI as sg

class TelaMenuUsuario:
    def tela_opcoes(self):
        layout = [
            [sg.Text('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====', font=('Arial', 16), justification='center')],
            [sg.Text('--- MENU USUÁRIO ---', font=('Arial', 14))],
            [sg.Button('1 - Criar Conta')],
            [sg.Button('2 - Fazer Login')],
            [sg.Button('3 - VER RANKINGS')],
            [sg.Button('0 - Retornar')],
        ]
        window = sg.Window('Menu Usuário', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, '0 - Retornar'):
                window.close()
                return 0
            elif event == '1 - Criar Conta':
                window.close()
                return 1
            elif event == '2 - Fazer Login':
                window.close()
                return 2
            elif event == '3 - VER RANKINGS':
                window.close()
                return 3

    def pega_dados_cadastro_usuario(self):
        layout = [
            [sg.Text('--- CADASTRO DE USUÁRIO ---', font=('Arial', 14))],
            [sg.Text('Digite o USERNAME do usuário:'), sg.Input(key='username')],
            [sg.Text('Digite o nome do usuário:'), sg.Input(key='nome')],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Cadastro Usuário', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return None
            elif event == 'Confirmar':
                username = values['username'].strip().lower()
                nome = values['nome'].strip().upper()
                if not username:
                    sg.popup('Username não pode ser vazio!')
                    continue
                if not nome:
                    sg.popup('Nome não pode ser vazio!')
                    continue
                window.close()
                return {'username': username, 'nome': nome}

    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem)

    def seleciona_carreiras(self, lista_carreiras):
        layout = [
            [sg.Text('📌 Escolha as carreiras (selecione uma ou mais):')],
            [sg.Listbox(values=[f"{c.id} - {c.nome}" for c in lista_carreiras], key='carreiras', select_mode=sg.SELECT_MODE_EXTENDED, size=(40,10))],
            [sg.Button('Confirmar'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Selecionar Carreiras', layout)

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancelar'):
                window.close()
                return []
            elif event == 'Confirmar':
                selecionados = values['carreiras']
                if not selecionados:
                    sg.popup('Selecione ao menos uma carreira.')
                    continue
                # extrair só os IDs
                ids_selecionados = [int(item.split(' - ')[0]) for item in selecionados]
                window.close()
                return ids_selecionados
