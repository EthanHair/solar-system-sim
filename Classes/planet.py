from body import Body

class Planet(Body):
    def __init__(self, iName, iRad, iM, iDist, iMoons, iVx, iVy, iC, visualize = True):
        super().__init__(iName, iRad, iM, iDist, 0, iVx, iVy, iC, visualize)
        self.__numMoons = iMoons
        self.__moonList = []
        
    def getMoons(self):
        return self.__numMoons

    def getMoonList(self):
        return self.__moonList
    
    def setMoons(self, newNumMoons):
        self.__numMoons = newNumMoons

    def addMoon(self, newMoon):
        self.__moonList.append(newMoon)
        self.__numMoons = self.__numMoons + 1