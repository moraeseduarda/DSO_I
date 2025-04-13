from models.carreira import Carreira
from models.skill import Skill
from models.nivel_proficiencia import NivelProficiencia
from models.material_estudo import MaterialEstudo
from models.projetos_pessoais import ProjetosPessoais
from models.status import Status

# Criando instâncias de Status
STATUS_NAO_INICIADO = Status("Não Iniciado")
STATUS_EM_PROGRESSO = Status("Em Progresso")
STATUS_APRENDIDO = Status("Aprendido")

# Criando instâncias de NivelProficiencia
nivel_avancado = NivelProficiencia(descricao="Avançado")
nivel_intermediario = NivelProficiencia(descricao="Intermediário")
nivel_basico = NivelProficiencia(descricao="Básico")

# Criando instâncias de MaterialEstudo
material1 = MaterialEstudo(titulo="Livro de Python", descricao="Um guia completo sobre Python", tipo="Livro")
material2 = MaterialEstudo(titulo="Curso Online", descricao="Curso interativo de Python", tipo="Curso")
material3 = MaterialEstudo(titulo="Documentação Java", descricao="Documentação oficial do Java", tipo="Documento")

# Criando instâncias de Skill
skill_python = Skill(nome="Python", id=1, descricao="Linguagem de programação", material_estudo=[], nivel_proficiencia=nivel_intermediario)
skill_java = Skill(nome="Java", id=2, descricao="Linguagem de programação", material_estudo=[], nivel_proficiencia=nivel_avancado)

# Adicionando materiais de estudo às skills
skill_python.adicionar_material(material1)
skill_python.adicionar_material(material2)
skill_java.adicionar_material(material3)

# Criando uma instância de Carreira
carreira_dev = Carreira(nome="Desenvolvedor de Software", id=101, descricao="Carreira focada em desenvolvimento de software.")

# Adicionando skills à carreira
carreira_dev.adicionar_skill(skill_python)
carreira_dev.adicionar_skill(skill_java)

# Criando instâncias de ProjetosPessoais
projeto1 = ProjetosPessoais(nome="Projeto 1", descricao="Projeto Front End", skill_relacionada_obj=skill_python, status=STATUS_NAO_INICIADO)
projeto2 = ProjetosPessoais(nome="Projeto 2", descricao="Projeto Back End", skill_relacionada_obj=skill_java, status=STATUS_EM_PROGRESSO)

# Exibindo os objetos criados
print("=== Carreira ===")
print(carreira_dev)

print("\n=== Skills ===")
print(skill_python)
print(skill_java)

print("\n=== Projetos Pessoais ===")
print(projeto1)
print(projeto2)