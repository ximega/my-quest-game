# /src/

## /classes/

### items.py

Item.\_\_init\_\_.characteristics: dict[str, str | int]

Provide descriptino of an item's characteristics

The maximum possible characteristic of "overall" item (that combines all items, specifications provided for each characteristic)

`.json format`, alllowed to specify characteristics in `/src/items/characteristics/[name].json`
{
    "main": {
        "durability": int
    },
    "enchants": {
        "unbreaking": int<1-10> 
        *can be different, check /settings/default.py*
    }
}