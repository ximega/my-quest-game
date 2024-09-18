# Commands

## Items
- `use`: using item for their purpose
- `atack`: for combat items
- `recent`
    | `drops` - all recent drops
- `inv`: player's inventory
- `item` 
    | `select [id]/active [order]`: select item for future manipulations
    | `move [active bar id]`: moving item from internal inventory to active one
    | `drop`: throw away item, can be picked if dropped recently

## Rooms
- `room`
    | `open [direction]`: Opening room if player has key
    | `light`: Light room if player has torch
    | `openchest`: for chests in rooms after defeating mobs
- `go [direction]`: going particular direction

## Quests
- `quests`
    | `open`: opening quests
    | `complete [id]`: completeing quest
    | `active`: lists all active quests
    | `check [id]`: whether requirements of quest is met
    | `claim`
    --- `new [id]`: claiming new quest
    | `remove [id]`: removing quest you don't want or can't complete

## Upgrades
- `upgrade`
    | `item`: will list available upgrades for an item
    | `self`: upgrades available for player
    | `inv`: upgrades available for inventory
    | `minis`: upgrades available for minis
    | `machine`: upgrades available for machines
    | `select [item/machine/entity/other]` selecting will provide the list of upgrades and list their ids 
    | `[perk_id]`: upgrade the last perk selected 

## Shop
- `shop`
    | `prev`: previous page of shop
    | `next`: next page of shop
    | `select [id]`: select the item you want to manipulate
    | `mult [amount]`: specify number of items to buy, by default the number is 1
    | `buy`: buys selected item

## Minis
- `minis`
    | `list`: list them all
    | `shop`: shows a buy menu for minis
    | `buy [id]`: buy mini by id in shop
    | `cultivate [id1] [id2]`: cultivate two minis, creating new one
    | `train [...ids]` train one/many of your minis
    | `sell [id]` sells one of your minis

## Spells and Potions
- `spell`
    | `list`: list all spells available for you
    | `use [id]`
    | `cast`: requires alchemistry table to cast
- `potion`
    | `list`: list all potions available for you
    | `use [id]`
    | `brew`: requires alchemistry brewery to brew
    
## Crafting
- `machine`
    | `list`: lists all machines
    | `repair [id]`: will repair machine
    | `check [id]`: provides technical information about machine
- `craft`
    | `open`: opens crafting interface
    | `machine`
    --- `switch [id]`: changes current machine to something else
    --- `show`: will show all machines
    --- `hide`: will hide all machines
    --- `main`: will show only the most used by a player
    | `select [id]`: selects item from player's inventory
    | `inv`
    --- `hide`: will hide all items
    --- `show`: will show all items
    | `put`: puts item onto a crafting space
    | `wcc ([id])`: (what can craft): lists all possible crafts, if provided id selects a crafting item
    | `do`: crafts selected, if not selected the first popped craft

## Others
- `save`: saves all data to storage.json
- `exit`: alternative to **Ctrl+C**
- `esc/close`: escapes from particular UI (interface). Both commands work
NOTE: Should add possibility of auto-save when Ctrl+C is done <!>

# UIs

## Main


Health: 100/100
Protection: 5 (weak)
Subprotection: 0 (no buffs)
Projectile protection: 0 (no buffs)
My damage: 1 (weak)

Nutrition: 54%
Gold coins: 10
Active inventory:
<pre>
   \[1] Enchanced Platinum-roded Ruby Sword
-> \[2] Cooked Porkchop
   \[3] Long-distance bow
   \[4] 1st level Map
</pre>

Minis' overall level: 0
Minis count: 0


command$: use




## Rooms (Map)

<pre>
                [  5  ]
              [  tier 3  ]

   [  2  ]         ↑           
[  tier 2  ]    ← YOU →       [  4  ]
                   ↓        [  tier 1  ]

                [  3  ]
              [  tier 9  ]  
</pre>

## Quests

Claimed:
1) Kill 10 mobs in 10 seconds [id:5] - 5 gold coins, tier 1 key
2) Find two same swords in different chests [id:7] - 7 gold coins, tier 2 key

Available:
1) Kill room boss in one minute [id:14] - 10 gold coins, tier 1 key
2) Open two opposite rooms in 10 seconds [id:4] - 2 gold coins, tier 1 key

## Upgrades
Your items that can be upgraded:
\[1] Enchanced Platinum-roded Ruby Sword
\[2] Long-distance bow
\[3] 1st level Map

## Crafting


[machine]: Crafting table
Alternatives:
<pre>
   Oven [id:2]
   Smeltery [id:3]
   Anvil [id:5]
</pre>

Selected items:
[list of selected items]

Can be crafted:
[list of what can be crafted]

Inventory:
[lists all items in inventory]


# Item descriptions (some of them)

## Map
Levels:
`1` - 1/4 of rooms show their tier, with 50% accuracy
`2` - 1/4 of rooms show their tier, with 95% accuracy
`3` - 2/4 of rooms show their tier, with 65% accuracy
`4` - 3/4 of rooms show their tier, with 25% accuracy
`5` - 3/4 of rooms show their tier, with 100% accuracy
`6` - 4/4 of rooms show their tier, with 55% accuracy
`7` - 4/4 of rooms show their tier, with 75% accuracy
`8` - 4/4 of rooms show their tier, with 100% accuracy


## Rooms
### Bosses
Tiers:
`1`
| Boss: 10-15hp, 2-3 protection, 1-2 subprotection, 0-10 projectile protection, 2-3 damage
`2`
| Boss: 15-25hp, 10-15 protection, 1-5 subprotection, 5-15 projectile protection, 10-15 damage
`3`
(70%)
| Boss: 25-30hp, 10-15 protection, 15-20 subprotection, 30-50 projectile protection, 10-15 damage
(30%)
| Boss: 100-150hp, 40-50 protection, 5-10 subprotection, 1-5 projectile protection, 15-17 damage
`4`
(65%)
| Boss: 150-175hp, 70-100 protection, 150-200 subprotection, 100-120 projectile protection, 10-15 damage
(35%)
| Boss: 100-120hp, 30-40 protection, 15-40 subprotection, 0-80 projectile protection, 30-45 damage
###### TODO: Edit bosses properties
`5`
()
| Boss: 10-15hp, 2-3 protection, 1-2 subprotection, 0-10 projectile protection, 2-3 damage
`6`
| Boss: 10-15hp, 2-3 protection, 1-2 subprotection, 0-10 projectile protection, 2-3 damage
`7`
| Boss: 10-15hp, 2-3 protection, 1-2 subprotection, 0-10 projectile protection, 2-3 damage
`8`
| Boss: 10-15hp, 2-3 protection, 1-2 subprotection, 0-10 projectile protection, 2-3 damage
`9`
| Boss: 10-15hp, 2-3 protection, 1-2 subprotection, 0-10 projectile protection, 2-3 damage
`10`
| Boss: 10-15hp, 2-3 protection, 1-2 subprotection, 0-10 projectile protection, 2-3 damage
`11`
| Boss: 10-15hp, 2-3 protection, 1-2 subprotection, 0-10 projectile protection, 2-3 damage
`12`
| Boss: 10-15hp, 2-3 protection, 1-2 subprotection, 0-10 projectile protection, 2-3 damage
`And later to be added...`


Loots:
`1`
`And later to be added`