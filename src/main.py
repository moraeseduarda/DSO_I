from models.carreira import Carreira
from models.skill import Skill
from models.material_estudo import MaterialEstudo
from models.projeto_pessoal import ProjetoPessoal
from models.usuario import Usuario
from models.status import STATUS_NAO_INICIADO, STATUS_EM_PROGRESSO
from models.nivel_proficiencia import NIVEL_BASICO, NIVEL_INTERMEDIARIO

# Criando instâncias de MaterialEstudo
material1 = MaterialEstudo(titulo="Livro de Python", descricao="Um guia completo sobre Python", tipo="Livro")
material2 = MaterialEstudo(titulo="Curso Online", descricao="Curso interativo de Python", tipo="Curso")
material3 = MaterialEstudo(titulo="Documentação Java", descricao="Documentação oficial do Java", tipo="Documento")

# Criando instâncias de Skill
skill_python = Skill(nome="Python", id=1, descricao="Linguagem de programação", material_estudo=[], nivel_proficiencia=NIVEL_BASICO)
skill_java = Skill(nome="Java", id=2, descricao="Linguagem de programação orientada a objetos", material_estudo=[], nivel_proficiencia=NIVEL_INTERMEDIARIO)

# Adicionando materiais de estudo às skills
skill_python.adicionar_material(material1)
skill_python.adicionar_material(material2)
skill_java.adicionar_material(material3)

# Criando uma instância de Carreira
carreira_dev = Carreira(nome="Desenvolvedor de Software", id=101, descricao="Carreira focada em desenvolvimento de software.")
carreira_dev.adicionar_skill(skill_python)
carreira_dev.adicionar_skill(skill_java)

# Criando instâncias de ProjetosPessoais
projeto1 = ProjetoPessoal(nome="Projeto 1", descricao="Projeto Front End", skill_relacionada_obj=skill_python, status=STATUS_NAO_INICIADO)
projeto2 = ProjetoPessoal(nome="Projeto 2", descricao="Projeto Back End", skill_relacionada_obj=skill_java, status=STATUS_EM_PROGRESSO)

# Criando uma instância de Usuario
usuario1 = Usuario(id=1, nome="João", carreira_escolhida=carreira_dev, projeto=projeto1)
usuario2 = Usuario(id=2, nome="Maria", carreira_escolhida=carreira_dev, projeto=projeto2)
usuario3 = Usuario(id=3, nome="Carlos", carreira_escolhida=carreira_dev, projeto=projeto1)

# TESTES

usuario1.add_skill_aprendida(skill_python)  # João aprende Python
usuario2.add_skill_aprendida(skill_java)   # Maria aprende Java
usuario2.add_skill_aprendida(skill_python) # Maria aprende Python
usuario3.add_skill_aprendida(skill_java)

print("=== Carreiras ===")
print(carreira_dev)

print("\n=== Skills ===")
print(skill_python)
print(skill_java)

print("\n=== Projetos Pessoais ===")
print(projeto1)
print(projeto2)

# Testando adicionar e remover projetos
print("\n=== Testando Projetos ===")
usuario1.add_projeto(projeto2)
print(f"Projetos após adicionar: {[projeto.nome for projeto in usuario1.projetos]}")
usuario1.remove_projeto(projeto1)
print(f"Projetos após remover: {[projeto.nome for projeto in usuario1.projetos]}")

# Testando adicionar e remover skills aprendidas
print("\n=== Testando Skills Aprendidas ===")
usuario1.add_skill_aprendida(skill_python)
print(f"Skills aprendidas após adicionar: {[skill.nome for skill in usuario1._Usuario__skills_aprendidas]}")
usuario1.remove_skill_aprendida(skill_python)
print(f"Skills aprendidas após remover: {[skill.nome for skill in usuario1._Usuario__skills_aprendidas]}")

# Testando percentual de skills concluídas
print("\n=== Testando Percentual de Skills Concluídas ===")
percentual = usuario1.percentual_skills_concluidas()
print(f"Percentual de skills concluídas: {percentual:.2f}%")

# Testando inicialização do mapa de aprendizado
print("\n=== Testando Mapa de Aprendizado ===")
usuario1.inicializa_mapa(status=STATUS_NAO_INICIADO, nivel_proficiencia=NIVEL_BASICO)
print(f"Mapa de aprendizado inicializado: {usuario1._Usuario__mapa_aprendizado}")

# Testando encontrar skill no mapa
print("\n=== Testando Encontrar Skill no Mapa ===")
skill_info = usuario1.encontrar_skill_no_mapa("Python")
print(f"Informações da skill 'Python' no mapa: {skill_info}")

print("\n=== Usuários ===")
print(usuario1)
