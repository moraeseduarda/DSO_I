from model.abstract_pessoa_sistema import PessoaSistema
from model.carreira import Carreira
from model.projeto_pessoal import ProjetoPessoal  


class Usuario(PessoaSistema):
    def __init__(self, username: str, nome: str):
        super().__init__(username)
        self.__nome = nome
        self.__carreiras = []
        self.__skills_para_aprender = [] 
        self.__skills_aprendidas = []   
        self.__projetos_pessoais = {}   
        
    @property
    def username(self):
        return super().username
    
    @username.setter
    def username(self, username: str):
        super().username = username
            
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            raise TypeError("nome deve ser do tipo string")

    @property
    def carreiras(self):
        return self.__carreiras
    
    @carreiras.setter 
    def carreiras(self, carreiras):
        if isinstance(carreiras, list):
            self.__carreiras = carreiras
        else:
            raise TypeError("carreiras deve ser uma lista")
    
    @property
    def skills_para_aprender(self):
        return self.__skills_para_aprender
    
    @skills_para_aprender.setter
    def skills_para_aprender(self, skills):
        if isinstance(skills, list):
            self.__skills_para_aprender = skills
        else:
            raise TypeError("skills_para_aprender deve ser uma lista")

    @property
    def skills_aprendidas(self):
        return self.__skills_aprendidas
    
    @skills_aprendidas.setter
    def skills_aprendidas(self, skills):
        if isinstance(skills, list):
            self.__skills_aprendidas = skills
        else:
            raise TypeError("skills_aprendidas deve ser uma lista")

    @property
    def projetos_pessoais(self):
        """Retorna uma LISTA dos objetos ProjetoPessoal."""
        return list(self.__projetos_pessoais.values())

    @projetos_pessoais.setter
    def projetos_pessoais(self, lista_de_projetos):
        """Define a lista de projetos pessoais.
        Espera uma lista de objetos ProjetoPessoal.
        """
        if not isinstance(lista_de_projetos, list):
            raise TypeError("projetos_pessoais deve ser uma lista de objetos ProjetoPessoal.")

        # Limpa o dicionário existente, mantendo a referência
        self.__projetos_pessoais.clear()
        for projeto in lista_de_projetos:
            if isinstance(projeto, ProjetoPessoal):
                self.__projetos_pessoais[projeto.nome] = projeto
            else:
                raise TypeError(f"Aviso: Item '{projeto}' na lista não é um objeto ProjetoPessoal e foi ignorado.")

    def exibir_informacoes(self):
        return f"Usuário: {self.nome}"
    
    def encontrar_projeto_na_lista(self, lista_projetos, nome_projeto):
        for proj in lista_projetos:
            if proj.nome == nome_projeto:
                return proj
        return None
