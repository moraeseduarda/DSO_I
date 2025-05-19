from model.carreira import Carreira
from model.projeto_pessoal import ProjetoPessoal
from model.skill import Skill
from model.status import Status, STATUS_CONCLUIDO

class Usuario():
    def __init__(self, id: int, nome: str, carreira_escolhida: Carreira, projeto: ProjetoPessoal):
        self.__id = id
        self.__nome = nome
        self.__carreira_escolhida = carreira_escolhida
        self.__skills_para_aprender = []
        self.__skills_aprendidas = []
        self.__projetos = []
        
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, id: str):
        if isinstance(id, str):
            self.__id = id
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def carreira_escolhida(self):
        return self.__carreira_escolhida

    @carreira_escolhida.setter
    def carreira_escolhida(self, carreira: Carreira):
        if isinstance(carreira, Carreira):
            self.__carreira_escolhida = carreira

    @property
    def projetos(self):
        return self.__projetos

    def add_projeto(self, projeto: ProjetoPessoal):
        if isinstance(projeto, ProjetoPessoal):
            self.__projetos.append(projeto)

    def remove_projeto(self, projeto: ProjetoPessoal):
        if projeto in self.__projetos:
            self.__projetos.remove(projeto)

    def add_skill_aprendida(self, skill: Skill):
        if isinstance(skill, Skill):
            if skill not in self.__skills_aprendidas:
                self.__skills_aprendidas.append(skill)
                if skill in self.__skills_para_aprender:
                    self.__skills_para_aprender.remove(skill)
                
                if skill.nome in self.__mapa_aprendizado:
                    self.__mapa_aprendizado[skill.nome]["status"] = STATUS_CONCLUIDO.status
            else:
                print(f"A Skill '{skill.nome}' foi aprendida.")

    def remove_skill_aprendida(self, skill: Skill):
        if skill in self.__skills_aprendidas:
            self.__skills_aprendidas.remove(skill)
        else:
            print(f"A Skill '{skill.nome}' não está na lista de skills aprendidas.")

    def percentual_skills_concluidas(self):
        total_skills = len(self.__carreira_escolhida.listar_skills()) 
        if total_skills == 0:
            return 0
        return (len(self.__skills_aprendidas) / total_skills) * 100

    def inicializa_mapa(self, status: Status, nivel_proficiencia):
        """Inicializa o mapa de aprendizado com status e nível de proficiência."""
        for skill in self.__carreira_escolhida.listar_skills():
            self.__mapa_aprendizado[skill] = {
                "nome": skill, 
                "status": status.status,
                "nivel_proficiencia": nivel_proficiencia.descricao
            }

    def encontrar_skill_no_mapa(self, nome_skill: str):
        """Encontra uma skill no mapa de aprendizado e retorna valores legíveis."""
        skill_info = self.__mapa_aprendizado.get(nome_skill, None)
        if skill_info:
            return {
                "nome": nome_skill,
                "status": skill_info["status"],
                "nivel_proficiencia": skill_info["nivel_proficiencia"]
            }
        return None

    def listar_skills_no_mapa(self):
        """Lista todas as skills no mapa de aprendizado."""
        if not self.__mapa_aprendizado:
            print("O mapa de aprendizado está vazio ou não foi inicializado.")
            return

        for skill_nome, skill_info in self.__mapa_aprendizado.items():
            print(f"Skill: {skill_nome}, Status: {skill_info['status']}, Nível: {skill_info['nivel_proficiencia']}")

    def __str__(self):
        return (
            f"Usuário: {self.nome} (ID: {self.id})\n"
            f"Carreira Escolhida: {self.__carreira_escolhida.nome}\n"
            f"Skills para Aprender: {[skill.nome for skill in self.__skills_para_aprender]}\n"
            f"Skills Concluídas: {[skill.nome for skill in self.__skills_aprendidas]}\n"
            f"Projetos: {[projeto.nome for projeto in self.__projetos]}\n"
            f"Percentual de Skills Concluídas: {self.percentual_skills_concluidas():.2f}%"
        )
