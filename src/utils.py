from typing import Literal
from src.classes.enchants import ProtectionTypes, random_round
from src.exceptions import (
    IncorrectCommand,
    ItemCannotAtack,
    ProtectionTypeDoesNotExist
)
from settings.default import (
    ENCHANT_DAMAGE_RESULTING_MODIFIER,
    ENCHANT_DEFENSE_RESULTING_MODIFIER,
    ENCHANT_RESULTING_MODIFIER,
    
)
from src.classes.items import Item, ItemPurpose
from src.classes.entities import Mob, Boss, Player




def use_item(item: Item, *, mob: Mob | Boss = None, player: Player = None, protection_type: ProtectionTypes = None) -> None:
    try:    
        enchant_modifier: int = item.enchants.unbreaking.level or 0
        item.characteristics['durability'] -= 1 * (ENCHANT_RESULTING_MODIFIER * enchant_modifier)
    except KeyError:
        raise IncorrectCommand(f'use() of item {item.name} function was used incorrectly')
    
    if item.purpose == ItemPurpose.COMBAT:
        hit_modifier: int | float = (item.enchants.atack.value * ENCHANT_DAMAGE_RESULTING_MODIFIER)
        defense_modifier: int | float = (getattr(mob, protection_type) * ENCHANT_DEFENSE_RESULTING_MODIFIER)
        
        value_minus: int | float = hit_modifier * defense_modifier * item.characteristics['damage']
        
        mob.health -= random_round(value_minus)
        
        if mob.health <= 0:
            mob.killself(player)
            
# NOTE: Have to add additional 
# multipliers for spells and potions 
# when implementing them in the future

def give_damage_to_mob(mob: Mob | Boss, player: Player, atacking_item: Item, damage_type: Literal['DEFAULT', 'SUB', 'PROJECTILE']) -> None:
    if damage_type not in ['DEFAULT', 'SUB', 'PROJECTILE']: raise ProtectionTypeDoesNotExist(f"The type {damage_type} doesn't exist and can't be provided as an argument to the method Mob.damage()")
    
    if atacking_item.purpose != ItemPurpose.COMBAT: raise ItemCannotAtack(f"The item {atacking_item.name} can't be used in a combat")
    
    use_item(atacking_item, mob = mob, player = player, protection_type = getattr(ProtectionTypes, damage_type))