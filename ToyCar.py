# File: Project2.py

# Course Name: CS303E
#
# Date: 4/2/23
# Description of Program: this program will simulate a toy car driving around a grid using functions within the class Toycar
# also will use functions outside of the class

import random

EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class ToyCar:
    # initializing... with private attributes
    def __init__(self, x=0, y=0, d=EAST):
        self.__x = x
        self.__y = y
        # makes sure that direction given is legal
        if d == EAST or d == NORTH or d == WEST or d == SOUTH:
            self.__d = d

        else:
            print("ERROR: Illegal direction entered.")

    # basically a print statement
    def __str__(self):
        if self.__d == EAST:
            printdir = "East"

        elif self.__d == NORTH:
            printdir = "North"

        elif self.__d == WEST:
            printdir = "West"

        else:
            printdir = "South"

        return "Your car is at location (" + str(self.__x) + ", " + str(self.__y) + "), heading " + printdir

    # allows user to set direction
    def setDir(self, n):
        if n == EAST or n == NORTH or n == WEST or n == SOUTH:
            self.__d = n

        if self.__d == EAST:
            printdir = "East"

        elif self.__d == NORTH:
            printdir = "North"

        elif self.__d == WEST:
            printdir = "West"

        else:
            printdir = "South"

        print("DEBUG: setting direction", printdir)

    # allows user to get direction
    def getDir(self):
        if self.__d == 0:
            return 0

        if self.__d == 90:
            return 90

        if self.__d == 180:
            return 180

        if self.__d == 270:
            return 270

    # allows access of x attribute even tho it's private, I use these for the functions outside of the class
    def getX(self):
        return self.__x

    # meow meow same thing
    def getY(self):
        return self.__y

    # turns car left, makes sure direction doesn't go like over 270
    def turnLeft(self):
        if self.__d == 270:
            self.__d = 0

        else:
            self.__d += 90

        if self.__d == EAST:
            printdir = "East"

        elif self.__d == NORTH:
            printdir = "North"

        elif self.__d == WEST:
            printdir = "West"

        else:
            printdir = "South"

        print("DEBUG: turning", printdir)

    # same thing
    def turnRight(self):
        if self.__d == 0:
            self.__d = 270

        else:
            self.__d -= 90

        if self.__d == EAST:
            printdir = "East"

        elif self.__d == NORTH:
            printdir = "North"

        elif self.__d == WEST:
            printdir = "West"

        else:
            printdir = "South"
        print("DEBUG: turning", printdir)

    # moves car forward by whatever user wants as long as its positive
    def forward(self, n):
        if n > 0:
            if self.__d == 0:
                self.__x += n

            if self.__d == 90:
                self.__y += n

            if self.__d == 180:
                self.__x -= n

            if self.__d == 270:
                self.__y -= n

            print("DEBUG: moving forward", n)

        else:
            print("ERROR: Illegal direction entered.")


# outerclass functions kachow
# random drive, makes sure number of times is legal woohoo
def randomDrive(car, n):
    if not n > 0:
        print("ERROR: Illegal value entered.")
        return

    # basically just does the number of times it wants
    for i in range(n):
        turndir = random.choice(["left", "right", "forward"])
        if turndir == "left":
            car.turnLeft()

        elif turndir == "right":
            car.turnRight()

        newdist = random.randint(1, 100)
        car.forward(newdist)

# go to a given location
def goto(car, x, y):
    if car.getX() == x and car.getY() == y:
        return

    if car.getX() != x:
        if x > car.getX():
            car.setDir(EAST)
            car.forward(x - car.getX())

        else:
            car.setDir(WEST)
            car.forward(car.getX() - x)

    if car.getY() != y:
        if y > car.getY():
            car.setDir(NORTH)
            car.forward(y - car.getY())

        else:
            car.setDir(SOUTH)
            car.forward(car.getY() - y)

# random gas coordinantes
def gasStation():
    gasx = random.randint(-100, 100)
    gasy = random.randint(-100, 100)
    print("Located gas station at (", gasx, ", ", gasy, ")")
    return gasx, gasy

# get some gas babyyy whooo lets gooo
def gasUp(car):
    newx, newy = gasStation()
    goto(car, newx, newy)
