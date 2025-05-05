class TelaCarreira:    
    def tela_opcoes(self):
        print('SISTEMA DE MONITORAMENTO DE HARD SKILLS')
        print('Escolha uma opção:')
        print('1 - Incluir carreira')
        print('2 - Alterar carreira')
        print('3 - Excluir carreira')
        print('4 - Listar carreira')
        print('5 - Retornar')
        opcao = int(input('Digite a opção desejada: '))
        print('\n')
        return opcao
    
    def pega_dados_carreira(self):
        print('---------- CARREIRA ----------')
        id = int(input('Digite o ID da carreira: '))
        nome = input('Digite o nome da carreira: ')
        descricao = input('Digite a descrição da carreira: ')
        
        return {'id': id, 'nome': nome, 'descricao': descricao}
    
    def mostra_carreira(self, dados_carreira):
        print('ID DA CARREIRA: ', dados_carreira['id'])
        print('NOME DA CARREIRA: ', dados_carreira['nome'])
        print('DESCRICAO DA CARREIRA: ', dados_carreira['descricao'])
        print('\n')
        
    def seleciona_carreira(self):
        id = int(input('Digite o ID da carreira: '))
        return id
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)