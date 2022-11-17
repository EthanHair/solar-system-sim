# This allows the file to be aware of the files in the Classes folder. Also the settings.json 
# file in the .vscode folder does the same if you are using VSCode as your editor
import sys
sys.path.insert(0, ".\\Classes")

from planet import Planet
from sun import Sun
from moon import Moon
from solarsystem import SolarSystem

# A lot of the numbers that define the masses, distances, gravity, ect. are a result of trial and error

def createSSandAnimate():
    ss = SolarSystem(7,7, True, 0.1, True, True)

    sun = Sun("Sun", 200, 1200, 5800, 0, 0)
    ss.addSun(sun)

    merc = Planet("Mercury", 30, 20, 0.5, 0, 0, 17, "blue")
    ss.addPlanet(merc)

    earth = Planet("Earth", 60, 50, 1.2, 0, 0, 11, "green")
    ss.addPlanet(earth)

    mars = Planet("Mars", 55, 30, 1.8, 0, 0, 9.5, "red")
    ss.addPlanet(mars)

    jupiter = Planet("Jupiter", 120, 70, 2.5, 0, 0, 6, "black")
    ss.addPlanet(jupiter)

    saturn = Planet("Saturn", 80, 60, 3.4, 0, 0, 8, "orange")
    ss.addPlanet(saturn)

    luna = Moon("Luna", 10, 10, 1.2, 0.1, -10, 11, "gray")
    earth.addMoon(luna)

    numTimePeriods = 1000
    for aMove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()

createSSandAnimate()

def createN_BodyandAnimate():
    ss = SolarSystem(6,6, True, 0.1, False, True)

    bod1 = Planet("Bob", 100, 60, -1, 0, 5, 1.5, "blue")
    ss.addPlanet(bod1)

    bod2 = Planet("Earl", 100, 90, 0, 0, 2, -3, "green")
    ss.addPlanet(bod2)

    bod3 = Planet("John", 100, 80, 1, 0, -5, 0, "red")
    ss.addPlanet(bod3)

    numTimePeriods = 1000
    for aMove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()

createN_BodyandAnimate()