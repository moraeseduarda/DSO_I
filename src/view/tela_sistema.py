import PySimpleGUI as sg


class TelaSistema:
    
    def __init__(self):
        sg.theme('DarkPurple4')
        
    def tela_opcoes_iniciais(self):
        layout = [
            [sg.Text("SISTEMA DE MONITORAMENTO DE HARD SKILLS",  font=('Arial', 16), justification='center')],
            [sg.Button("Entrar como Administrador", key="1")],
            [sg.Button("Entrar como Usuário", key="2")],
            [sg.Button("Sair", key="0")]
        ]
        window = sg.Window("Menu", layout)
        while True:
            event, _ = window.read()
            if event in ("0", sg.WIN_CLOSED):
                opcao = 0
                break
            elif event == "1":
                opcao = 1
                break
            elif event == "2":
                opcao = 2
                break
        window.close()
        return opcao

    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem)
