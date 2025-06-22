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
        for carreira in self.__carreiras:
            if carreira.id == id:
                return carreira
        return None

    def cadastro_carreira(self):
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
        if not self.__carreiras:
            self.__tela_carreira.mostra_mensagem("Nenhuma carreira cadastrada.\n")
            return
        self.__tela_carreira.mostra_mensagem("Listando as carreiras existentes...")
        for carreira in self.__carreiras:
            self.__tela_carreira.mostra_carreira({'id': carreira.id, 'nome': carreira.nome, 'descricao': carreira.descricao})
        
    def excluir_carreira(self):
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
            try:
                opcao = self.__tela_carreira.tela_opcoes()
                if opcao == 0:
                    self.__tela_carreira.retornar() 
                    break 
                
                funcao_escolhida = lista_opcoes.get(opcao)
                if funcao_escolhida:
                    funcao_escolhida()
                else:
                    limpar_console()
                    self.__tela_carreira.mostra_mensagem("Opção inválida. Tente novamente.")
            except ValueError:
                limpar_console()
                self.__tela_carreira.mostra_mensagem("\nEntrada inválida. Digite apenas números.")
    
    def seleciona_carreiras_por_id(self, ids_usuario):
        carreiras_encontradas = []
        for id_carreira in ids_usuario:
            carreira = next((c for c in self.__carreiras if c.id == id_carreira), None)
            if carreira and carreira not in carreiras_encontradas:
                carreiras_encontradas.append(carreira)
        return carreiras_encontradas
   
    def seleciona_ids_carreiras_existentes(self, ids_usuario):
        """
        Recebe uma lista de IDs e retorna uma lista apenas com os IDs que existem em self.__carreiras.
        """
        ids_validos = [carreira.id for carreira in self.__carreiras]
        return [id_carreira for id_carreira in ids_usuario if id_carreira in ids_validos]
   
    def listagem_carreiras(self):
        return [{"id": carreira.id, "nome": carreira.nome} for carreira in self.__carreiras]
    
    def cadastro_usuario_carreiras(self):
        self.lista_carreira()
        self.__tela_carreira.escolha_carreiras()
        ids_selecionados_usuario = self.__tela_carreira.seleciona_carreiras()
        ids_carreiras = self.seleciona_ids_carreiras_existentes(ids_selecionados_usuario)

        self.__tela_menu_usuario.mostra_mensagem("Carreiras que você selecionou: ")
        carreiras_usuario = self.seleciona_carreiras_por_id(ids_selecionados_usuario)
        self.printar(carreiras_usuario)
            # Buscar objetos Carreira válidos (sem duplicatas)
        carreiras_escolhidas = []
        for id in ids_carreiras:
            carreira = self.pega_carreira_por_id(id)
            if carreira and carreira not in carreiras_escolhidas:
                carreiras_escolhidas.append(carreira)
        
        return