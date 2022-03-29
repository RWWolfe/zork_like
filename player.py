#player class responsible for tracking movement through rooms, this will determine the win condition
#Classes should have as little responsibility as possible

class Player:
    def __init__(self, cr):
        self._cr = cr
        self.check0 = False
        self.check1 = False
        self.check2 = False
        self.check3 = False
        self.check4 = False
        self.check5 = False

    @property
    def cr(self):
        return self._cr

    @cr.setter
    def cr(self, val):
        self._cr = val
        


    def check_win_condition(self):
        return self.check0 and self.check1 and self.check2 and self.check3 and self.check4 and self.check5

    