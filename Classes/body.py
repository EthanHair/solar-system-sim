class Body:
    def __init__(self, iName, iRad, iM, iDx, iDy, iVx, iVy, iC, visualize = True):
        self.__name = iName
        self.__radius = iRad
        self.__mass = iM
        self.__distance = iDx
        self.__color = iC
        self.__x = self.__distance
        self.__y = iDy

        if visualize:
            import turtle
            self.__pTurtle = turtle.Turtle()

            self.__pTurtle.color(self.__color)
            self.__pTurtle.shape("circle")
            self.__pTurtle.resizemode("user")
            self.__pTurtle.shapesize(self.__radius/100, self.__radius/100, self.__radius/100)

            self.__pTurtle.up()
            self.__pTurtle.goto(self.__x, self.__y)
            self.__pTurtle.down()

        self.__velX = iVx
        self.__velY = iVy
        
    def getName(self):
        return self.__name

    def getRadius(self):
        return self.__radius 
            
    def getMass(self):
        return self.__mass

    def getDistance(self):
        return self.__distance   

    def getVolume(self):
        import math
        v = 4/3 * math.pi * self.__radius**3
        return v 

    def getSurfaceArea(self):
        import math
        sa = 4 * math.pi * self.__radius**2
        return sa

    def getDensity(self):
        d = self.__mass / self.getVolume()
        return d

    def setName(self, newName):
        self.__name = newName

    def __str__(self):
        return self.__name

    def __lt__(self, otherBody):
        return self.__distance < otherBody.__distance

    def __gt__(self, otherBody):
        return self.__distance > otherBody.__distance

    def getCircumference(self):
        import math
        c = 2 * math.pi * self.__radius
        return self.__name

    def getXPos(self):
        return self.__pTurtle.position()[0]

    def getYPos(self):
        return self.__pTurtle.position()[1]

    def moveTo(self, newX, newY):
        self.__pTurtle.goto(newX, newY)

    def getXVel(self):
        return self.__velX

    def getYVel(self):
        return self.__velY

    def setXVel(self, newVx):
        self.__velX = newVx

    def setYVel(self, newVy):
        self.__velY = newVy