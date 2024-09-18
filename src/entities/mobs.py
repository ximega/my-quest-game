from random import randint

from src.classes.entities import Mob
from src.items.objects.mob_loot import *
from src.classes.items import Item

zombie_1lvl = Mob(
    'Zombie', 
    10, 
    [
        Item.replicate_item(zombie_bone, randint(0, 3)), 
        Item.replicate_item(zombie_eye, randint(0, 2)),
        Item.replicate_item(zombie_flesh, randint(1, 5))
    ]
)