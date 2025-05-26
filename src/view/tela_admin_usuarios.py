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
        print('-----------------------------------')
        print('USERNAME DO USUÁRIO: @', dados_usuario['username'])
        print('NOME DO USUARIO: ', dados_usuario['nome'])
        print('CARREIRAS: ', ", ".join(dados_usuario['carreiras']) if dados_usuario['carreiras'] else "Nenhuma")
        print('SKILLS APRENDIDAS: ', ", ".join(dados_usuario['skills_aprendidas']) if dados_usuario['skills_aprendidas'] else "Nenhuma")
        print('-----------------------------------')


    def mostra_mensagem(self, mensagem):
        print(mensagem)
        input("Pressione ENTER para continuar...")
        limpar_console()
    

    def tela_opcoes_admin(self):
        print('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')
        print('--- MENU ADMINISTRADOR ---')
        print('Escolha uma opção:')
        print('1 - CARREIRAS')
        print('2 - SKILLS')
        print('3 - USUÁRIOS')
        print('0 - VOLTAR AO MENU PRINCIPAL')
        while True:
            try:
                opcao = int(input('Digite a opção desejada: '))
                limpar_console()
                return opcao
            except ValueError:
                limpar_console()
                print("Entrada inválida. Por favor, digite um número.")
