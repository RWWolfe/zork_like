#player class responsible for tracking movement through rooms, this will determine the win condition
#Classes should have as little responsibility as possible

class Player:
    def __init__(self, current_room):
        self._current_room = current_room
        self.visited_rooms = {}

    @property
    def current_room(self):
        return self._current_room

    @current_room.setter
    def current_room(self, val):
        self._current_room = val
    
    def move_player(self, new_room):
        self.current_room = new_room
        self.visited_rooms[new_room.room_id] = new_room
        
    def check_win_condition(self, all_rooms):
        for room in all_rooms:
            if not self.visited_rooms.get(room.room_id):
                return False
        else:
            return True