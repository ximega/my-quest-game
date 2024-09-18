from enum import Enum
from settings.default import MAX_KEY_TIER
from src.classes.items import Item, ItemPurpose, ItemState
from src.utils2 import irange, key_format_name

class ENUM_KEYS(Enum): ...

for i in irange(1, MAX_KEY_TIER):
    setattr(ENUM_KEYS, f'TIER{i}', Item(key_format_name(i), ItemPurpose.GENERAL, ItemState.LOOT))