from room import Room
from player import Player
from config import room_layout_config







all_rooms = {}
#i want to pull the room key from the dictionary in config for each room
#a dictionary of rooms. kvp 



for room_dict in room_layout_config:
    room_key = room_dict["room_key"]               #obelisk
    room_val = Room(room_dict["room_key"], room_dict["description"], room_dict["description_itemless"], room_dict["starting_room"], room_dict["north_room_key"], room_dict["south_room_key"], room_dict["west_room_key"], room_dict["east_room_key"], room_dict["item"])
    kvp = {room_key: room_val}
    all_rooms.update(kvp)





"""""
all_rooms = {
"church": Room("church", "gingign", "no ging", False, "obelisk", None, None, None, None), 
"obelisk": Room("obelisk", "tall", "small", True, "garden", "church", "mountainside", "theater", "height")
"""








#for room in room_layout_config:
    #room_key = ["room_key"]
    #room_val = 
    #all_rooms.update(Room(room["room_key"], room["description"], room["description_itemless"], room["starting_room"], room["north_room_key"], room["south_room_key"], room["west_room_key"], room["east_room_key"], room["item"]))


player= Player(Player.get_starting_room(all_rooms))

while len(player.items) != len(room_layout_config):
    print(player.current_room.description)
    if player.current_room.north_room_key:
        print(" North")
    if player.current_room.south_room_key:
        print(" South")
    if player.current_room.east_room_key:
        print(" East")
    if player.current_room.west_room_key:
        print(" West")
    if player.current_room.item:
        print(" Take" + " " + player.current_room.item + "?")
    
    user_input = input("What do you do? ")
    user_input = user_input.strip().lower()

    try:
        next_room_key = player.get_player_action(user_input)
   
        next_room = all_rooms[next_room_key]
  
        player.current_room = next_room
    
    except KeyError:
        continue

print("I am Die")