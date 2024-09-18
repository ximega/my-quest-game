from random import randint

from src.classes.entities import Boss
from src.items.objects.boss_loot import *

Wider = Boss(
    'Wider',
    randint(10,15),
    loot_Wider,
    randint(2,3),
    randint(1,2),
    randint(0,10),
    randint(2,3)
)