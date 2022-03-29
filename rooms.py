class Room:
    def __init__(self, name, description, north, south , east, west, interactable, takeable):
        self._name = name
        self._description = description
        self._north = north
        self._south = south
        self._east = east
        self._west = west
        self._interactable = interactable
        self._takeable = takeable
      
 #should be an int/ how to make work with location in player?
    @property
    def name(self):
        return self._name


    @property
    def description(self):
        return self._description
    
    @property
    def north(self):
        return self._north

    @property
    def south(self):
        return self._south

    @property
    def east(self):
        return self._east

    @property
    def west(self):
        return self._west

#prompt to get more info/ find items
    @property
    def interactable(self):
        return self._interactable

#keeps track of item on map/ how do i do with inv on player
    @property
    def takeable(self):
        return self._takeable








