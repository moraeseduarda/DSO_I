class TelaMenuUsuario:
    def tela_opcoes(self):
        print('SISTEMA DE MONITORAMENTO DE HARD SKILLS')
        print('--- MENU USUÁRIO ---')
        print('1 - Cadastrar novo usuário')
        print('2 - Acessar usuário existente')
        print('0 - Retornar')
        return int(input('Escolha uma opção: '))

    def pega_dados_usuario(self):
        print('SISTEMA DE MONITORAMENTO DE HARD SKILLS')
        print('--- CADASTRO DE USUÁRIO ---')
        id_usuario = int(input('Digite o ID do usuário: '))
        nome = input('Digite o nome do usuário: ')
        return {'id': id_usuario, 'nome': nome}

    def seleciona_carreira(self, lista_carreiras):
        print('Escolha sua carreira:')
        for carreira in lista_carreiras:
            print(f'{carreira.id} - {carreira.nome}')
        id_escolhido = int(input('Digite o ID da carreira desejada: '))
        return id_escolhido
