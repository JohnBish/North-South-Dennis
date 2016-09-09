import graphics
from time import sleep
import os
import random

Point = graphics.Point
Rectangle = graphics.Rectangle
Line = graphics.Line
Text = graphics.Text
Image = graphics.Image
o = Point(0, 0)
x = Point(801, 401)
dir = os.path.dirname(os.path.realpath(__file__))
character = Image(o, dir + "\defaultSkin.png")
textPoint = Point(400, 375)
resp = ""
location = 0
dialogue = Text(textPoint, "")
largeRoom = True
firstMain = ""
firstNorth1 = ""
northDir = 2
respawn = False
movementSpeed = 0.005

rustySpoon = {"Name": "Rusty Spoon", "Power": 2, "Def": 4, "Reg": 10, "Image": Image(Point(400, 200), "rustySpoon.png")}
giraffeSkin = {"Name": "Giraffe Skin", "Power": 0,  "Def": 3, "Reg": 0}
greenSlime = {"Name": "Green Slime", "Power": 0, "Def": 2, "Reg": 10}
items = []
items.append(rustySpoon)
items.append(giraffeSkin)
items.append(greenSlime)

ceilingGiraffe = {"Name": "Carnivorous Ceiling Giraffe", "Power": 5, "Def": 5, "Image": Image(Point(-100, 100), "ceilingGiraffe.png")}
slugoon = {"Name": "Slugoon", "Power": 3, "Def": 5, "Image": Image(Point(-100, 100), "slugoon.png")}

ownedItems = []

roomText = "currentRoom.txt"
inventoryText = "inventory.txt"
firstText = "firstEnter.txt"


'''class Character(object):
    def __init__(self):
'''


def main():
    global location
    global firstMain
    global firstNorth1
    with open(roomText) as rt:
        fileRead = rt.read()
        if fileRead == "":
            location = 0
        else:
            location = int(fileRead)
    with open(inventoryText) as it:
        for line in it:
            if line != "":
                ownedItems.append(line)
    with open(firstText) as ft:
        firstMain = ft.readline()
        firstNorth1 = ft.readline()
    moveRoom()


def roomEnter():
    backgr = Rectangle(o, x)
    backgr.setFill("black")
    backgr.draw(win1)
    textPut(733, 15, "Version 1.1")


def textCentre(str):
    return str.center(100)


#Prints text at the bottom of the screen
def textPrint(str):
    textCentre(str)
    dialogue = Text(textPoint, str)
    dialogue.setFace("courier")
    dialogue.setTextColor("white")
    dialogue.draw(win1)
    win1.getMouse()
    dialogue.undraw()
    sleep(0.2)


#Prints text at any location on the screen
def textPut(a, b, str):
    dialogue = Text(Point(a, b), str)
    dialogue.setFace("courier")
    dialogue.setTextColor("white")
    dialogue.draw(win1)


def roomDraw():
    if largeRoom:
        room = Rectangle(Point(200, 100), Point(600, 300))
    else:
        room = Rectangle(Point(300, 125), Point(500, 275))
    room.setOutline("white")
    room.draw(win1)


def characterDraw(a, b):
    global character
    character = Image(Point(a, b), "defaultSkin.png")
    character.draw(win1)


def characterEnter(a, b, int):
    global character
    global northDir
    y = 200
    if  int != 2:
        if int == 1:
            x = 800
            characterDraw(x, y)
        elif int == 0:
            x = 0
            characterDraw(x, y)
        while x < a:
            character.move(1, 0)
            x += 1
            sleep(movementSpeed)
        while x > a:
            character.move(-1, 0)
            x -= 1
            sleep(movementSpeed)
        while y < b:
            character.move(0, 1)
            y += 1
            sleep(movementSpeed)
        while y > b:
            character.move(0, -1)
            y -= 1
            sleep(movementSpeed)
    else:
        characterDraw(a, b)
    northDir = 2
    dirDraw()


#True parameter = left exits
def exits(boolean):
    if largeRoom:
        xind = 200
    else:
        xind = 300
    if boolean:
        door = Line(Point(xind, 150), Point(xind, 250))
        wall1 = Line(Point(xind, 150), Point(0, 150))
        wall2 = Line(Point(xind, 250), Point(0, 250))
    else:
        door = Line(Point(800 - xind, 150), Point(800 - xind, 250))
        wall1 = Line(Point(800 - xind, 150), Point(802, 150))
        wall2 = Line(Point(800 - xind, 250), Point(802, 250))
    door.setOutline("black")
    wall1.setOutline("white")
    wall2.setOutline("white")
    door.draw(win1)
    wall1.draw(win1)
    wall2.draw(win1)


def exits2(boolean):
    if largeRoom:
        yind = 100
    else:
        yind = 125
    if boolean:
        door = Line(Point(350, yind), Point(450, yind))
        wall1 = Line(Point(350, yind), Point(350, 0))
        wall2 = Line(Point(450, yind), Point(450, 0))
    else:
        door = Line(Point(350, 400 - yind), Point(450, 400))
        wall1 = Line(Point(350, 400 - yind), Point(350, 400))
        wall2 = Line(Point(450, 400 - yind), Point(450, 400))
    door.setOutline("black")
    wall1.setOutline("white")
    wall2.setOutline("white")
    door.draw(win1)
    wall1.draw(win1)
    wall2.draw(win1)


def hallway():
    hall = Rectangle(Point(-1, 150), Point(802, 250))
    hall.setOutline("white")
    hall.draw(win1)
    

def input():
    inp = ""
    inputBox = graphics.Entry(textPoint, 1)
    while inp != "N" and inp != "S" and inp != "D" and inp != "S" and inp != "I" and inp != "B" and inp != "?":
        inputBox.draw(win1)
        win1.getMouse()
        inp = inputBox.getText()
        inputBox.undraw()
    return inp


def death():
    global location
    global respawn
    roomEnter()
    textPrint("You have died!")
    location = 0
    respawn = True
    moveRoom()


def inventory():
    global northDir
    global ownedItems
    northDir = 2
    roomEnter()
    inp = ""
    inputBox = graphics.Entry(textPoint, 1)
    textPut(400, 100, textCentre("Inventory"))
    textPut(100, 133, "Item")
    textPut(300, 133, "Power")
    textPut(500, 133, "Defense")
    textPut(700, 133, "Regen")
    #textPut(100, 200, item["Name"])
    inputBox.draw(win1)
    win1.getMouse()
    inp = inputBox.getText()
    inputBox.undraw()


def search():
    roomEnter()

# To be fixed later
playerHp = 10
mobHp = ceilingGiraffe["Def"]

def encounter(a, b, mob):
    global ceilingGiraffe
    global firstNorth1

    ceilingGiraffe["Image"] = (Image(Point(-100, 100), "ceilingGiraffe.png"))

    def encounterInput():
        inp = ""
        inputBox = graphics.Entry(textPoint, 1)
        while inp != "A" and inp != "F":
            inputBox.draw(win1)
            win1.getMouse()
            inp = inputBox.getText()
            inputBox.undraw()
        return inp


    def encounterEnter():
        x = 700
        y = 350
        c = a
        d = b
        while d < y:
            d += 1
            character.move(0, 1)
            sleep(0.005)
        while c < x:
            c += 1
            character.move(1, 0)
            sleep(0.005)
        sleep(2)
        mob["Image"].draw(win1)
        for i in range(1, 300):
            mob["Image"].move(1, 0)
            sleep(0.005)


    def attack():
        global playerHp
        global mobHp
        while playerHp > 1 and mobHp > 1:
            inp = ""
            textPrint("Choose a number between 0 and 9")
            inputBox = graphics.Entry(textPoint, 1)
            while inp != "0" and inp != "1" and inp != "2" and inp != "3" and inp != "4" and inp != "5" and inp != "6" and inp != "7" and inp != "8" and inp != "9":
                inputBox.draw(win1)
                win1.getMouse()
                inp = inputBox.getText()
                inputBox.undraw()
            number = random.randint(-10, 20)
            if number > int(inp):
                textPrint("Alas! You were dealt a blow.")
                playerHp -= mob["Power"]
            else:
                textPrint("A direct hit!")
                mobHp -= 3
            fillText = Rectangle(Point(455, 165), Point(465, 175))
            fillText.setFill("black")
            fillText.draw(win1)
            textPut(460, 170, mobHp)
            fillText = Rectangle(Point(600, 365), Point(620, 375))
            fillText.setFill("black")
            fillText.draw(win1)
            textPut(610, 370, playerHp)


    if mob["Name"] == "Carnivorous Ceiling Giraffe":
        textPrint("What's that?")
        textPrint("Drip.")
        textPrint("Drip.")
        textPrint("It's getting closer.")
        roomEnter()
        characterDraw(a, b)
        sleep(1)
        textPrint("A drop just landed on your head.")
        sleep(2)
        encounterEnter()
        textPut(450, 150, mob["Name"])
        textPut(460, 170, mobHp)
        textPut(600, 350, "Player")
        textPut(610, 370, playerHp)
        textPrint("Type A (Attack), or F (Flee)")
        textPrint("NOTE: Flee is currently unavailable.")
        resp = encounterInput()
        if resp == "A":
            attack()
        if playerHp < 1:
            for i in range(1, 100):
                character.move(0, 1)
                sleep(movementSpeed)
            mob["Image"].undraw()
            character.undraw()
            death()
        else:
            for i in range(1, 300):
                mob["Image"].move(0, -1)
                sleep(movementSpeed)
            mob["Image"].undraw()
            textPrint("You were victorious!")
            character.undraw()
            firstNorth1 = "0"
            with open(firstText, "w") as ft:
                ft.write("")
                ft.write(firstNorth1)
            moveRoom()


def moveRoom():
    with open(roomText, "w") as rt:
        rt.write(str(location))
    if location == 1:
        north1()
    elif location == 0:
        mainRoom()
    elif location == -1:
        south1()
    elif location == 2:
        north2()
    elif location == -2:
        south2()
    elif location == 3:
        roomEnter()
        slugoon["Image"].move(500, 100)
        slugoon["Image"].draw(win1)
        textPrint("You have fallen into the abyss!")
        slugoon["Image"].move(-500, -100)
        slugoon["Image"].undraw()
        death()
    elif location == -3:
        roomEnter()
        slugoon["Image"].move(500, 100)
        slugoon["Image"].draw(win1)
        textPrint("You have fallen into the abyss!")
        slugoon["Image"].move(-500, -100)
        slugoon["Image"].undraw()
        death()


def move(str):
    global location
    global northDir
    if str == "N":
        textPrint("You have chosen North!")
        for i in range (399):
            character.move(-1, 0)
            sleep(movementSpeed)
        location += 1
        northDir = 1
    elif str == "S":
        textPrint("You have chosen South!")
        for i in range(399):
            character.move(1, 0)
            sleep(movementSpeed)
        location -= 1
        northDir = 0
    elif str == "I":
        inventory()
    elif str == "?":
        search()
    moveRoom()


def dirDraw():
    dir1 = Text(Point(167, 200), "N")
    dir2 = Text(Point(633, 200), "S")
    dir1.setSize(20)
    dir2.setSize(20)
    dir1.setTextColor("white")
    dir2.setTextColor("white")
    dir1.setFace("courier")
    dir2.setFace("courier")
    dir1.undraw()
    dir2.undraw()
    dir1.draw(win1)
    dir2.draw(win1)


def dirDraw2(boolean):
    if boolean:
        dir = Text(Point(400, 100), "E")
    else:
        dir = Text(Point(400, 300), "W")
    dir.setSize(20)
    dir.setTextColor("white")
    dir.setFace("courier")
    dir.undraw()
    dir.draw(win1)


def mainRoom():
    global largeRoom
    global respawn
    global firstText
    global playerHp
    roomEnter()
    largeRoom = True
    roomDraw()
    exits(True)
    exits(False)
    dennisdoor = Line(Point(300, 100), Point(500, 100))
    denniswall1 = Line(Point(300, 100), Point(300, 0))
    denniswall2 = Line(Point(500, 100), Point(500, 0))
    dennisdoor.setOutline("black")
    denniswall1.setOutline("white")
    denniswall2.setOutline("white")
    dennisdoor.draw(win1)
    denniswall1.draw(win1)
    denniswall2.draw(win1)
    global firstMain
    if firstMain:
        dirDraw()
        characterDraw(400, 200)
        textPrint("Welcome to North South Dennis, a game by the NSD Team (click to proceed)")
        textPrint("You have become lost in the basement of your new house.")
        textPrint("Try to find the way out.")
        textPrint("To begin, input N (North), S (South), D (Dennis), ? (Search), or I (Inventory).")
        textPrint("NOTE: Search and Inventory are currently unavailable.")
        textPrint ("Then, click to enter your input.")
        with open(firstText, "w") as ft:
            ft.write("")
            ft.write("")
        firstMain = False
    elif respawn:
        dirDraw()
        number = random.randint(1, 5)
        if number == 1:
            textPrint("Sucks to suck.")
        elif number == 2:
            textPrint("That didn't take very long.")
        elif number == 3:
            textPrint("You should be ashamed of yourself.")
        elif number == 4:
            textPrint("How will you get anywhere in life if you can't even get out of a basement?")
        elif number == 5:
            textPrint("Brethren, doest thou even hoist?")
        characterDraw(400, 200)
        playerHp = 10
        respawn = False
    else:
        characterEnter(400, 200, northDir)
    resp = input()
    move(resp)


def north1():
    roomEnter()
    hallway()
    characterEnter(400, 200, northDir)
    if firstNorth1 == "1":
        encounter(400, 200, ceilingGiraffe)
    resp = input()
    move(resp)


def north2():
    global largeRoom
    roomEnter()
    largeRoom = False
    roomDraw()
    exits(False)
    exits2(True)
    characterEnter(400, 200, northDir)
    dirDraw2(True)
    resp = input()
    move(resp)


def south1():
    global largeRoom
    roomEnter()
    largeRoom = True
    roomDraw()
    exits(True)
    exits(False)
    characterEnter(400, 200, northDir)
    resp = input()
    move(resp)


def south2():
    global largeRoom
    roomEnter()
    largeRoom = False
    roomDraw()
    exits(True)
    characterEnter(400, 200, northDir)
    resp = input()
    move(resp)


win1 = graphics.GraphWin("North South Dennis", 800, 400)
main()
sleep(3)
win1.close()