from typing import Literal, Self
from copy import deepcopy
from random import randint
from src.ctypes import T
from settings.default import (
    MAX_HEALTH,
    MAX_PROTECTION,
    MAX_SUBPROTECTION,
    MAX_PROJECTILE_PROTECTION,
    MAX_DAMAGE,
    INIT_ACTIVE_INV_SIZE,
    INIT_INV_SIZE,
    INIT_MINI_MAX_SIZE,
    PROTECTION_MODIFIER,
    PROJECTILE_PROTECTION_MODIFIER,
    SUBPROTECTION_MODIFIER,
    GAME_OVER_TEXT
)
from src.classes.items import Item, ItemState
from src.exceptions import (
    PlayerAlreadyExist,
    InventoryIsFull,
    InventoryWillBeFull,
    IncorrectArgument,
    RoomAlreadyOpen,
    DontHaveRequiredItem
)
from src.utils2 import key_format_name
import os


class Entity:
    # TODO: When loading back from /settings/storage.json, all static variables have to be updated
    __instances: list[Self] = []
    __last_id: int = 0

    def __init__(
            self, 
            name: str,
            health: int, 
            protection: int = 0, 
            subprotection: int = 0, 
            projectile_protection: int = 0,
            damage: int = 0,
        ) -> None:
        
        self.id = Entity.__last_id + 1
        self.name = name
        self.__health = health
        self.__protection = protection
        self.__subprotection = subprotection
        self.__projectile_protection = projectile_protection
        self.__damage = damage

        Entity.__instances.append(self)
        Entity.__last_id + 1

    def __str__(self) -> str:
        return f"<Entity> {self.name} with id = {self.id}"

    def __repr__(self) -> str:
        return f"<Entity> {self.name=}, {self.id=}, {self.health=}, {self.protection=}, {self.subprotection}, {self.projectile_protection}, {self.damage=}"

    @property
    def health(self):
        return self.__health
    @property
    def protection(self):
        return self.__protection
    @property
    def subprotection(self):
        return self.__subprotection
    @property
    def projectile_protection(self):
        return self.__projectile_protection
    @property
    def damage(self):
        return self.__damage
    
    @health.setter
    def health(self, value: int): 
        if value <= 0:
            os.system('cls')
            print(GAME_OVER_TEXT)
            exit(1)
        if value <= MAX_HEALTH: self.__health = value
    @protection.setter
    def protection(self, value: int): 
        if value <= MAX_PROTECTION: self.__protection = value
    @subprotection.setter
    def subprotection(self, value: int): 
        if value <= MAX_SUBPROTECTION: self.__subprotection = value
    @projectile_protection.setter
    def projectile_protection(self, value: int): 
        if value <= MAX_PROJECTILE_PROTECTION: self.__projectile_protection = value
    @damage.setter
    def damage(self, value: int): 
        if value <= MAX_DAMAGE: self.__damage = value
        
    @classmethod
    def kill_entity(cls, entity: Self) -> None:
        cls.__instances = [x for x in cls.__instances if x != entity]
        
class Mini(Entity):
    __instances: list[Self] = []
    
    def __init__(
            self, 
            name: str, 
            health: int, 
            protection: int = 0, 
            subprotection: int = 0, 
            projectile_protection: int = 0, 
            damage: int = 0,
            level: int = 1,
        ) -> None:
        
        super().__init__(name, health, protection, subprotection, projectile_protection, damage)
        
        self.level = level
        
        Mini.__instances.append(self)
    
class Player(Entity):
    # NOTE: goes first, because of dependencies in bosses. Achievements should be stored as a list of strings rather than copies of bosses or other entities
    
    __instance_created = False
    
    def __init__(
            self, 
            name: str, 
            health: int, 
            protection: int = 0, 
            subprotection: int = 0, 
            projectile_protection: int = 0, 
            damage: int = 1,
            active_inventory: list[Item] = [] # if i want to add some default items here in the future
        ) -> None:
        
        if Player.__instance_created: 
            raise PlayerAlreadyExist('Player has already been initialized and second instance of player cannot be created.')
        
        super().__init__(name, health, protection, subprotection, projectile_protection, damage)
        
        self.nutrition = 1
        self.gold_coins = 0
        self.minis: list[Mini] = []
        self.mini_max: int = INIT_MINI_MAX_SIZE
        self.active_inventory = active_inventory
        self.inventory: list[Item] = []
        self.holding_item = active_inventory[0]
        self.holding_item_index = self.active_inventory.index(self.holding_item)
        self.crafting_tier: int = 0
        self.player_inv_size: int = INIT_INV_SIZE
        self.player_active_inv_size: int = INIT_ACTIVE_INV_SIZE
        self.open_rooms_id: list[int] = []
        
        Player.__instance_created = True
        
    def give_reward(self, amount: int) -> None:
        self.gold_coins += amount
        
    def add_mini(self, mini: Mini) -> None:
        self.minis.append(mini)
        
    def add_items_to_inventory(self, *items: Item) -> None:
        if len(self.inventory) == self.player_inv_size:
            raise InventoryIsFull("Player's inventory is full and no more item can be added")
        
        if len(self.inventory) + len(items) > self.player_inv_size:
            raise InventoryWillBeFull('Inventory will be overflowed, thus nothing was added')
        
        for item in items:
            item.state = ItemState.PASSIVE
            
        self.inventory.extend(list(items))
    
    def has(self, arg: Item | str) -> bool:
        """
        `arg`:
            - Item: will check whether the class itself in inventory
            - str: will check item by name whether it is in inventory
        """
        if isinstance(arg, Item):
            combined_inventory = deepcopy(self.inventory)
            combined_inventory.extend(self.active_inventory)

            return arg in combined_inventory
        elif isinstance(arg, str):
            combined_names = [x.name for x in self.inventory]
            combined_names.extend([x.name for x in self.active_inventory])
            
            return arg in combined_names
        else:
            raise IncorrectArgument(f"You can't argument type of {type(arg)}")
    
    def delete_item(self, arg: Item | str) -> None:
        """
        `arg`:
            - Item: will check whether the class itself in inventory
            - str: will check item by name whether it is in inventory
        """

        if isinstance(arg, Item):
            if arg in self.active_inventory:
                self.active_inventory.remove(arg)
            elif arg in self.inventory:
                self.inventory.remove(arg)
            else:
                raise IncorrectArgument(f"Can't delete {arg.name} from player's inventory: it doesn't exist in the player's inventory")
        elif isinstance(arg, str):
            active_names = [x.name for x in self.active_inventory]
            passive_names = [x.name for x in self.inventory]
            if arg in active_names:
                self.active_inventory.pop(active_names.index(arg))
            elif arg in passive_names:
                self.inventory.pop(passive_names.index(arg))
            else:
                raise IncorrectArgument(f"Can't delete {arg} from player's inventory: it doesn't exist in the player's inventory")
        else:
            raise IncorrectArgument(f"You can't argument type of {type(arg)}")

    def get_active_items(self) -> str:
        listed_items_with_index: list[str] = []
        
        for index, item in enumerate(self.active_inventory):
            prefix = ""
            
            if index == self.holding_item_index:
                prefix = '-> '
            else:
                prefix = '   '
                
            listed_items_with_index.append(f'{prefix}[{index+1}] {item.name}')
            
        return "\n".join(listed_items_with_index)
    
    def open_room(self, room_id: int, room_tier: int) -> None:
        if self.has(key_format_name(room_tier)):
            self.open_rooms_id.append(room_id)
            self.delete_item(key_format_name(room_tier))
        else:
            raise DontHaveRequiredItem(f'Player doesn\'t have required item to enter room: {key_format_name(room_tier)}')
        
    def take_damage(self, mob_type: Literal['boss', 'mobs'], *, mob_damage: int = None, mob_count: int = None, boss_damage: int = None) -> int:
        match mob_type:
            case 'boss':
                if boss_damage is None:
                    raise SyntaxError('Player.take_damage: need to specify boss damage integer')
                
                protection = (PROTECTION_MODIFIER * self.protection) or 1
                projectile_protection = (PROJECTILE_PROTECTION_MODIFIER * self.projectile_protection) or 1

                amount = round(( 
                    boss_damage * protection +
                    boss_damage * projectile_protection
                ))
                
                self.health -= amount

                return amount
                
            case 'mobs':
                if mob_count is None or mob_damage is None:
                    raise SyntaxError(f'Player.take_damage: need to specify mob damage or count integer ({mob_count=}, {mob_damage=})')

                protection = PROTECTION_MODIFIER * self.protection or 1

                amount = round(( 
                    mob_damage * protection * mob_count
                ))
                
                print(amount, mob_damage, protection, mob_count)
                
                self.health -= amount

                return amount

            case _:
                raise SyntaxError(f'Player.take_damage: mob_type - unknown literal ({mob_type})')

class Mob(Entity):
    def __init__(
            self, 
            name: str, 
            health: int, 
            loot: list[Item],
            protection: int = 0, 
            subprotection: int = 0, 
            projectile_protection: int = 0, 
            damage: int = 0,
            reward_gold_coins: int = 1
        ) -> None:
        
        super().__init__(name, health, protection, subprotection, projectile_protection, damage)
    
        self.reward_gold_coins = reward_gold_coins
        self.loot = loot
    
    def killself(self, player: Player) -> None:
        Entity.kill_entity(self)
        
        player.give_reward(self.reward_gold_coins)
        
        del self
        
    def create_alike(self) -> Self:
        return deepcopy(self)
    
    @staticmethod
    def replicate_mob(mob: Self, times: int) -> list[Self]:
        ret: list[Self] = []
        for _ in range(times):
            ret.append(deepcopy(mob))
            
        return ret
        
    
class Boss(Mob):
    def __init__(
            self, 
            name: str, 
            health: int, 
            loot: list[Item],
            protection: int = 0, 
            subprotection: int = 0, 
            projectile_protection: int = 0, 
            damage: int = 0,
            reward_gold_coins_range: list[int] = [0, 1]
        ) -> None:
        
        super().__init__(name, health, protection, subprotection, projectile_protection, damage)
        
        self.reward_gold_coins = reward_gold_coins_range
        self.loot = loot
        
    def killself(self, player: Player) -> str:
        Entity.kill_entity(self)
        
        
        player.give_reward(randint(self.reward_gold_coins_range[0], self.reward_gold_coins[1]))
        
        del self
        
        return f'The {self.name} has been defeated!'

    # TODO: also add projectile_ and sub_ damages. The damage given to a boss is influenced by protection level and nutrition of a player
    