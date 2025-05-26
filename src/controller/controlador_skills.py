from model.skill import Skill
from view.tela_skill import TelaSkill
from model.material_estudo import MaterialEstudo


class ControladorSkill:

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
                [],  
            )
            self.__skills.append(nova_skill)
            self.__tela_skill.mostra_mensagem('Skill cadastrada com sucesso')
            print('\n')
        else:
            self.__tela_skill.mostra_mensagem('SKILL COM ESSE ID JÁ CADASTRADA')

    def lista_skill(self):
        if not self.__skills:
            self.__tela_skill.mostra_mensagem("Nenhuma skill cadastrada!")
            return
            
        for skill in self.__skills:
            self.__tela_skill.mostra_skill({
                'id': skill.id,
                'nome': skill.nome,
                'descricao': skill.descricao,
                'material_estudo': skill.material_estudo,
                'carreiras': skill.carreiras  
            })
        input('\nPressione ENTER para continuar...')
        
    def excluir_skill(self):
        self.lista_skill()
        id_skill = self.__tela_skill.seleciona_skill()
        skill = self.pega_skill_por_id(id_skill)

        if skill is not None:
            self.__skills.remove(skill)
            self.__tela_skill.mostra_mensagem('Skill excluída com sucesso')
            print('\n')
        else:
            self.__tela_skill.mostra_mensagem('skill não existe.')
        
    def associar_skill_carreira(self):
        self.__tela_skill.mostra_skills_disponiveis(self.__skills)
        if not self.__skills:
            return  
        id_skill = self.__tela_skill.seleciona_skill()
        skill = self.pega_skill_por_id(id_skill)
        if not skill:
            self.__tela_skill.mostra_mensagem("Skill não encontrada!")
            return
        carreiras = self.__controlador_sistema.controlador_carreira.carreiras
        self.__tela_skill.mostra_carreiras_disponiveis(carreiras)
        if not carreiras:
            return
        id_carreira = self.__tela_skill.seleciona_carreira()
        carreira = self.__controlador_sistema.controlador_carreira.pega_carreira_por_id(id_carreira)
        if carreira:
            skill.adicionar_carreira(carreira)
            carreira.adicionar_skill(skill)
            self.__tela_skill.mostra_mensagem(f'Skill {skill.nome} adicionada à carreira {carreira.nome}')
        else:
            self.__tela_skill.mostra_mensagem("Carreira não encontrada!")

    def retornar(self):
        print("Retornando ao menu administrador...")
    
    def abre_tela(self):
        lista_opcoes = {
            1: self.incluir_skill, 
            2: self.excluir_skill, 
            3: self.lista_skill,
            4: self.adicionar_material_estudo,  
            5: self.associar_skill_carreira
        }

        while True:
            opcao = self.__tela_skill.tela_opcoes() 
            if opcao == 6: 
                self.retornar()
                break 
            
            funcao_escolhida = lista_opcoes.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_skill.mostra_mensagem("Opção inválida. Tente novamente.")

    def adicionar_material_estudo(self):
        self.lista_skill()
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
            self.__tela_skill.mostra_mensagem('Material de estudo adicionado com sucesso!')
        else:
            self.__tela_skill.mostra_mensagem('Skill não encontrada.')
