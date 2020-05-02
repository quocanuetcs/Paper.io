import pygame
from Divided_MergeZone import *

def inCurZone(val, zone):
    for index in zone:
        if ((val.y == index.data_y) and
                (index.data_x_min <= val.x) and
                (val.x<=index.data_x_max)):
            return True

    return False

def inLine(head, line):
    for val in line:
        if val.x == head.x and val.y == head.y:
            return True
    return  False

def InsertXY(line, head):

    if len(line) == 0:
        line.append(XYType(head.x, head.y))
    else:
        putIn = False
        i = 0
        while (i<len(line) and not(putIn)):
            if (head.y> line[i].y):
                i+=1
            elif head.y == line[i].y:
                j = i
                while (j<len(line) and not(putIn) and line[i].y ==line[j].y):
                    if (head.x> line[j].x):
                        j+=1
                    else:
                        putIn = True
                        line.insert(j, XYType(head.x, head.y))
                if not(putIn):
                    putIn = True
                    line.insert(j, XYType(head.x, head.y))
            else:
                putIn = True
                line.insert(i, XYType(head.x, head.y))

        if not (putIn):
            putIn = True
            line.insert(len(line), XYType(head.x, head.y))

def SetZone(line, zone):
    iLine = 0
    iZone = 0
    lengthVer = []
    currZone = zone.copy()

    curr_x = []
    if line[0].y > currZone[0].data_y: curr_y = currZone[0].data_y
    else: curr_y = line[0].y

    while iLine <= len(line) or iZone <= len(currZone):
        if (iLine<len(line) and iZone<len(currZone) and line[iLine].y == curr_y and
                currZone[iZone].data_y == curr_y):
            if line[iLine].x > currZone[iZone].data_x_min:
                curr_x, lengthVer = InsZoneToCurX(curr_x, lengthVer, currZone[iZone])
                iZone += 1
            else:
                curr_x, lengthVer = InsertVerToCurX(curr_x, lengthVer, line[iLine].x)
                iLine += 1
        ####################
        elif iLine<len(line) and line[iLine].y == curr_y:
            curr_x, lengthVer = InsertVerToCurX(curr_x, lengthVer, line[iLine].x)
            iLine += 1
        ####################
        elif  iZone<len(currZone) and (currZone[iZone].data_y == curr_y):
            curr_x, lengthVer = InsZoneToCurX(curr_x, lengthVer, currZone[iZone])
            iZone += 1
        ####################
        else:
            if len(curr_x)>=1: ChooseZone(curr_x,curr_y, lengthVer, currZone, zone, line)
            curr_x.clear()
            lengthVer.clear()
            #update curr_y
            if iLine<len(line) and iZone<len(currZone):
                if line[iLine].y > currZone[iZone].data_y:
                    curr_y = currZone[iZone].data_y
                else:
                    curr_y = line[iLine].y
            elif iZone<len(currZone):
                curr_y = currZone[iZone].data_y
            elif iLine<len(line):
                curr_y = line[iLine].y

            if iLine == len(line): iLine += 1
            if iZone == len(currZone): iZone +=1

def SetOverlappingZone(mainZone, zone):
    resultMain = []
    for val in zone:
        push = False
        for mainVal in mainZone:
            if (mainVal.data_y == val.data_y):
                if (mainVal.data_x_max< val.data_x_min or mainVal.data_x_min> val.data_x_max):
                    push = True
                    resultMain.append(ZoneType(val.data_x_min, val.data_x_max, val.data_y))
                else:
                    push = True
                    if (mainVal.data_x_min > val.data_x_min):
                        resultMain.append(ZoneType(val.data_x_min, mainVal.data_x_min - 1, val.data_y))
                    if (mainVal.data_x_max < val.data_x_max):
                        resultMain.append(ZoneType(mainVal.data_x_max + 1, val.data_x_max, val.data_y))
        if push == False: resultMain.append(ZoneType(val.data_x_min, val.data_x_max, val.data_y))
    return resultMain
