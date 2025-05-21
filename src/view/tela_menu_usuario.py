from view.utils import limpar_console

class TelaMenuUsuario:
    def tela_opcoes(self):
        print('--- MENU USUÁRIO ---')
        print('1 - Criar Conta')
        print('2 - Fazer Login')
        print('0 - Retornar')
        opcao = int(input('Digite a opção desejada: '))
        limpar_console()
        return opcao
        

    def pega_dados_cadastro_usuario(self):
        print('--- CADASTRO DE USUÁRIO ---')
        id_usuario = int(input('Digite o ID do usuário: '))
        nome = input('Digite o nome do usuário: ')
        return {'id': id_usuario, 'nome': nome}

    def seleciona_carreira(self, lista_carreiras):
        # Verifica se há carreiras cadastradas
        print('Escolha sua carreira:')
        for carreira in lista_carreiras:
            print(f'{carreira.id} - {carreira.nome}')
        id_escolhido = int(input('Digite o ID da carreira desejada: '))
        return id_escolhido

    def mostra_mensagem(self, mensagem):
        print(mensagem)