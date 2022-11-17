def getDist(t):
    return t[1]

class SolarSystem:
    def __init__(self, width, height, visualize = True, G = 0.1, usingSuns = True, usingPlanets = True):
        self.__sunList = []
        self.__planets = []
        self.__G = G
        self.__usingSuns = usingSuns
        self.__usingPlanets = usingPlanets
        if visualize:
            import turtle
            self.__ssTurtle = turtle.Turtle()
            self.__ssTurtle.hideturtle()
            self.__ssScreen = turtle.Screen()
            self.__ssScreen.setworldcoordinates(-width/2.0, -height/2.0, width/2.0, height/2.0)

    def addPlanet(self, aPlanet):
        self.__planets.append(aPlanet)

    def addSun(self, aSun):
        self.__sunList.append(aSun)

    def showPlanets(self):
        for aPlanet in self.__planets:
            print(aPlanet)

    def numPlanets(self):
        return len(self.__planets)
    
    def totalMass(self):
        totMass = 0
        for aSun in self.__sunList:
            totMass = totMass + aSun.getMass()
        for aPlanet in self.__planets:
            totMass = totMass + aPlanet.getMass()
        return totMass

    def removePlanet(self, exPlanet):
        self.__planets.remove(exPlanet)

    def getNearst(self):
        nearestSoFar = self.__planets[0].getDistance()
        nearest = self.__planets[0]
        for planet in self.__planets:
            distance = planet.getDistance()
            if distance < nearestSoFar:
                nearest = planet
        return nearest

    def getFurthest(self):
        furthestSoFar = self.__planets[0].getDistance()
        furthest = self.__planets[0]
        for planet in self.__planets:
            distance = planet.getDistance()
            if distance > furthestSoFar:
                furthest = planet
        return furthest

    def __str__(self):
        ssString = ""
        for aSun in self.__sunList:
            ssString = aSun.getName()
        planetDict = {}
        for planet in self.__planets:
            planetDict[planet] = planet.getDistance()
        planetDictList = list(planetDict.items())
        planetDictList.sort(key=getDist)
        for planet in planetDictList:
            ssString = ssString + ", " + planet[0].getName() 
        return ssString

    def freeze(self):
        import turtle
        self.__ssScreen.exitonclick()
        turtle.TurtleScreen._RUNNING=True

    def movePlanets(self):
        import math
        dt = 0.001

        for p in self.__planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())
            accX = 0
            accY = 0

            if self.__usingSuns:
                for aSun in self.__sunList:
                    rX = aSun.getXPos() - p.getXPos()
                    rY = aSun.getYPos() - p.getYPos()
                    r = math.sqrt(rX**2 + rY**2)

                    accX = accX + self.__G * aSun.getMass() * rX/r**3
                    accY = accY + self.__G * aSun.getMass() * rY/r**3

            if self.__usingPlanets:
                for p2 in self.__planets:
                    if p2 != p:
                        r2X = p2.getXPos() - p.getXPos()
                        r2Y = p2.getYPos() - p.getYPos()
                        r2 = math.sqrt(r2X**2 + r2Y**2)

                        gravXp2 = (self.__G * p2.getMass() * r2X/r2**3)
                        gravYp2 = (self.__G * p2.getMass() * r2Y/r2**3)
                        accX = accX + gravXp2
                        accY = accY + gravYp2

            p.setXVel(p.getXVel() + dt * accX)
            p.setYVel(p.getYVel() + dt * accY)

        for p in self.__planets:
            for m in p.getMoonList():
                m.moveTo(m.getXPos() + dt * m.getXVel(), m.getYPos() + dt * m.getYVel())
                accX = 0
                accY = 0

                if self.__usingSuns:
                    for aSun in self.__sunList:
                        rX = aSun.getXPos() - p.getXPos()
                        rY = aSun.getYPos() - p.getYPos()
                        r = math.sqrt(rX**2 + rY**2)

                        accX = accX + self.__G * aSun.getMass() * rX/r**3
                        accY = accY + self.__G * aSun.getMass() * rY/r**3

                rX = p.getXPos() - m.getXPos()
                rY = p.getYPos() - m.getYPos()
                r = math.sqrt(rX**2 + rY**2)

                accX = accX + self.__G * 2.5 * p.getMass() * rX/r**3
                accY = accY + self.__G * 2.5 * p.getMass() * rY/r**3

                m.setXVel(m.getXVel() + dt * accX)
                m.setYVel(m.getYVel() + dt * accY)