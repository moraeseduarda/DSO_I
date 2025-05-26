from model.carreira import Carreira
from view.tela_carreira import TelaCarreira


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
        print("-- Alterando uma carreira, informe o ID... --")
        id_carreira = self.__tela_carreira.seleciona_carreira()
        print()
        carreira = self.pega_carreira_por_id(id_carreira)
        
        if (carreira is not None):
            print("-- Agora, altere os campos para os valores que você deseja: --")
            novos_dados_carreira = self.__tela_carreira.pega_dados_carreira(None)
            carreira.id = novos_dados_carreira['id']
            carreira.nome = novos_dados_carreira['nome']
            carreira.descricao = novos_dados_carreira['descricao']
            self.lista_carreira()
            print()
        else:
            self.__tela_carreira.mostra_mensagem('ATENCAO: Carreira não existente')
            print()
        
    def lista_carreira(self):
        print("Listando as carreiras existentes...")
        for carreira in self.__carreiras:
            self.__tela_carreira.mostra_carreira({'id': carreira.id, 'nome': carreira.nome, 'descricao': carreira.descricao})
        print()
        
    def excluir_carreira(self):
        self.lista_carreira()
        print("-- Excluindo uma carreira, informe o ID... --")
        id_carreira = self.__tela_carreira.seleciona_carreira()
        carreira = self.pega_carreira_por_id(id_carreira)

        if carreira is not None:
            self.__carreiras.remove(carreira)
            self.lista_carreira()
        else:
            self.__tela_carreira.mostra_mensagem('Carreira não existe.')
    
    def retornar(self):
        self.__controlador_sistema.menu_administrador()
 
    def abre_tela(self):
        lista_opcoes = {1: self.cadastro_carreira, 2: self.alterar_carreira, 3: self.excluir_carreira, 4: self.lista_carreira, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_carreira.tela_opcoes()]()
