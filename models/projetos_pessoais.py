class ProjetosPessoais:
    """Representa um projeto pessoal. Existe associado a um Usuário."""
    def __init__(self, nome, descricao, skill_relacionada_obj):
        self.nome = nome
        self.descricao = descricao
        # **ASSOCIAÇÃO**: O projeto está associado a uma Skill.
        # A Skill existe independentemente do projeto.
        self.skill_relacionada = skill_relacionada_obj # Guarda a referência ao objeto Skill
    def __str__(self):
        skill_nome = self.skill_relacionada.nome if self.skill_relacionada else "Nenhuma"
        return f"Projeto '{self.nome}': (Associado a Skill: {skill_nome}). Contexto: {self.descricao}"
projeto1 = ProjetosPessoais('Projeto 1', 'Projeto Front End',None)
print(projeto1)