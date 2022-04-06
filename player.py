class Player:
    def __init__(self, current_room):
        self._current_room = current_room
        self.items = []

    
    @property
    def current_room(self):
        return self._current_room

    @current_room.setter
    def current_room(self, new_room):
        self._current_room = new_room
   
    def add_item(self, item):
        self.items.append(item)
        return self.items

    def get_starting_room(rooms):
        starting_room = rooms["obelisk"]
        #for key in rooms:
       #     if room[key]:
       #         starting_room =
       #         break
        return starting_room

    def get_player_action(self, user_input):
        if user_input == "n" or user_input == "north":
            return self.current_room.north_room_key
        if user_input == "s" or user_input == "south":
            return self.current_room.south_room_key
        if user_input == "e" or user_input == "east":
            return self.current_room.east_room_key
        if user_input == "w" or user_input == "west":
            return self.current_room.west_room_key
        if user_input == "t" or user_input == "take":
            self.add_item(self.current_room.item)
            print("You took " + self.current_room.item)
            self.current_room.take_item_from_room()