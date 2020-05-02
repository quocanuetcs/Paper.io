import pygame
import os
from ScreenMove import *
import PersonObject as person

_image_library = {}
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WHIDTH, HEIGHT))

counter = 30
dt = 0

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def get_text(text, x, y, size):
    color = (200, 000, 000)
    font_type = 'ARCADEPI.TTF'
    global screen
    text = str(text)
    font = pygame.font.Font(font_type, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))


def PrintPlayer_zone(color , line, zone, head):
    for val in zone:
        pygame.draw.rect(screen, color.zone,
                         pygame.Rect(val.data_x_min * STRIDE, val.data_y * STRIDE,
                                     (val.data_x_max - val.data_x_min + 1) * STRIDE, STRIDE))

def PrintPlayer_line_head(color , line, zone, head):
    for val in line:
        pygame.draw.rect(screen, color.line,
                pygame.Rect(val.x*STRIDE, val.y*STRIDE, STRIDE, STRIDE))

    pygame.draw.rect(screen, color.head,
                pygame.Rect(head.x * STRIDE, head.y * STRIDE, STRIDE, STRIDE))

def PrintGameOver(GameOverText):
    get_text(GameOverText, 525, 375, 75)
    pygame.display.flip()

def FindScores(zone):
    scores = 0
    for val in zone:
        scores += val.data_x_max - val.data_x_min + 1
    return scores




def Render(botPlayer):
    global screen
    global counter
    global dt
    counter = counter -dt
    screen.fill((255, 255, 255))

    ScreenMove(person, botPlayer)
    if person.live == False:
        PrintGameOver("YOU LOST");
    elif botPlayer.live == False:
        PrintGameOver("YOU WIN");
    elif (counter < 0):
        if (person.scores>= botPlayer.scores):
            PrintGameOver("YOU WIN");
        else: PrintGameOver("YOU LOST");
    else:
        person.scores = FindScores(person.zone)
        botPlayer.scores = FindScores(botPlayer.zone)
        PrintPlayer_zone(person.color, person.line, person.zone, person.head)
        PrintPlayer_zone(botPlayer.color, botPlayer.line, botPlayer.zone, botPlayer.head)
        PrintPlayer_line_head(person.color, person.line, person.zone, person.head)
        PrintPlayer_line_head(botPlayer.color, botPlayer.line, botPlayer.zone, botPlayer.head)
        get_text("YOUR SCORES: " + str(person.scores), WHIDTH - 400, 50, 30)
        get_text("BOT SCORES:  "  + str(botPlayer.scores), WHIDTH - 400, 100, 30)
        get_text("TIME:        "  + str(round(counter)), WHIDTH - 400, 150, 30)
    pygame.display.flip()
    dt = clock.tick(15)/1000