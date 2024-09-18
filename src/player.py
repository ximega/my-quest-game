from src.items.objects.keys import ENUM_KEYS
from copy import deepcopy
from src.classes.entities import Player
from src.items.objects.combat import basic_sword
from settings.default import DEFAULT_CHARACTER_NAME

player = Player(
    DEFAULT_CHARACTER_NAME or input('Enter your character name: '),
    10,
    active_inventory = [basic_sword, deepcopy(ENUM_KEYS.TIER1)]
)