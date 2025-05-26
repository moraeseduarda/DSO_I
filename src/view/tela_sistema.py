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
    
    def tela_opcoes_admin(self):
        print('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')
        print('--- MENU ADMINISTRADOR ---')
        print('Escolha uma opção:')
        print('1 - CARREIRAS')
        print('2 - SKILLS')
        print('3 - USUÁRIOS')
        print('0 - VOLTAR AO MENU PRINCIPAL')
        opcao = int(input('Digite a opção desejada: '))
        limpar_console()
        return opcao