from enum import Enum
from random import randint
from math import floor, ceil

class ProtectionTypes(Enum):
    DEFAULT = 'protection'
    PROJECTILE = 'projectile_protection'
    SUB = 'subprotection'

class Enchant:
    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level

    def __str__(self) -> str:
        return f"{self.name} enchant at level {self.level}"

    def __repr__(self) -> str:
        return f"Enchant {self.name}, level = {self.level}"
    
    
class Enchants:
    def __init__(self) -> None:
        self.all: list[Enchant] = []
        
    def add_enchant(self, enchant: Enchant) -> None:
        self.all.append(enchant)
        setattr(self, enchant.name, Enchant)

    def remove_enchant(self, enchant_name: str) -> None:
        self.all = [x for x in self.all if x.name != enchant_name]
        delattr(self, enchant_name)
        
def random_round(value: int | float, flooring_chance: int) -> int:
    """
    `flooring_chance` is in range 1...100
    
    `ceiling_chance` is automatically calculated out of `flooring_chance`
    """
    random_chance = randint(1, 100)
    
    if random_chance in range(1, flooring_chance+1):
        return floor(value)
    else:
        return ceil(value)