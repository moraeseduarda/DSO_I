class TelaAdminUsuario():
    def tela_opcoes(self):
        print('SISTEMA DE MONITORAMENTO DE HARD SKILLS')
        print('--- MENU ADMIN. USUARIOS ---')
        print('Escolha uma opção:')
        print('1 - Listar usuarios')
        print('0 - Retornar')
        opcao = int(input('Digite a opção desejada: '))
        print('\n')
        return opcao
    
    def mostra_usuario(self, dados_usuario):
        print('ID DO USUARIO: ', dados_usuario['id'])
        print('NOME DO USUARIO: ', dados_usuario['nome'])
        print('\n')
