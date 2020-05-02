import PlayerObject as person
import  pygame
from Define import *

direction = "RIGHT"
ansDirection = "RIGHT"
switch = False

line = []
head = XYType(7,7)
zone = [ZoneType(5, 8, 5),ZoneType(5, 8, 6),ZoneType(5, 8, 7)]
live = True
color = PlayerColor((176, 12, 12), (255, 150, 150), (255, 0,0))
scores = 0

def Key_press(pressed):
    global ansDirection
    global direction
    global personSteps

    if pressed[pygame.K_UP]:
        direction = "UP"
        if ansDirection != "DOWN":
            head.y -= 1
            ansDirection = "UP"
            return True

    elif pressed[pygame.K_LEFT]:
        direction = "LEFT"
        if ansDirection != "RIGHT":
            head.x -= 1
            ansDirection = "LEFT"
            return True

    elif pressed[pygame.K_RIGHT]:
        direction = "RIGHT"
        if ansDirection != "LEFT":
            head.x += 1
            ansDirection = "RIGHT"
            return True
    elif pressed[pygame.K_DOWN]:
        direction = "DOWN"
        if ansDirection != "UP":
            head.y += 1
            ansDirection = "DOWN"
            return True

def Control(bot):
    global head_
    global line
    global zone
    global switch
    global live

    if person.inLine(head, bot.line):  bot.live = False

    if not (person.inCurZone(head, zone)):
        if not(person.inLine(head, line)):
            person.InsertXY(line, head)
        else: live = False
        switch = True
    else:
        if switch:
            person.SetZone(line, zone)
            bot.zone = person.SetOverlappingZone(zone, bot.zone)
        line.clear()
        switch = False



