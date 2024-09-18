from src.classes.items import Item, ItemPurpose, ItemState


zombie_flesh = Item('Zombie\'s Flesh', ItemPurpose.MATERIAL, ItemState.LOOT, {
    "stincky": True, "smells_bad": True, "decaying_flesh": True 
})

zombie_bone = Item('Zombie\'s Bone', ItemPurpose.MATERIAL, ItemState.LOOT, {
    "stincky": True, "smells_bad": True, "broken_bone": True 
})

zombie_eye = Item('ZOmbie\'s Eye', ItemPurpose.MATERIAL, ItemState.LOOT, {
    "works_out_of_skull": True, "smells_fresh": True, "viens_throughout": True
})