from typing import Self, Literal
from src.constants import T, DirectionLiteral, RoomsList
from src.classes.entities import Boss, Mob, Player
from src.classes.items import Item, ItemPurpose, ItemState
from src.exceptions import (
    DontHaveRequiredItem
)
from src.utils2 import key_format_name


def generate_random_loot(tier: int) -> list[Item]:
    # TODO: implement this function for random loot, and make it default for class initialization
    if tier == 0:
        return []

    ret: list[Item] = [
        Item(key_format_name(tier), ItemPurpose.GENERAL, ItemState.LOOT)
    ]

    return ret

class Room:
    __last_id = 0
    __instances: list[Self] = []
    
    def __init__(
            self,
            boss: Boss | None,
            mobs: list[Mob] | None,
            tier: int,
        ) -> None:
        
        self.id = Room.__last_id + 1
        self.boss = boss
        self.mobs = mobs
        self.tier = tier
        self.loot = generate_random_loot(self.tier)
        self.is_open = self.id == 1
        self.next_rooms: RoomsList = []
        
        Room.__last_id += 1
        Room.__instances.append(self)
        
    def __str__(self) -> str:
        return f"  [  {self.id}  ]  \n[  tier {self.tier}  ]"
    
    def __repr__(self) -> str:
            return f"Room #{self.id}, {self.tier} contains {self.boss=} and {self.mobs}. Loot is {self.loot}"
    
    @classmethod
    def all(cls) -> list[Self]:
        return cls.__instances
    
    def boss_defeated(self) -> bool:
        return self.boss is None
    
    def open_chest(self, player: Player) -> None:  
        player.add_items_to_inventory(self.loot)
        
    def open_room(self, player: Player) -> None:
        if player.has(key_format_name(self.id)):
            self.is_open = True
            player.open_room(self.id)
        else:
            raise DontHaveRequiredItem(key_format_name(self.tier))
                
    def get_next_room(self, direction: DirectionLiteral) -> Self | None:
        """
        Used only for going to another room from current. Other uses might break game.
        """

        for room in self.next_rooms:
            if room[1] == direction:
                return room[0]
        
        return None
        
    def set_next_rooms(self, rooms: RoomsList) -> None:
        self.next_rooms = rooms

    @classmethod
    def get_room_from_list(cls, rooms: RoomsList, direction: DirectionLiteral) -> Self | None:
        for room in rooms:
            if room[1] == direction:
                return room[0]
        return None