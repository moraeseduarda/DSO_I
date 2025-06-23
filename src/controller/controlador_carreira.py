from model.carreira import Carreira
from view.tela_carreira import TelaCarreira
from view.console_utils import limpar_console


class ControladorCarreira:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_carreira = TelaCarreira()
        self.__carreiras = []

    @property
    def carreiras(self):
        return self.__carreiras 

    def pega_carreira_por_id(self, id: int):
        """Pega carreira pelo seu id"""
        for carreira in self.__carreiras:
            if carreira.id == id:
                return carreira
        return None

    def cadastro_carreira(self):
        """Cadastra uma carreira e coloca na lista do controlador (carreiras)"""
        cadastro = True
        dados_carreira = self.__tela_carreira.pega_dados_carreira(cadastro)
        carreira = self.pega_carreira_por_id(dados_carreira['id'])
        if carreira is None:
            nova_carreira = Carreira(dados_carreira['id'], dados_carreira['nome'], dados_carreira['descricao'])
            self.__carreiras.append(nova_carreira)
            self.__tela_carreira.mostra_mensagem('Carreira cadastrada com sucesso!\n')
        else:
            self.__tela_carreira.mostra_mensagem("ATENCAO: Carreira já existente. Insira outro ID.\n")
            
    def alterar_carreira(self):
        """Altera uma carreira, procura por id se a carreira existe"""
        self.lista_carreira()
        self.__tela_carreira.mensagem_inicio_alteracao()
        id_carreira = self.__tela_carreira.seleciona_carreira()
        carreira = self.pega_carreira_por_id(id_carreira)
        
        if carreira is None:
            self.__tela_carreira.mostra_mensagem('ATENCAO: Carreira não existente\n')
            return  # Sai do método se não encontrar o ID

        if (carreira is not None):
            self.__tela_carreira.mensagem_altere_campos()
            novos_dados_carreira = self.__tela_carreira.pega_dados_carreira(None)
            carreira.id = novos_dados_carreira['id']
            carreira.nome = novos_dados_carreira['nome']
            carreira.descricao = novos_dados_carreira['descricao']
            self.lista_carreira()
        
    def lista_carreira(self):
        """Lista todas as carreiras cadastradas"""
        if not self.__carreiras:
            self.__tela_carreira.mostra_mensagem("Nenhuma carreira cadastrada.\n")
            return
        self.__tela_carreira.mostra_mensagem("Listando as carreiras existentes...")
        carreiras_formatadas = []
        for carreira in self.__carreiras:
            carreiras_formatadas.append({
                'id': carreira.id,
                'nome': carreira.nome,
                'descricao': carreira.descricao
            })
    
        # Envia a lista completa para a tela mostrar
        self.__tela_carreira.mostra_lista_carreiras(carreiras_formatadas)
        
    def excluir_carreira(self):
        """Exclui uma carreira, procura se a carreira existe primeiro"""
        self.lista_carreira()
        self.__tela_carreira.mostra_mensagem("-- Excluindo uma carreira, informe o ID... --")
        id_carreira = self.__tela_carreira.seleciona_carreira()
        carreira = self.pega_carreira_por_id(id_carreira)

        if carreira is not None:
            self.__carreiras.remove(carreira)
            self.lista_carreira()
        else:
            self.__tela_carreira.mostra_mensagem('Carreira não existe.')
    

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastro_carreira, 
            2: self.alterar_carreira, 
            3: self.excluir_carreira, 
            4: self.lista_carreira
        }

        while True:
            opcao = self.__tela_carreira.tela_opcoes()
            if opcao == 0:
                self.__tela_carreira.retornar() 
                break
            
            try:    
                funcao_escolhida = lista_opcoes.get(opcao)
                try:
                    funcao_escolhida()
                except KeyError:
                    self.__tela_carreira.mostra_mensagem("Opção inválida. Tente novamente.")
            except ValueError:
                self.__tela_carreira.mostra_mensagem("Entrada inválida. Digite apenas números.")

   
    def seleciona_ids_carreiras_existentes(self, ids_usuario):
        """
        Recebe uma lista de IDs e retorna apenas os IDs que existem nas carreiras cadastradas.
        """
        ids_cadastrados = [carreira.id for carreira in self.__carreiras]
        ids_validos = [id_ for id_ in ids_usuario if id_ in ids_cadastrados]
        return ids_validos