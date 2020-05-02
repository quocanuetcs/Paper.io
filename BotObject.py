import PlayerObject as bot
from Define import *
from PlayerObject import inCurZone
from Divided_MergeZone import TestInList
from PlayerObject import inLine
from Graphics import Render
import array as arr
from random import shuffle

def MinStepsFromHeadToZone(zone, head, line):
    valMax_x = head.x
    valMin_x = head.x

    for val in zone:
        if val.data_x_max > valMax_x: valMax_x = val.data_x_max
        if val.data_x_min < valMin_x: valMin_x = val.data_x_min

    valMin_y = zone[0].data_y
    if head.y<valMin_y: valMin_y = head.y
    valMax_y = zone[len(zone) - 1].data_y
    if head.y>valMax_y: valMax_y = head.y

    valMax_x += 10
    valMax_y += 10
    valMin_y -=10
    valMin_x -= 10
    if inCurZone(head, zone): return 0
    else:
        tested = []
        queue = []
        distance = arr.array('l', [0])

        #Init
        m = XYType(head.x, head.y)
        tested.append(m)
        queue.append(m)

        ###
        while (len(queue) != 0):
            if (m.x<= valMax_x) or (m.x >= valMin_x) or (m.y <= valMax_y) or (m.y >= valMin_y):
                tg = XYType(m.x + 1, m.y)
                if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                    if inCurZone(tg, zone):
                        return distance[0] + 1
                    else:
                        if not (TestInList(tg, tested)):
                            if not(inLine(tg, line)):
                                queue.append(tg)
                                tested.append(tg)
                                distance.append(distance[0] + 1)
                            else:
                                tested.append(tg)


                tg = XYType(m.x - 1, m.y)
                if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                    if inCurZone(tg, zone):
                        return distance[0] + 1
                    else:
                        if not (TestInList(tg, tested)):
                            if not (inLine(tg, line)):
                                queue.append(tg)
                                tested.append(tg)
                                distance.append(distance[0] + 1)
                            else:
                                tested.append(tg)

                tg = XYType(m.x, m.y + 1)
                if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                    if inCurZone(tg, zone):
                        return distance[0] + 1
                    else:
                        if not (TestInList(tg, tested)):
                            if not (inLine(tg, line)):
                                queue.append(tg)
                                tested.append(tg)
                                distance.append(distance[0] + 1)
                            else:
                                tested.append(tg)

                tg = XYType(m.x, m.y - 1)
                if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                    if inCurZone(tg, zone):
                        return distance[0] + 1
                    else:
                        if not (TestInList(tg, tested)):
                            if not (inLine(tg, line)):
                                queue.append(tg)
                                tested.append(tg)
                                distance.append(distance[0] + 1)
                            else:
                                tested.append(tg)

            del queue[0]
            del distance[0]
            if len(queue) > 0: m = queue[0]
    return 0

def MinStepFromBotHeadToPersonHead(bHead, pHead):
    return abs(bHead.x - pHead.x) + abs(bHead.y - pHead.y)

def MinStepToGoToLine(line, head, exception):
    valMax_x = head.x
    valMin_x = head.x

    for val in line:
        if val.x > valMax_x: valMax_x = val.x
        if val.x < valMin_x: valMin_x = val.x

    valMin_y = line[0].y
    if head.y < valMin_y: valMin_y = head.y
    valMax_y = line[len(line) - 1].y
    if head.y > valMax_y: valMax_y = head.y

    tested = []
    queue = []
    link = []

    # Init
    m = XYType(head.x, head.y)
    tested.append(m)
    queue.append(m)
    link.append(0)

    ###
    while (len(queue) != 0):
        if (m.x <= valMax_x) or (m.x >= valMin_x) or (m.y <= valMax_y) or (m.y >= valMin_y):
            tg = XYType(m.x + 1, m.y)
            if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                if inLine(tg, line):
                    tutorial = []
                    tutorial.append(tg)
                    logic = True
                    while (logic):
                        if m==0: logic = False
                        for index in range(len(tested)):
                            if (tested[index] == m):
                                tutorial.append(m)
                                m = link[index]
                    return  tutorial
                else:
                    if not (TestInList(tg, tested)):
                        if not (inLine(tg, exception)):
                            queue.append(tg)
                            tested.append(tg)
                            link.append(m)
                        else:
                            tested.append(tg)
                            link.append(m)


            tg = XYType(m.x - 1, m.y)
            if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                if inLine(tg, line):
                    tutorial = []
                    tutorial.append(tg)
                    logic = True
                    while (logic):
                        if m == 0: break
                        for index in range(len(tested)):
                            if (tested[index] == m):
                                tutorial.append(m)
                                m = link[index]
                    return tutorial
                else:
                    if not (TestInList(tg, tested)):
                        if not (inLine(tg, exception)):
                            queue.append(tg)
                            tested.append(tg)
                            link.append(m)
                        else:
                            tested.append(tg)
                            link.append(m)

            tg = XYType(m.x, m.y + 1)
            if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                if inLine(tg, line):
                    tutorial = []
                    tutorial.append(tg)
                    logic = True
                    while (logic):
                        if m == 0: break
                        for index in range(len(tested)):
                            if (tested[index] == m):
                                tutorial.append(m)
                                m = link[index]
                    return tutorial
                else:
                    if not (TestInList(tg, tested)):
                        if not (inLine(tg, exception)):
                            queue.append(tg)
                            tested.append(tg)
                            link.append(m)
                        else:
                            tested.append(tg)
                            link.append(m)

            tg = XYType(m.x, m.y - 1)
            if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                if inLine(tg, line):
                    tutorial = []
                    tutorial.append(tg)
                    logic = True
                    while (logic):
                        if m == 0: break
                        for index in range(len(tested)):
                            if (tested[index] == m):
                                tutorial.append(m)
                                m = link[index]
                    return tutorial
                else:
                    if not (TestInList(tg, tested)):
                        if not (inLine(tg, exception)):
                            queue.append(tg)
                            tested.append(tg)
                            link.append(m)
                        else:
                            tested.append(tg)
                            link.append(m)

        del queue[0]
        if len(queue) > 0: m = queue[0]
    return []

def MinStepToGoToZone(zone, head, exception):
    valMax_x = head.x
    valMin_x = head.x

    for val in zone:
        if val.data_x_max > valMax_x: valMax_x = val.data_x_max
        if val.data_x_min < valMin_x: valMin_x = val.data_x_min

    valMin_y = zone[0].data_y
    if head.y < valMin_y: valMin_y = head.y
    valMax_y = zone[len(zone) - 1].data_y
    if head.y > valMax_y: valMax_y = head.y

    valMax_x += 10
    valMax_y += 10
    valMin_y -= 10
    valMin_x -= 10

    if inCurZone(head, zone):
        return [1]


    # Init
    tested = []
    queue = []
    link = []
    m = XYType(head.x, head.y)
    tested.append(m)
    queue.append(m)
    link.append(0)

    ###
    while (len(queue) != 0):
        if (m.x <= valMax_x) or (m.x >= valMin_x) or (m.y <= valMax_y) or (m.y >= valMin_y):
            tg = XYType(m.x + 1, m.y)
            if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                if inCurZone(tg, zone):
                    tutorial = []
                    tutorial.append(tg)
                    logic = True
                    while (logic):
                        if m == 0: logic = False
                        for index in range(len(tested)):
                            if (tested[index] == m):
                                tutorial.append(m)
                                m = link[index]
                    return tutorial
                else:
                    if not (TestInList(tg, tested)):
                        if not (inLine(tg, exception)):
                            queue.append(tg)
                            tested.append(tg)
                            link.append(m)
                        else:
                            tested.append(tg)
                            link.append(m)

            tg = XYType(m.x - 1, m.y)
            if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                if inCurZone(tg, zone):
                    tutorial = []
                    tutorial.append(tg)
                    logic = True
                    while (logic):
                        if m == 0: break
                        for index in range(len(tested)):
                            if (tested[index] == m):
                                tutorial.append(m)
                                m = link[index]
                    return tutorial
                else:
                    if not (TestInList(tg, tested)):
                        if not (inLine(tg, exception)):
                            queue.append(tg)
                            tested.append(tg)
                            link.append(m)
                        else:
                            tested.append(tg)
                            link.append(m)

            tg = XYType(m.x, m.y + 1)
            if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                if inCurZone(tg, zone):
                    tutorial = []
                    tutorial.append(tg)
                    logic = True
                    while (logic):
                        if m == 0: break
                        for index in range(len(tested)):
                            if (tested[index] == m):
                                tutorial.append(m)
                                m = link[index]
                    return tutorial
                else:
                    if not (TestInList(tg, tested)):
                        if not (inLine(tg, exception)):
                            queue.append(tg)
                            tested.append(tg)
                            link.append(m)
                        else:
                            tested.append(tg)
                            link.append(m)

            tg = XYType(m.x, m.y - 1)
            if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                if inCurZone(tg, zone):
                    tutorial = []
                    tutorial.append(tg)
                    logic = True
                    while (logic):
                        if m == 0: break
                        for index in range(len(tested)):
                            if (tested[index] == m):
                                tutorial.append(m)
                                m = link[index]
                    return tutorial
                else:
                    if not (TestInList(tg, tested)):
                        if not (inLine(tg, exception)):
                            queue.append(tg)
                            tested.append(tg)
                            link.append(m)
                        else:
                            tested.append(tg)
                            link.append(m)

        del queue[0]
        if len(queue) > 0: m = queue[0]

    return []

def Random(line, head, zone, ans):
     DIRECTION = []
     if not(inLine(XYType(head.x-1, head.y), line)):
             if (len(MinStepToGoToZone(zone,XYType(head.x-1, head.y) , line))!=0):
                DIRECTION.append("LEFT")
     if not(inLine(XYType(head.x+1, head.y), line)) and (len(MinStepToGoToZone(zone, XYType(head.x+1, head.y), line))!=0):
         DIRECTION.append("RIGHT")
     if not (inLine(XYType(head.x, head.y - 1), line))and (len(MinStepToGoToZone(zone, XYType(head.x, head.y - 1), line))!=0):
         DIRECTION.append("UP")
     if not (inLine(XYType(head.x, head.y + 1), line)) and (len(MinStepToGoToZone(zone, XYType(head.x, head.y + 1)               , line))!=0):
         DIRECTION.append("DOWN")

     if (ans in DIRECTION): DIRECTION.remove(ans)

     shuffle(DIRECTION)
     return DIRECTION[0]

def UpdateAnsDirection(head, fuHead):
    if (fuHead.x == head.x):
        if (fuHead.y > head.y): return "DOWN"
        else: return "UP"
    else:
        if (fuHead.x > head.x): return "RIGHT"
        else: return "LEFT"
def  LogicDrections(direction, ansDirection):
    if (direction == "RIGHT" and ansDirection == "LEFT"): return False
    if (direction == "LEFT" and ansDirection == "RIGHT"): return False
    if (direction == "UP" and ansDirection == "DOWN"): return False
    if (direction == "DOWN" and ansDirection == "UP"): return False
    return True

class BotType():
    def __init__(self, head, zone, color):
        self.line = []
        self.head = head
        self.zone = zone
        self.color = color
        self.live = True
        self.direction = "RIGHT"
        self.ansDirection = "RIGHT"
        self.switch = False
        self.botSteps = 0
        self.scores = 0

    def SetSteps(self, person):
        if bot.inLine(self.head, person.line): person.live = False

        if not (bot.inCurZone(self.head, self.zone)):
            if not(bot.inLine(self.head, self.line)):
                bot.InsertXY(self.line, self.head)
                if self.head == person.head: person.live = False
            self.switch = True

        else:
            if self.switch:
                bot.SetZone(self.line, self.zone)
                person.zone = bot.SetOverlappingZone(self.zone, person.zone)
            self.line.clear()
            self.switch = False

    def Control(self, person):
        person_HeadtoZone = MinStepsFromHeadToZone(person.zone, person.head, person.line)
        botHead_to_personHead = MinStepFromBotHeadToPersonHead(self.head, person.head)
        bot_HeadtoZone = MinStepsFromHeadToZone(self.zone, self.head, self.line)

        #find fuHead
        logicelse = False
        if (botHead_to_personHead < person_HeadtoZone):
            m = MinStepToGoToLine(person.line,self.head, self.line)
            i = len(m) - 2
            fuHead = XYType(m[i].x, m[i].y)
        elif (len(self.line)>0 and
            bot_HeadtoZone > len(MinStepToGoToLine(self.line, person.head, person.line))- 4):
            m = MinStepToGoToZone(self.zone, self.head, self.line)
            i = len(m) - 2
            fuHead = XYType(m[i].x, m[i].y)
        else:
            logicelse = True
            while (True):
                fuHead = XYType(self.head.x, self.head.y)
                if (self.direction == "RIGHT"):fuHead.x += 1
                elif (self.direction == "LEFT"):fuHead.x -= 1
                elif (self.direction == "UP"):fuHead.y -= 1
                else: fuHead.y += 1

                if not (inLine(fuHead, self.line)) and (
                        len(MinStepToGoToZone(self.zone, fuHead, self.line))) != 0 and (
                        LogicDrections(UpdateAnsDirection(self.head, fuHead), self.ansDirection)):
                    self.head = fuHead
                    break
                else:
                    self.direction = Random(self.line, self.head, self.zone, self.ansDirection)

            self.ansDirection = self.direction
            self.SetSteps(person)

        if (logicelse == False):
            while (True):
                if not (inLine(fuHead, self.line)) and(
                        LogicDrections(UpdateAnsDirection(self.head, fuHead), self.ansDirection)):
                    self.ansDirection = UpdateAnsDirection(self.head, fuHead)
                    self.head = fuHead
                    break
                else:
                    fuHead = XYType(self.head.x, self.head.y)
                    self.direction = Random(self.line, self.head, self.zone, self.ansDirection)
                    if (self.direction == "RIGHT"): fuHead.x += 1
                    elif (self.direction == "LEFT"):fuHead.x -= 1
                    elif (self.direction == "UP"): fuHead.y -= 1
                    else: fuHead.y += 1

            self.SetSteps(person)















