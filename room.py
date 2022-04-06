class Room:
    def __init__(self, room_key, description, description_itemless, starting_room, north_room_key, south_room_key, west_room_key, east_room_key, item):
        self._room_key = room_key
        self._description = description
        self._description_itemless = description_itemless
        self.starting_room = starting_room
        self._north_room_key = north_room_key
        self._south_room_key = south_room_key
        self._west_room_key = west_room_key
        self._east_room_key = east_room_key
        self._item = item

    @property
    def room_key(self):
        return self._room_key

    @property
    def description(self):
        if self.item:
            return self._description
        else:
            return self._description_itemless

    @property
    def north_room_key(self):
        return self._north_room_key

    @property
    def south_room_key(self):
        return self._south_room_key
    
    @property
    def east_room_key(self):
        return self._east_room_key
    
    @property
    def west_room_key(self):
        return self._west_room_key
    
    @property
    def item(self):
        return self._item

    def take_item_from_room(self):
        self._item = None
        return self._item
