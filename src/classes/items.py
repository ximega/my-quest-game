from typing import Self
from enum import Enum, auto
from copy import deepcopy
from random import randint

from settings.default import (
    MAX_STACK_SIZE,
    MIN_DURABILITY,
)
from src.classes.enchants import Enchants



class ItemPurpose(Enum):
    """
    Listing of all purposes for items
    """
    MATERIAL = auto()
    COMBAT = auto()
    TOOL = auto()
    GENERAL = auto()
    SPELL = auto()
    POTION = auto()
    # NOTE: add more enums here
    
class ItemState(Enum):
    """
    States of items
    """
    DROPPED = auto()
    ACTIVE = auto() # being used in active bar
    PASSIVE = auto() # it means it is in inventory
    LOOT = auto() # either in chest or boss/mob
    SHOP = auto()
    QUEST = auto()
    CRAFTING = auto()
    

class Item:
    __instances: list[Self] = []

    def __init__(
            self, 
            name: str, 
            purpose: ItemPurpose, 
            state: ItemState,
            characteristics: dict[str, str | int] = None,
            number: int = 1
        ) -> None:
        
        self.name = name
        self.purpose = purpose
        self.state = state
        self.characteristics = characteristics or {
            "durability": MIN_DURABILITY
        }
        self.number = number
        self.enchants: Enchants = Enchants()

        Item.__instances.append(self)

    def __str__(self) -> str:
        return f"{self.state} <Item> {self.name} with {self.purpose} purpose"

    def __repr__(self) -> str:
        return f"{self.state} <Item> {self.name}. {self.purpose=}, Characteristics:{[x for x in self.characteristics]}"
    
    @classmethod
    def all(cls) -> list[Self]:
        return cls.__instances
    
    def update_characteristics(self, values: dict[str, str | int]) -> None:
        self.characteristics.update(values)
            
    @classmethod
    def destroy_item(cls, item: Self) -> None:
        cls.__instances = [x for x in cls.__instances if x != item]
            
    def __iadd__(self, other: Self) -> None:
        sum = self.number + other.numbe
        if sum <= MAX_STACK_SIZE:
            self.number += other.number
            
            del other
        else:
            # So, if MAX_STACK_SIZE is 100 
            # and sum adds up to 126 (64 and 62)
            # Then, first item will be maximum of 100
            # and second will equal remainder of sum and max size
            # 126 - 100 = 26. Second = 26
            remainder = sum - MAX_STACK_SIZE 
            self.number = MAX_STACK_SIZE 
            other.number = remainder
        
    @staticmethod
    def replicate_item(item: Self, times: int) -> list[Self]:
        ret: list[Self] = []
        for _ in range(times):
            ret.append(deepcopy(item))
            
        return ret
    
    @staticmethod
    def choose_one_of(item1: Self, item2: Self) -> Self:
        randnum = randint(0, 1)
        return item1 if randnum == 0 else item2