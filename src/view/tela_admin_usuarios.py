from view.console_utils import limpar_console


class TelaAdminUsuario:
    def tela_opcoes_admin_usuarios(self):
        print('SISTEMA DE MONITORAMENTO DE HARD SKILLS')
        print('--- MENU ADMIN. USUARIOS ---')
        print('Escolha uma opção:')
        print('1 - Listar usuarios')
        print('0 - Retornar')
        opcao = int(input('Digite a opção desejada: '))
        limpar_console()
        return opcao
    
    def mostra_usuario(self, dados_usuario):
        print('USERNAME DO USUÁRIO: @', dados_usuario['username'])
        print('NOME DO USUARIO: ', dados_usuario['nome'])


    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}\n")
