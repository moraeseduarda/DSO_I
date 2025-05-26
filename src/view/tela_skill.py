from view.console_utils import limpar_console


class TelaSkill:
    def tela_opcoes(self):
        while True:
            print('===== SISTEMA DE MONITORAMENTO DE HARD SKILLS =====')
            print('===== MENU SKILLS =====')
            print('1 - Incluir habilidade')
            print('2 - Excluir habilidade')
            print('3 - Listar habilidades')
            print('4 - Adicionar material de estudo')
            print('5 - Associar skill a carreira')
            print('0 - Retornar')
            try:
                opcao = int(input('Digite a opção desejada: '))
                if 0 <= opcao <= 5:
                    limpar_console()
                    return opcao
                else:
                    limpar_console()
                    print("Opção inválida. Digite um número entre 1 e 6.")
                    continue
            except ValueError:
                limpar_console()
                print("Entrada inválida. Digite um número.")
    
    def pega_dados_skill(self):
        print('-----HABILIDADE-----')
        while True:
            try:
                id = int(input('Digite o ID da habilidade: '))
                nome = input('Digite o nome da habilidade: ').upper()
                descricao = input('Digite a descrição da habilidade: ').upper()
                return {'id': id, 'nome': nome, 'descricao': descricao}
            except ValueError:
                print("ID inválido. Digite um número.")
    
    def pega_dados_material_estudo(self):
        print('-----MATERIAL DE ESTUDO-----')
        titulo = input('Digite o título do material: ').upper()
        descricao = input('Digite a descrição do material: ').upper()
        print('\nTipos de material:')
        print('1 - Livro')
        print('2 - Vídeo')
        print('3 - Curso')
        print('4 - Artigo')
        
        while True:
            try:
                tipo_num = int(input('Digite o tipo do material (1-4): '))
                tipos = {1: 'LIVRO', 2: 'VIDEO', 3: 'CURSO', 4: 'ARTIGO'}
                if tipo_num in tipos:
                    return {
                        'titulo': titulo,
                        'descricao': descricao,
                        'tipo': tipos[tipo_num]
                    }
                print("Opção inválida. Digite um número entre 1 e 4.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    
    def mostra_skill(self, dados_skill):
        print('\n=== DETALHES DA SKILL ===')
        print('ID:', dados_skill['id'])
        print('NOME:', dados_skill['nome'])
        print('DESCRIÇÃO:', dados_skill['descricao'])
        print('MATERIAIS DE ESTUDO:')
        if dados_skill['material_estudo']:
            for material in dados_skill['material_estudo']:
                print(f"- {material.titulo} ({material.tipo})")
        else:
            print("Nenhum material cadastrado")
        print('CARREIRAS ASSOCIADAS:')  
        if dados_skill.get('carreiras'):
            for carreira in dados_skill['carreiras']:
                print(f"- {carreira.nome}")
        else:
            print("Nenhuma carreira associada")
        print('------------------------\n')
    
    def seleciona_skill(self):
        while True:
            try:
                id = int(input('Digite o ID da habilidade: '))
                return id
            except ValueError:
                print("ID inválido. Digite um número.")
    
    def confirma_exclusao(self):
        while True:
            confirma = input('Confirma a exclusão da skill? (S/N): ').upper()
            if confirma in ['S', 'N']:
                return confirma == 'S'
            print("Digite S para confirmar ou N para cancelar.")
    
    def mostra_mensagem(self, mensagem):
        print(f"\n{mensagem}\n")

    def seleciona_carreira(self):
            while True:
                try:
                    id = int(input('\nDigite o ID da carreira desejada: '))
                    return id
                except ValueError:
                    print("ID inválido. Digite um número.")

    def mostra_carreiras_disponiveis(self, carreiras):
        print('\n=== CARREIRAS DISPONÍVEIS ===')
        if carreiras:
            for carreira in carreiras:
                print(f'ID: {carreira.id} - Nome: {carreira.nome}')
        else:
            print("Nenhuma carreira cadastrada!")
        print('---------------------------')

    def mostra_skills_disponiveis(self, skills):
        print('\n=== SKILLS DISPONÍVEIS ===')
        if skills:
            for skill in skills:
                print(f'ID: {skill.id} - Nome: {skill.nome}')
        else:
            print("Nenhuma skill cadastrada!")
        print('-------------------------')

