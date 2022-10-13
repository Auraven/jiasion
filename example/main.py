from jiasion import Serializable
import json

class ItemSlot(Serializable):
    def __init__(self, name=None, stack_size=None, json_object=None):       
        self.name = name 
        self.stack_size = stack_size
        if json_object is not None:
            self.decode(json_object)

class Player(Serializable):
    def __init__(self, name=None, inventory=None, json_object=None):       
        self.name = name
        self.inventory = inventory        
        if json_object is not None:   
            self.inventory = [ItemSlot()]    
            self.decode(json_object)

inventory = [
    ItemSlot('Knife', 1),
    ItemSlot("Fork", 15),
    ItemSlot("Spoon", 3)
]

player = Player('Yaga Baba', inventory)
print(player.name)
for item_slot in player.inventory:
    print(item_slot.name, item_slot.stack_size)
print()

player.name = "Baba Yaga"
player.inventory[0].name = 'Spork'

with open('player.json', 'w') as jfile:
    json.dump(player.encode(), jfile, indent=4)

with open('player.json', 'r') as jfile:
    player = Player(json_object=json.load(jfile))
    print(player.name)
    for item_slot in player.inventory:
        print(item_slot.name, item_slot.stack_size) 

