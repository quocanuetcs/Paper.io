from Define import  *

def InsZoneToCurX(curr_x, lengthVer, val):
    index = len(curr_x) - 1
    if index>=0 and  curr_x[index] + lengthVer[index] ==  val.data_x_min:
        lengthVer[index] += (val.data_x_max - val.data_x_min +1)
    else:
        curr_x.append(val.data_x_min)
        lengthVer.append(val.data_x_max - val.data_x_min + 1)
    return curr_x, lengthVer

def InsertVerToCurX(curr_x, lengthVer, val_x):
    index = len(curr_x)-1
    if index>=0 and curr_x[index] + lengthVer[index] == val_x:
        lengthVer[index]+=1
    else:
        curr_x.append(val_x)
        lengthVer.append(1)
    return curr_x, lengthVer

def ChooseZone(cur_x, cur_y, lengthVer, currZone, zone, line):
    zoneAdd = []

    if len(cur_x) == 1:
        zoneAdd.append(ZoneType(cur_x[0], cur_x[0] + lengthVer[0] - 1, cur_y))

    index = 1
    while index<len(cur_x):
        if lengthVer[index] == 1 and lengthVer[index-1] == 1:
            zoneAdd.append(ZoneType(cur_x[index-1], cur_x[index], cur_y))
            if index+1  == len(cur_x)-1:
                zoneAdd.append(ZoneType(cur_x[index+1], cur_x[index+1] + lengthVer[index+1] - 1, cur_y ))
            index+=2

        else:
            val_x = round((cur_x[index-1] + lengthVer[index-1] - 1 + cur_x[index])/2)
            val_y = cur_y
            if inNewZone(val_x, val_y, currZone, line):
                zoneAdd.append(ZoneType(cur_x[index-1], cur_x[index] + lengthVer[index] - 1, cur_y))
            else:
                zoneAdd.append(ZoneType(cur_x[index-1], cur_x[index-1] + lengthVer[index-1] - 1, cur_y))
                if index == len(cur_x) - 1:
                    zoneAdd.append(ZoneType(cur_x[index], cur_x[index] + lengthVer[index] - 1, cur_y))
            index+=1

    i = 0
    while i+1<len(zoneAdd):
        while i+1< len(zoneAdd) \
                and ((zoneAdd[i+1].data_x_min + 1 == zoneAdd[i].data_x_max ) or zoneAdd[i+1].data_x_min < zoneAdd[i].data_x_max):
            zoneAdd[i].data_x_max = zoneAdd[i+1].data_x_max
            zoneAdd.pop(i+1)
        i+=1

    MergeZone(cur_y, zoneAdd, zone)

def inNewZone(val_x, val_y, currZone, line):
    valMax_x = line[0].x
    valMin_x = line[0].x

    for val in line:
        if val.x > valMax_x: valMax_x = val.x
        if val.x < valMin_x: valMin_x = val.x

    for val in currZone:
        if val.data_x_max > valMax_x: valMax_x = val.data_x_max
        if val.data_x_min < valMin_x: valMin_x = val.data_x_min


    valMin_y = line[0].y
    if currZone[0].data_y < line[0].y: valMin_y = currZone[0].data_y

    valMax_y = line[len(line)-1].y
    if currZone[len(currZone) - 1].data_y > valMax_y: valMax_y = currZone[len(currZone) - 1].data_y

    tested = []
    queue = []
    m = XYType(val_x, val_y)
    tested.append(m)
    queue.append(m)
    while (len(queue)!= 0):
        queue.pop()
        if (m.x == valMax_x) or (m.x == valMin_x) or (m.y == valMax_y) or (m.y == valMin_y):
            if not(OnBorder(m, currZone, line)): return False

        tg = XYType(m.x+1, m.y)
        if tg.x<= valMax_x and tg.x >= valMin_x and tg.y<=valMax_y and tg.y>=valMin_y:
            if OnBorder(tg, currZone, line):
                tested.append(tg)
            else:
                if not(TestInList(tg, tested)):
                    queue.append(tg)
                    tested.append(tg)

        tg = XYType(m.x - 1, m.y)
        if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
            if OnBorder(tg, currZone, line):
                tested.append(tg)
            else:
                if not(TestInList(tg, tested)):
                    queue.append(tg)
                    tested.append(tg)

        tg = XYType(m.x, m.y + 1)
        if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
            if OnBorder(tg, currZone, line):
                tested.append(tg)
            else:
                if not(TestInList(tg, tested)):
                    queue.append(tg)
                    tested.append(tg)

        tg = XYType(m.x, m.y - 1)
        if tg.x <= valMax_x and tg.x >= valMin_x and tg.y <= valMax_y and tg.y >= valMin_y:
            if OnBorder(tg, currZone, line):
                tested.append(tg)
            else:
                if not(TestInList(tg, tested)):
                    queue.append(tg)
                    tested.append(tg)

        if len(queue)>0: m = queue[len(queue)-1]

    return True

def OnBorder(val, currZone, line):
    bool = False
    i = 0
    while i<len(line) and not(bool):
        if val.x == line[i].x and val.y == line[i].y: bool = True
        i+=1

    if bool or inCurZone(val.x, val.y, currZone): return True
    else: return  False

def inCurZone(val_x, val_y, zone):
    for val in zone:
        if ((val_y == val.data_y) and
                (val.data_x_min<=val_x and val_x<=val.data_x_max)):
            return True

    return False

def TestInList(tg, tested):
    for val in tested:
        if val.x == tg.x and val.y == tg.y: return True
    else: return False

def MergeZone(cur_y, zoneAdd, zone):

    startInsert = -1
    index = len(zone)-1
    while index>=0:
        if zone[index].data_y == cur_y:
            zone.pop(index)
            startInsert = index
        index-=1

    if startInsert != -1:
        index = len(zoneAdd) - 1
        while index>=0:
            zone.insert(startInsert, zoneAdd[index])
            index-=1
    else:
        Input = False
        startInsert = 0
        while startInsert<len(zone) and not(Input) and len(zoneAdd)!=0:
            if zoneAdd[0].data_y < zone[startInsert].data_y:
                Input = True
            else: startInsert+=1

        index = len(zoneAdd) - 1
        while index >= 0:
            zone.insert(startInsert, zoneAdd[index])
            index -= 1