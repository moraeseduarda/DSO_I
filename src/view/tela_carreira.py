from view.console_utils import limpar_console


class TelaCarreira:    
    def tela_opcoes(self):
        print('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')
        print('--- CARREIRAS ---')
        print('Escolha uma opção:')
        print('1 - Cadastrar nova carreira')
        print('2 - Alterar carreira existente')
        print('3 - Excluir uma carreira')
        print('4 - Listar todas as carreiras cadastradas')
        print('0 - Retornar')
        opcao = int(input('Digite a opção desejada: '))
        limpar_console()
        return opcao
    
    def pega_dados_carreira(self, cadastro):
        if cadastro:
            print('---------- CADASTRO CARREIRA ----------')
        else:
            print('---------- CARREIRA ----------')
        id = int(input('Digite o ID da carreira: '))
        nome = input('Digite o nome da carreira: ').upper()
        descricao = input('Digite a descrição da carreira: ').upper()
        return {'id': id, 'nome': nome, 'descricao': descricao}
    
    
    def mostra_lista_carreiras(self, lista_carreiras):
        print("\n--- Lista de Carreiras ---")
        for carreira in lista_carreiras:
            print(f"ID: {carreira['id']}")
            print(f"Nome: {carreira['nome']}")
            print(f"Descrição: {carreira['descricao']}")
            print("------------------------------")
        print()

    
    def seleciona_carreira(self):
        id = int(input('Digite o ID da carreira: '))
        return id
    
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}\n")

    def mensagem_inicio_alteracao(self):
        print("-- Alterando uma carreira, informe o ID... --")

    def mensagem_altere_campos(self):
        print("-- Agora, altere os campos para os valores que você deseja: --")
        
    def retornar(self):
        print("Retornando ao menu administrador...")