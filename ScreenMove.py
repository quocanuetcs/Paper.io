from Define import *

def ScreenMove(person, bot):
    move = XYType(0, 0)
    if person.head.x <= 1:
        move.x = 0 - person.head.x + 1
    elif person.head.x * STRIDE >= (WHIDTH - STRIDE):
        move.x = WHIDTH / STRIDE - person.head.x - 2
    else:
        move.x = 0

    if person.head.y <= 1:
        move.y = 0 - person.head.y + 1
    elif person.head.y * STRIDE >= (HEIGHT - STRIDE):
        move.y = HEIGHT / STRIDE - person.head.y - 2
    else:
        move.y = 0

    person.head.x += move.x
    person.head.y += move.y

    for val in person.line:
        val.x += move.x
        val.y += move.y

    for val in person.zone:
        val.data_x_min += move.x
        val.data_x_max += move.x
        val.data_y += move.y

    bot.head.x += move.x
    bot.head.y += move.y

    for val in bot.line:
        val.x += move.x
        val.y += move.y

    for val in bot.zone:
        val.data_x_min += move.x
        val.data_x_max += move.x
        val.data_y += move.y