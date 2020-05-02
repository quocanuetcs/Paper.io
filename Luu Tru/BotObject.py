import PlayerObject as bot
from Define import *
from PlayerObject import inCurZone
from Divided_MergeZone import TestInList


def MinStepsFromHeadToZone(zone, head):
    valMax_x = head.x
    valMin_x = head.x

    for val in zone:
        if val.data_x_max > valMax_x: valMax_x = val.data_x_max
        if val.data_x_min < valMin_x: valMin_x = val.data_x_min

    valMin_y = zone[0].data_y
    if head.y<valMin_y: valMin_y = head.y
    valMax_y = zone[len(zone) - 1].data_y
    if head.y>valMax_y: valMax_y = head.y



    if inCurZone(head, zone): return 0
    else:
        tested = []
        queue = []

        #Init
        m = XYType(head.x, head.y)
        tested.append(m)
        queue.append(m)
        ###
        while (len(queue) != 0):
            del queue[0]
            if (m.x<= valMax_x) or (m.x >= valMin_x) or (m.y <= valMax_y) or (m.y >= valMin_y):

                tg = XYType(m.x + 1, m.y)
                if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                    if inCurZone(tg, zone):
                        return (abs(head.x - tg.x) + abs(head.y - tg.y) + 1)
                    else:
                        if not(TestInList(tg, tested)):
                            queue.append(tg)
                            tested.append(tg)

                tg = XYType(m.x - 1, m.y)
                if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                    if inCurZone(tg, zone):
                        return (abs(head.x - tg.x) + abs(head.y - tg.y))
                    else:
                        if not (TestInList(tg, tested)):
                            queue.append(tg)
                            tested.append(tg)

                tg = XYType(m.x, m.y + 1)
                if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                    if inCurZone(tg, zone):
                        return (abs(head.x - tg.x) + abs(head.y - tg.y))
                    else:
                        if not (TestInList(tg, tested)):
                            queue.append(tg)
                            tested.append(tg)

                tg = XYType(m.x, m.y - 1)
                if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
                    if inCurZone(tg, zone):
                        return (abs(head.x - tg.x) + abs(head.y - tg.y))
                    else:
                        if not (TestInList(tg, tested)):
                            queue.append(tg)
                            tested.append(tg)

            if len(queue) > 0: m = queue[0]



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

    def Control(self, person):
        ##if person.head.x == 10:
        print(MinStepsFromHeadToZone(person.zone, person.head))

        fuHead = self.head
        if not (bot.inCurZone(self.head, self.zone)):
            if not(bot.inLine(fuHead, self.line)):
                self.head = fuHead
                bot.InsertXY(self.line, self.head)
            self.switch = True
        else:
            if self.switch: bot.SetZone(self.line, self.zone)
            self.line.clear()
            self.switch = False

    def PrintPlayer(self, screen):
        bot.PrintPlayer(screen, self.color, self.line, self.zone, self.head)



