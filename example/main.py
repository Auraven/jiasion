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

inventory = [
    ItemSlot(name='Fork', stack_size=1),
    ItemSlot(name='Knife', stack_size=4),
    ItemSlot(name='Spoon', stack_size=11)
]

player = Player(name='Mr Mime', stats=Stats(kda_ratio=-1, wins=200), inventory=inventory)
print(player.name)
print(player.stats.wins, player.stats.kda_ratio)
for item_slot in player.inventory:
    print(item_slot.name, item_slot.stack_size)

player.inventory[0].name = 'Spork'
player.inventory[1].stack_size = '123'
player.stats.kda_ratio = 999

with open('player.json', 'w') as jfile:
    json.dump(player.encode(), jfile, indent=4)
    print('Player Saved')
print()

with open('player.json', 'r') as jfile:
    player = Player(json.load(jfile))
    print('Player Loaded')
    print(player.name)
    print(player.stats.wins, player.stats.kda_ratio)
    for item_slot in player.inventory:
        print(item_slot.name, item_slot.stack_size)