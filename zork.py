from room import Room
from player import Player
from utils import connect_rooms, get_new_current_room, get_starting_room

all_rooms = [
    Room(0, "A small, one room church with pews and an altar. Path: "),
    Room(1, "There is a small church ahead. Paths: "),
    Room(2, "bing ging"),
    Room(3, "Before you stands the Obelisk. Surrounding it are several statues of people. Paths: "),
    Room(4, "An ampitheater, staged in front of the ocean. Path: "),
    Room(5, "A garden of various roses. Path: ")
]

connect_rooms(all_rooms)

player = Player(get_starting_room(all_rooms))

while not player.check_win_condition(all_rooms):
    print(player.current_room.description)
    if player.current_room.room_layout["north_room_id"]:
        print(" North ")
    if player.current_room.room_layout["south_room_id"]:
        print(" South ")
    if player.current_room.room_layout["east_room_id"]:
        print(" East ")
    if player.current_room.room_layout["west_room_id"]:
        print(" West ")
    direction = input("What do you do? ")
    direction = direction.strip().lower()
    new_current_room = get_new_current_room(player.current_room, all_rooms, direction)
    player.move_player(new_current_room)

print("You win!")


# You currently making a complete check of every possible south move or whatever move and then determing which one to do.