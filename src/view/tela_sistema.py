class TelaSistema:
    def tela_opcoes_iniciais(self):
        print("===== BEM-VINDO AO SISTEMA DE MONITORAMENTO DE HARD SKILLS =====")
        print("1 - Entrar como Administrador")
        print("2 - Entrar como Usuário")
        print("0 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        print()
        return opcao
    
    def tela_opcoes_admin(self):
        print('--- MENU ADMINISTRADOR ---')
        print('Escolha uma opção:')
        print('1 - CARREIRA')
        print('2 - SKILL')
        print('3 - USUÁRIO')
        print('0 - VOLTAR')
        opcao = int(input('Digite a opção desejada: '))
        print('\n')
        return opcao