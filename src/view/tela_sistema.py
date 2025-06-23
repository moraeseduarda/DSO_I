from view.console_utils import limpar_console


class TelaSistema:
    def tela_opcoes_iniciais(self):
        print("===== BEM-VINDO AO SISTEMA DE MONITORAMENTO DE HARD SKILLS =====")
        print("1 - Entrar como Administrador")
        print("2 - Entrar como Usuário")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        limpar_console()
        return opcao
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)
