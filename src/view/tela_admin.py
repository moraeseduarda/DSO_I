import PySimpleGUI as sg

class TelaAdmin:
    def tela_opcoes_admin_usuarios(self):
        layout = [
            [sg.Text('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')],
            [sg.Text('--- MENU ADMIN. USUÁRIOS ---')],
            [sg.Text('Escolha uma opção:')],
            [sg.Button('1 - Listar usuários', key=1)],
            [sg.Button('0 - Retornar', key=0)],
        ]
        window = sg.Window('Menu Admin. Usuários', layout)
        while True:
            event, _ = window.read()
            if event in (None, sg.WIN_CLOSED):
                window.close()
                return 0
            if event in (0, 1):
                window.close()
                return event
            else:
                sg.popup("Opção inválida. Por favor, escolha 0 ou 1.")
    
    def mostra_usuario(self, dados_usuario):
        mensagem = (
            '-----------------------------------\n'
            f'USERNAME DO USUÁRIO: @{dados_usuario["username"]}\n'
            f'NOME DO USUÁRIO: {dados_usuario["nome"]}\n'
            f'CARREIRAS: {", ".join(dados_usuario["carreiras"]) if dados_usuario["carreiras"] else "Nenhuma"}\n'
            f'SKILLS APRENDIDAS: {", ".join(dados_usuario["skills_aprendidas"]) if dados_usuario["skills_aprendidas"] else "Nenhuma"}\n'
            '-----------------------------------'
        )
        sg.popup(mensagem, title="Detalhes do Usuário")


    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem)
    

    def tela_opcoes_admin(self):
        layout = [
            [sg.Text('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')],
            [sg.Text('--- MENU ADMINISTRADOR ---')],
            [sg.Text('Escolha uma opção:')],
            [sg.Button('1 - CARREIRAS', key=1)],
            [sg.Button('2 - SKILLS', key=2)],
            [sg.Button('3 - USUÁRIOS', key=3)],
            [sg.Button('0 - VOLTAR AO MENU PRINCIPAL', key=0)],
        ]
        window = sg.Window('Menu Administrador', layout)
        while True:
            event, _ = window.read()
            if event in (None, sg.WIN_CLOSED):
                window.close()
                return 0
            if event in (0, 1, 2, 3):
                window.close()
                return event
            else:
                sg.popup("Opção inválida. Por favor, escolha uma opção entre 0 e 3.")

    def solicitar_palavra_chave_admin(self):
        layout = [
            [sg.Text("Digite a palavra-chave do administrador: ")],
            [sg.Text("Palavra-chave: "), sg.InputText(key="palavra_chave")],
            [sg.Submit("Enviar"), sg.Cancel("Cancelar")]
        ]
        window = sg.Window('Permissão administrador', layout)
        event, values = window.read()
        window.close()
        if event == 'Enviar':
            return values['palavra_chave'].strip()
        else:
            return None