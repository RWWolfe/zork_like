class Room:
    def __init__(self, room_id, description):
        self._room_id = room_id
        self._description = description
        self._room_layout = {}

    @property
    def starting_room(self):
        return self.room_layout.get("starting_room", False)

    @property
    def room_id(self):
        return self._room_id

    @property
    def description(self):
        return self._description
    
    # Begin room linking section. Is a dictionary formatted as having ids of rooms in directions. Can be None indicating no room.
    @property
    def room_layout(self):
        return self._room_layout
    
    @room_layout.setter
    def room_layout(self, val):
        self._room_layout = val








