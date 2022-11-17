from body import Body

class Moon(Body):
    def __init__(self, iName, iRad, iM, iDx, iDy, iVx, iVy, iC, visualize = True):
        super().__init__(iName, iRad, iM, iDx, iDy, iVx, iVy, iC, visualize)