from model.carreira import Carreira
from view.tela_carreira import TelaCarreira

class ControladorCarreira():
    
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_carreira = TelaCarreira()
        self.__carreiras = []

    def pega_carreira_por_id(self, id: int):
        for carreira in self.__carreiras:
            if carreira.id == id:
                return carreira
        return None
    
    def incluir_carreira(self):
        dados_carreira = self.__tela_carreira.pega_dados_carreira()
        nova_carreira = Carreira(dados_carreira['id'], dados_carreira['nome'], dados_carreira['descricao'])
        self.__carreiras.append(nova_carreira)
        self.__tela_carreira.mostra_mensagem('Carreira cadastrada com sucesso!')
    
    def alterar_carreira(self):
        self.__carreiras
        
    def lista_carreira(self):
        for carreira in self.__carreiras:
            self.__tela_carreira.mostra_carreira({'id': carreira.id, 'nome': carreira.nome, 'descricao': carreira.descricao})
        if self.__carreiras == []:
            self.__tela_carreira.mostra_mensagem('Nenhuma carreira cadastrada!')
        
    def excluir_carreira(self):
        self.lista_carreira()
        id_carreira = self.__tela_carreira.seleciona_carreira()
        carreira = self.pega_carreira_por_id(id_carreira)
        
        if carreira is not None:
            self.__carreiras.remove(carreira)
            self.lista_carreira()
        else:
            self.__tela_carreira.mostra_mensagem('Carreira não exite.')
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()
        
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_carreira, 2: self.alterar_carreira, 3: self.lista_carreira, 4: self.excluir_carreira, 0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__tela_carreira.tela_opcoes()]()
            