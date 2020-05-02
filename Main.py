import pygame
import PersonObject as person
from PersonObject import Key_press
from Define import *
from BotObject import  *
from Graphics import *

#Init
pygame.init()
exitGame = False
botPlayer = BotType(XYType(12, 12), [ZoneType(10, 13, 11), ZoneType(10, 13, 12), ZoneType(10, 13, 13)],
                    PlayerColor((253, 120, 0), (251, 253, 109), (250, 253, 0)))

turn = True

###Control
while not exitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True


    pressed = pygame.key.get_pressed()
    if (turn):
        if Key_press(pressed):
            person.Control(botPlayer)
            turn = False
            # TEST PERSON
            if pressed[pygame.K_0]:
                turn = True
    else:
        botPlayer.Control(person)
        turn = True

    #TEST PERSON
    if pressed[pygame.K_0]:
        turn = True

    #TEST BOT
    if pressed[pygame.K_SPACE]:
        botPlayer.Control(person)

    Render(botPlayer)



