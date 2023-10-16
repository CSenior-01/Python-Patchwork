# Caitlin Senior
# up2113762
# Python Coursework 1

from graphics import *


def line(win, point1, point2, colour):
    l = Line(point1, point2)
    l.setOutline(colour)
    l.draw(win)
    return l


def rectangle(win, tlPoint, brPoint, colour):
    r = Rectangle(tlPoint, brPoint)
    r.setFill(colour)
    r.draw(win)
    return r


def brPoint(tlPoint, width, height):
    x = tlPoint.getX() + width
    y = tlPoint.getY() + height
    brPoint = Point(x, y)
    return brPoint


def diagPatch(win, topLeftX, topLeftY, userColour):
    # Draws first set of diagonal lines
    for i in range(0, 100, 20):
        p1 = Point(topLeftX + i, topLeftY)
        p2 = Point(topLeftX, topLeftY + i)
        line(win, p1, p2, userColour)
        p3 = Point(topLeftX + 100, topLeftY + i)
        p4 = Point(topLeftX + i, topLeftY + 100)
        line(win, p3, p4, userColour)

    # Draws second set of diagonal lines
    for i in range(0, 100, 20):
        p5 = Point(topLeftX + i, topLeftY)
        p6 = Point(topLeftX + 100, topLeftY + 100 - i)
        line(win, p5, p6, userColour)
        p7 = Point(topLeftX, topLeftY + i)
        p8 = Point(topLeftX + 100 - i, topLeftY + 100)
        line(win, p7, p8, userColour)


def brickPatch(win, topLeftX, topLeftY, userColour):
    for j in range(5):
        # Draws first line of bricks
        for i in range(0, 100, 25):
            tl = Point(topLeftX + i, topLeftY + j * 20)
            br = brPoint(tl, 25, 10)
            rectangle(win, tl, br, userColour)

        # Draws second line of bricks
        for i in range(0, 100, 40):
            tl = Point(topLeftX + i, topLeftY + 10 + j * 20)
            br = brPoint(tl, 20, 10)
            rectangle(win, tl, br, userColour)


def plainPatch(win, topLeftX, topLeftY, userColour):
    tl = Point(topLeftX, topLeftY)
    br = Point(topLeftX + 100, topLeftY + 100)
    rectangle(win, tl, br, userColour)


def patchwork(screenSize, colours):
    alt = True
    win = GraphWin("Patchwork", screenSize, screenSize)
    for y in range(0, screenSize, 100):
        for x in range(0, screenSize, 100):
            tlPoint = Point(x, y)
            topLeftX = tlPoint.getX()
            topLeftY = tlPoint.getY()
            if x == screenSize - y - 100:
                userColour = colours[1]
            elif x < screenSize - y - 100:
                userColour = colours[0]
            else:
                userColour = colours[2]

            if topLeftY == screenSize - 100 and topLeftX == 0:
                diagPatch(win, topLeftX, topLeftY, userColour)
            elif screenSize / 2 - 50 > x >= 100 and screenSize - 100 > y >= screenSize / 2 + 50:
                brickPatch(win, topLeftX, topLeftY, userColour)
            elif x < screenSize / 2 and y >= screenSize / 2 - 100:
                diagPatch(win, topLeftX, topLeftY, userColour)
            elif x == screenSize - y - 100:
                plainPatch(win, topLeftX, topLeftY, userColour)
            elif x < screenSize - y - 100:
                if x < 0 and y < screenSize - 100:
                    diagPatch(win, topLeftX, topLeftY, userColour)
                else:
                    plainPatch(win, topLeftX, topLeftY, userColour)
            elif x > screenSize - y - 100:
                plainPatch(win, topLeftX, topLeftY, userColour)
            alt = not alt
    win.getMouse()


def menu():
    while True:
        screen = int(input("What size will the patchwork be? "))
        colour = ["red", "green", "purple", "blue", "cyan", "orange"]
        colours = []
        if screen == 5 or screen == 7:
            screenSize = screen * 100
            firstColour = input(str("What will the first colour be? "))
            if firstColour in colour:
                colours.append(firstColour)
                secondColour = input(str("What will the second colour be? "))
                if secondColour in colour:
                    colours.append(secondColour)
                    thirdColour = input(str("What will the third colour be? "))
                    if thirdColour in colour:
                        colours.append(thirdColour)
                        patchwork(screenSize, colours)
                        break
                    else:
                        print(
                            "Your third input was incorrect, please try again. Valid colours are red, green, purple, blue, cyan or orange.")
                else:
                    print(
                        "Your second input was incorrect, please try again. Valid colours are red, green, purple, blue, cyan or orange.")
            else:
                print(
                    "Your first input was incorrect, please try again. Valid colours are red, green, purple, blue, cyan or orange.")
        else:
            print("Incorrect input, please enter either 5 or 7.")


menu()
