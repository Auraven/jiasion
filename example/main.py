from jiasion import Serializable
import json

class Stats(Serializable):
    kda_ratio : float
    wins : int

class ItemSlot(Serializable):
    name : str
    stack_size : int    

class Player(Serializable):
    name : str
    stats : Stats
    inventory : list[ItemSlot]

with open('player.json', 'r') as jfile:
    player = Player(json.load(jfile))
    for item_slot in player.inventory:
        item_slot.stack_size += 2
        print(item_slot.name, item_slot.stack_size)

with open('player.json', 'w') as jfile:
    json.dump(player.encode(), jfile, indent=4)