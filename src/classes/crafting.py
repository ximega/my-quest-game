from typing import Self
from enum import Enum, auto
from src.classes.items import Item, ItemPurpose, ItemState
from src.classes.entities import Player
from src.exceptions import (
    NoRequiredIngridients,
    UnnecessaryIngridients,
    CraftingErrorRecipe,
)


class RepairStatus(Enum):
    COMPLETELY_BROKEN = auto()
    BROKEN = auto()
    OUT_OF_WORK = auto()
    BARELY_WORKING = auto()
    SLIGHTLY_DAMAGES = auto()
    FINE = auto()
    NEW = auto()

class ItemRecipe:
    __instances: list[Self] = []
    
    def __init__(self, *items: str, output: str, output_purpose: ItemPurpose, time: int, tier: int, machine: "Machine") -> None:
        """ 
        Must specify arguments item when creating an instance, since *items will take all arguments as a list to itself
        
        `time`: time specified in seconds
        """
        self.ingridients = items
        self.output = output
        self.output_purpose = output_purpose
        self.time = time
        self.tier = tier
        self.machine = machine
        
        ItemRecipe.__instances.append(self)
        
    def __str__(self) -> str:
        return f"Recipe of {self.output} made out of {[x for x in self.ingridients]} takes {self.time}s in {self.machine} (required tier - {self.tier})"

    def __repr__(self) -> str:
        return f"Recipe of {self.output} made out of {[x for x in self.ingridients]} takes {self.time}s in {self.machine} (required tier - {self.tier})"
        
class Machine:
    def __init__(
            self, 
            name: str,
            slots_number: int,
            repair_status: RepairStatus = RepairStatus.NEW,
            times_used: int = 0
        ) -> None:

        self.name = name
        self.slots_number = slots_number
        self.repair_status = repair_status
        self.times_used = times_used
        self.recipies: list[ItemRecipe] = []
        self.is_unlocked: bool = False
        
    def __str__(self) -> str:
        return self.name
        
    def update_recipies(self, *recepies: ItemRecipe) -> None:
        self.recipies.extend(list(recepies))
        
    def show_available_recipies(self, *items: Item) -> list[ItemRecipe]:
        sorted_recipies: list[ItemRecipe] = []
        
        if len(items) < 1: return
        
        for recipe in self.recipies:
            this_item_not_in_ingridients: bool = False
        
            for item in items:
                if item.name not in recipe.ingridients:
                    this_item_not_in_ingridients = True
                    break
            
            if this_item_not_in_ingridients: 
                break
            
            sorted_recipies.append(recipe)
            
        return sorted_recipies
        
    def craft(self, *items: Item, recipe: ItemRecipe, times: int, player: Player) -> Item:        
        if len(items) > len(recipe.ingridients):
            raise UnnecessaryIngridients('Player liad/used/put too many ingidients into a crafting')
        if len(items) < len(recipe.ingridients):
            raise NoRequiredIngridients("Player didn't put all required ingridients")
        for item in items:
            if item not in recipe.ingridients: 
                raise UnnecessaryIngridients(f'{item.name} isn\'t neccesary in this crafting')
        
        for item in items: del item
        
        player.add_items_to_inventory(Item(recipe.output, recipe.output_purpose, ItemState.PASSIVE, number = times))
        
    def unlock_to_player(self) -> None:
        self.is_unlocked = True
        