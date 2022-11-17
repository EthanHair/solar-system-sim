from body import Body

class Sun(Body):
    def __init__(self, iName, iRad, iM, iTemp, iDx, iDy, visualize = True):
        super().__init__(iName, iRad, iM, iDx, iDy, 0, 0, "yellow", visualize)
        self.__temp = iTemp

    def getTemp(self):
        return self.__temp