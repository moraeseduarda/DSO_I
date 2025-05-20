from model.skill import Skill
from view.tela_skill import TelaSkill


class ControladorSkill():
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_skill = TelaSkill()
        self.__skills = []
    
    def pega_skill_por_id(self, id: int):
        for skill in self.__skills:
            if skill.id == id:
                return skill
        return None
    
    def incluir_skill(self):
        dados_skill = self.__tela_skill.pega_dados_skill()
        skill = self.pega_skill_por_id(dados_skill['id'])
        
        if skill is None:
            nova_skill = Skill(
                dados_skill['nome'],
                dados_skill['id'],
                dados_skill['descricao'],
                [],    # material_estudo vazio
                None   # nivel_proficiencia vazio
            )
            self.__skills.append(nova_skill)
            self.__tela_skill.mostra_mensagem('Skill cadastrada com sucesso')
            print('\n')
        else:
            self.__tela_skill.mostra_mensagem('SKILL JÁ CADASTRADA')

    def alterar_skill(self):
            self.lista_skill()
            id_skill = self.__tela_skill.seleciona_skill()
            skill = self.pega_skill_por_id(id_skill)
            
            if (skill is not None):
                novos_dados_skill = self.__tela_skill.pega_dados_skill()
                skill.id = novos_dados_skill['id']
                skill.nome = novos_dados_skill['nome']
                skill.descricao = novos_dados_skill['descricao']
                self.lista_skill()
            else:
                self.__tela_skill.mostra_mensagem('ATENCAO: skill não existente')

    def lista_skill(self):
            for skill in self.__skills:
                self.__tela_skill.mostra_skill({
                    'id': skill.id,
                    'nome': skill.nome,
                    'descricao': skill.descricao,
                    'material_estudo': skill.material_estudo,
                    'nivel_proficiencia': skill.nivel_proficiencia
                })
            
    def excluir_skill(self):
        self.lista_skill()
        id_skill = self.__tela_skill.seleciona_skill()
        skill = self.pega_skill_por_id(id_skill)

        if skill is not None:
            self.__skills.remove(skill)
            self.lista_skill()
        else:
            self.__tela_skill.mostra_mensagem('skill não existe.')
        
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_skill, 2: self.alterar_skill, 3: self.excluir_skill, 4: self.lista_skill, 5: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_skill.tela_opcoes()]()
