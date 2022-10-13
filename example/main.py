from jiasion import Serializable
import json

class Stats(Serializable):
    def __init__(self, constitution=0, strength=0, dexterity=0, intelligence=0, wisdom=0, charisma=0, json_object=None):       
        self.constitution = constitution 
        self.strength = strength 
        self.dexterity = dexterity 
        self.intelligence = intelligence 
        self.wisdom = wisdom 
        self.charisma = charisma 
        if json_object is not None:
            self.decode(json_object)

class ItemSlot(Serializable):
    def __init__(self, name='', stack_size=0, json_object=None):       
        self.name = name 
        self.stack_size = stack_size
        if json_object is not None:
            self.decode(json_object)

class Player(Serializable):
    def __init__(self, name='', stats=Stats(), inventory=None, json_object=None):       
        self.name = name
        self.stats = stats
        self.inventory = inventory        
        if json_object is not None:   
            self.inventory = [ItemSlot()]    
            self.decode(json_object)

inventory = [
    ItemSlot('Knife', 1),
    ItemSlot("Fork", 15),
    ItemSlot("Spoon", 3)
]

player = Player('Yaga Baba', Stats(12,14,18,8,10,9), inventory)
print(player.name)
for item_slot in player.inventory:
    print(item_slot.name, item_slot.stack_size)
print(player.stats.dexterity)
print()

player.name = "Baba Yaga"
player.inventory[0].name = 'Spork'
player.stats.dexterity = 20

with open('player.json', 'w') as jfile:
    json.dump(player.encode(), jfile, indent=4)

with open('player.json', 'r') as jfile:
    player = Player(json_object=json.load(jfile))
    print(player.name)
    for item_slot in player.inventory:
        print(item_slot.name, item_slot.stack_size) 
    print(player.stats.dexterity)