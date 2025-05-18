class TelaSkill:
    def tela_opcoes(self):
        print('ESCOLHA UMA OPÇÃO')
        print('1 - Incluir habilidade')
        print('2 - Alterar habilidade')
        print('3 - Excluir habilidade')
        print('4 - Listar habilidade')
        print('5 - Retornar')
        opcao = int(input('Digite a opção desejada: '))
        print('\n')
        return opcao
    
    def pega_dados_skill(self):
        print('-----HABILIDADE-----')
        id = int(input('Digite o ID da habilidade: '))
        nome = input('Digite o nome da habilidade: ')
        descricao = input('Digite a descrição da habilidade: ')
        return {'id': id, 'nome': nome, 'descricao': descricao}
    
    def mostra_skill(self, dados_skill):
        print('ID DA HABILIDADE: ', dados_skill['id'])
        print('NOME DA HABILIDADE: ', dados_skill['nome'])
        print('DESCRICAO DA HABILIDADE: ', dados_skill['descricao'])  
    
    def seleciona_skill(self):
        id = int(input('Digite o ID da habilidade: '))
        return id
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def cria_nova_skill(self, dados_skill):
        nova_skill = Skill(
            dados_skill['nome'],
            dados_skill['id'],
            dados_skill['descricao'],
            [],  
            None 
        )
        return nova_skill

