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
        username_usuario = input('Digite o USERNAME do usuário: @').strip().lower()
        nome = input('Digite o nome do usuário: ').upper()
        return {'username': username_usuario, 'nome': nome}

    def mostra_mensagem(self, mensagem):
        print(mensagem)
        
    def seleciona_carreiras(self, lista_carreiras):
        ids_validos = [carreira.id for carreira in lista_carreiras]

        while True:
            print('\n📌 Escolha as carreiras (digite os IDs separados por vírgula):')
            for carreira in lista_carreiras:
                print(f'{carreira.id} - {carreira.nome}')

            entrada = input('Digite os IDs: ')
            try:
                ids_digitados = [int(id.strip()) for id in entrada.split(',')]

                if not ids_digitados:
                    print('Nenhum ID informado. Tente novamente.\n')
                    continue

                if any(id_invalido not in ids_validos for id_invalido in ids_digitados):
                    print('Um ou mais IDs inválidos. Tente novamente.\n')
                    continue

                if len(ids_digitados) != len(set(ids_digitados)):
                    print('IDs duplicados informados. Por favor, informe apenas IDs únicos.\n')
                    continue

                return ids_digitados

            except ValueError:
                print('Entrada inválida. Digite apenas números separados por vírgula.\n')
