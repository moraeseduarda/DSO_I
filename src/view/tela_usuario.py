class TelaUsuario():
    def tela_opcoes(self):
        print('SISTEMA DE MONITORAMENTO DE HARD SKILLS')
        print('Escolha uma opção:')
        print('1 - Incluir usuario')
        print('2 - Alterar usuario')
        print('3 - Excluir usuario')
        print('4 - Listar usuario')
        print('5 - Retornar')
        opcao = int(input('Digite a opção desejada: '))
        print('\n')
        return opcao
    
    def pega_dados_usuario(self):
        print('---------- CADASTRO DO USUARIO ----------')
        id = int(input('Digite o ID do Usuario: '))
        nome = input('Digite o nome do Usuario: ')
        
        return {'id': id, 'nome': nome}
    
    def seleciona_carreira(self):
        pass
        
    def mostra_usuario(self, dados_usuario):
        print('ID DO USUARIO: ', dados_usuario['id'])
        print('NOME DO USUARIO: ', dados_usuario['nome'])
        print('DESCRICAO DO USUARIO: ', dados_usuario['descricao'])
        print('\n')
        
    def seleciona_usuario(self):
        id = int(input('Digite o ID DO USUARIO: '))
        return id
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)