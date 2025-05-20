from view.utils import limpar_console

class TelaCarreira:    
    def tela_opcoes(self):
        print('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')
        print('--- CARREIRAS ---')
        print('Escolha uma opção:')
        print('1 - Incluir carreira')
        print('2 - Alterar carreira')
        print('3 - Excluir carreira')
        print('4 - Listar carreiras')
        print('5 - Retornar')
        opcao = int(input('Digite a opção desejada: '))
        limpar_console()
        return opcao
    
    def pega_dados_carreira(self):
        limpar_console()
        print('---------- CARREIRA ----------')
        id = int(input('Digite o ID da carreira: '))
        nome = input('Digite o nome da carreira: ')
        descricao = input('Digite a descrição da carreira: ')
        
        return {'id': id, 'nome': nome, 'descricao': descricao}
    
    def mostra_carreira(self, dados_carreira):
        limpar_console()
        print('ID DA CARREIRA: ', dados_carreira['id'])
        print('NOME DA CARREIRA: ', dados_carreira['nome'])
        print('DESCRICAO DA CARREIRA: ', dados_carreira['descricao'])
        
    def seleciona_carreira(self):
        id = int(input('Digite o ID da carreira: '))
        return id
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)