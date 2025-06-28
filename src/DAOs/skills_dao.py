from DAOs.dao import DAO
from model.skill import Skill

class SkillDAO(DAO):
    def __init__(self):
        super().__init__('skill.pkl')

    def add(self, skill: Skill):
        if (skill is not None) and isinstance(skill, Skill) and isinstance(skill.id, int):
            super().add(skill.id, skill)

    def update(self, skill: Skill):
        if (skill is not None) and isinstance(skill, Skill) and isinstance(skill.id, int):
            super().update(skill.id, skill)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)