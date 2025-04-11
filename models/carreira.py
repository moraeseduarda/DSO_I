# Classe 7: Carreira
# **HERANÇA**: Carreira É-UM tipo de Cadastro.
from cadastro import Cadastro
class Carreira(Cadastro):
    """Representa uma carreira profissional. Existe independentemente."""
    def __init__(self, nome, id_unico):
        super().__init__(nome, id_unico)
        # **AGREGAÇÃO**: Carreira AGREGA (tem) Skills.
        # As Skills existem independentemente da Carreira.
        self.skills_requeridas = [] # Guarda referências a objetos Skill

    # Método essencial para adicionar skills de forma controlada
    def adicionar_skill(self, skill):
        if isinstance(skill, Skill):
            if skill not in self.skills_requeridas:
                self.skills_requeridas.append(skill)
        else:
            print(f"Erro: Só adicionar objetos Skill à carreira {self.nome}.")

    def __str__(self):
        return f"Carreira: {self.nome} (ID: {self.id_unico})"