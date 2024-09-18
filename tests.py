from src.classes.crafting import Machine, ItemRecipe, RepairStatus
from src.classes.items import Item, ItemPurpose, ItemState


iron = Item("Iron", ItemPurpose.MATERIAL, ItemState.PASSIVE, {"oxidized"}, 100)

copper = Item("Copper", ItemPurpose.MATERIAL, ItemState.PASSIVE, {"oxidized"}, 100)

tin = Item("Tin", ItemPurpose.MATERIAL, ItemState.PASSIVE, None, 100)

Smeltery = Machine("Smeltery", "6")

bronze_recipe = ItemRecipe("Copper", "Copper", "Copper", "Tin", output="Bronze", time=5, tier=1, machine=Smeltery)

Smeltery.update_recipies(bronze_recipe)

print(Smeltery.show_available_recipies(tin))