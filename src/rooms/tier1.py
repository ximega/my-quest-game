from src.classes.room import Room
from src.classes.entities import Mob
from src.entities import boss, mobs
from random import randint

room_init = Room(
    None,
    None,
    0
)

room1 = Room(
    boss.Wider,
    Mob.replicate_mob(mobs.zombie_1lvl, randint(5, 10)),
    1
)