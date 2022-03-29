from rooms import Room
from player import Player

r0 = Room(0, "A small, one room church with pews and an altar. Path: ", True, False, False, False, "A book with details on the ritual. Take? ", False)
r1 = Room(1, "There is a small church ahead. Paths: ", True, True, False, False, "Laid on the side of the church is a small shovel. Take?", False)
r2 = Room(2, "bing ging", False, False, True, False, "Fing Ging", False)
r3 = Room(3, "Before you stands the Obelisk. Surrounding it are several statues of people. Paths: ", True, True, True, True, "Crystal statues", False)
r4 = Room(4, "An ampitheater, staged in front of the ocean. Path: ", False, False, False, True, "A bloody knife lays on the stage. Take?", False)
r5 = Room(5, "A garden of various roses. Path: ", False, True, False, False, "A white rose", False)


#cr= current room

player = Player(r3)


while not player.check_win_condition():
    print(player.cr.description)
    if player.cr.north:
        print(" North ")
    if player.cr.south:
        print(" South ")
    if player.cr.east:
        print(" East ")
    if player.cr.west:
        print(" West ")
    dir = input("What do you do? ")
    #disaster incoming
    dir = dir.strip().lower()
    if dir == "n" and player.cr.north:
        if player.cr == r3:
            player.cr = r5
            player.check5 = True
        if player.cr == r1:
            player.cr = r3
            player.check3 = True
        if player.cr == r0:
            player.cr = r1
            player.check1 = True
    if dir == "s" and player.cr.south:
        if player.cr == r1:
            player.cr = r0
            player.check0 = True
        if player.cr == r3:
            player.cr = r1
            player.check1 = True
        if player.cr == r5:
            player.cr = r3
            player.check3 = True
    if dir == "e" and player.cr.east:
        if player.cr == r3:
            player.cr = r4
            player.check4 = True
        if player.cr == r2:
            player.cr = r3
            player.check3 = True
    if dir == "w" and player.cr.west:
        if player.cr == r3:
            player.cr = r2
            player.check2 = True
        if player.cr == r4:
            player.cr = r3
            player.check3 = True
    
    
if player.check_win_condition():
        print("You win!")