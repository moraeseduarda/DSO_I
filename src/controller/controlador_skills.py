from model.skill import Skill
from view.tela_skill import TelaSkill
from model.material_estudo import MaterialEstudo
from view.console_utils import limpar_console
from DAOs.skills_dao import SkillDAO


class ControladorSkill:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_skill = TelaSkill()
        self.__skill_dao = SkillDAO()
        self.__skills = []
    
    def pega_skill_por_id(self, id: int):
        for skill in self.__skill_dao.get_all():
            if skill.id == id:
                return skill
        return None
    
    def mostra_skill(self, skill):
        dados_skill = {
            'id': skill.id,
            'nome': skill.nome,
            'descricao': skill.descricao,
            'material_estudo': [
                {'titulo': m.titulo, 'tipo': m.tipo} for m in skill.material_estudo
            ],
            'carreiras': [c.nome for c in skill.carreiras]
        }
        self.__tela_skill.mostra_skill(dados_skill)
    
    def incluir_skill(self):
        dados_skill = self.__tela_skill.pega_dados_skill()
        if dados_skill is None: 
            return
        
        skill = self.pega_skill_por_id(dados_skill['id'])
        
        if skill is None:
            nova_skill = Skill(
                dados_skill['nome'],
                dados_skill['id'],
                dados_skill['descricao'],
                [],  
            )
            self.__skill_dao.add(nova_skill)  
            self.__tela_skill.mostra_mensagem('Skill cadastrada com sucesso\n')
        else:
            self.__tela_skill.mostra_mensagem('SKILL COM ESSE ID JÁ CADASTRADA')

    def lista_skill(self):
        skills = list(self.__skill_dao.get_all())
        if not skills:
            self.__tela_skill.mostra_mensagem("Nenhuma skill cadastrada!")
            return

        lista_dados = []
        for skill in skills:
            lista_dados.append({
                'id': skill.id,
                'nome': skill.nome,
                'descricao': skill.descricao,
                'material_estudo': [
                    {'titulo': m.titulo, 'tipo': m.tipo} for m in skill.material_estudo
                ],
                'carreiras': [c.nome for c in skill.carreiras]
            })
        self.__tela_skill.mostra_skill(lista_dados)
        self.__tela_skill.enter()
        
    def excluir_skill(self):
        self.lista_skill()
        id_skill = self.__tela_skill.seleciona_skill()
        skill = self.pega_skill_por_id(id_skill)

        if skill is not None:
            self.__skill_dao.remove(skill.id)
            self.__tela_skill.mostra_mensagem('Skill excluída com sucesso\n')
        else:
            self.__tela_skill.mostra_mensagem('skill não existe.')
        
    def associar_skill_carreira(self):
        skills = list(self.__skill_dao.get_all())
        skills_simples = [{'id': skill.id, 'nome': skill.nome} for skill in skills]
        self.__tela_skill.mostra_skills_disponiveis(skills_simples)
        if not skills:
            return
        id_skill = self.__tela_skill.seleciona_skill()
        skill = self.pega_skill_por_id(id_skill)
        if not skill:
            self.__tela_skill.mostra_mensagem("Skill não encontrada!")
            return
        carreiras = self.__controlador_sistema.controlador_carreira.get_carreiras() 

        carreiras_simples = [{'id': c.id, 'nome': c.nome} for c in carreiras]
        self.__tela_skill.mostra_carreiras_disponiveis(carreiras_simples)

        if not carreiras:
            return
        id_carreira = self.__tela_skill.seleciona_carreira()
        carreira = self.__controlador_sistema.controlador_carreira.pega_carreira_por_id(id_carreira)
        if carreira:
            skill.adicionar_carreira(carreira)
            carreira.adicionar_skill(skill)
            self.__skill_dao.update(skill)  # Atualiza no DAO
            self.__tela_skill.mostra_mensagem(f'Skill {skill.nome} adicionada à carreira {carreira.nome}')
        else:
            self.__tela_skill.mostra_mensagem("Carreira não encontrada!")

    def mostra_carreira_disponiveis(self):
        id_carreira = self.__tela_skill.seleciona_carreira()
        carreira = self.__controlador_sistema.controlador_carreira.pega_carreira_por_id(id_carreira)
        if carreira is None:
            self.__tela_carreira.mostra_mensagem("Carreira não encontrada.")
            return
        dados_carreira = {
        "id": carreira.id,
        "nome": carreira.nome,
        "descricao": carreira.descricao,
        # ... outros campos necessários
        }
        self.__controlador_sistema.controlador_carreira.tela_carreira.mostra_carreira(dados_carreira)
    
    def abre_tela(self):
        while True:
            lista_opcoes = {
                1: self.incluir_skill, 
                2: self.excluir_skill, 
                3: self.lista_skill,
                4: self.adicionar_material_estudo,  
                5: self.associar_skill_carreira
            }
            opcao = self.__tela_skill.tela_opcoes() 
            if opcao == 0: 
                self.__tela_skill.retornar()
                break 
            try:
                funcao_escolhida = lista_opcoes.get(opcao)
                try:
                    funcao_escolhida()
                except KeyError:
                    self.__tela_skill.mostra_mensagem("Opção inválida. Tente novamente.")
            except ValueError:
                limpar_console()
                self.__tela_skill.mostra_mensagem("Entrada inválida. Digite apenas números.")

    def adicionar_material_estudo(self):
        id_skill = self.__tela_skill.seleciona_skill()
        skill = self.pega_skill_por_id(id_skill)
        if skill:
            dados_material = self.__tela_skill.pega_dados_material_estudo()
            material = MaterialEstudo(
                dados_material['titulo'],
                dados_material['descricao'],
                dados_material['tipo']
            )
            skill.adicionar_material_estudo(material)
            self.__skill_dao.update(skill)  # Atualiza no DAO
            self.__tela_skill.mostra_mensagem('Material de estudo adicionado com sucesso!')
        else:
            self.__tela_skill.mostra_mensagem('Skill não encontrada.')
