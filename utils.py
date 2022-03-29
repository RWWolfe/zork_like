from config import room_layout_config

def connect_rooms(rooms):
    # Assign the config to the room objects
    for room in rooms:
        room.room_layout = room_layout_config[room.room_id]

def get_starting_room(rooms):
    starting_room = rooms[0]
    for room in rooms:
        if room.starting_room:
            starting_room = room
            break
    return starting_room

def _parse_rooms(new_room_id, rooms):
    for room in rooms:
        if room.room_id == new_room_id:
            return room
    else:
        return None

def get_new_current_room(current_room, rooms, direction):
    new_current_room = None
    if direction == "n":
        new_current_room = _parse_rooms(current_room.room_layout["north_room_id"], rooms)
    if direction == "s":
        new_current_room = _parse_rooms(current_room.room_layout["south_room_id"], rooms)
    if direction == "e":
        new_current_room = _parse_rooms(current_room.room_layout["east_room_id"], rooms)
    if direction == "w":
        new_current_room = _parse_rooms(current_room.room_layout["west_room_id"], rooms)
    
    if new_current_room:
        return new_current_room
    else:
        return current_room