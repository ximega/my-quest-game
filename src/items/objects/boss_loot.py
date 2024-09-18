from src.classes.items import Item, ItemPurpose, ItemState
from src.items.objects.combat import Wider_bow, Wider_sword


loot_Wider: list[Item] = [Item.choose_one_of(Wider_bow, Wider_sword)]

