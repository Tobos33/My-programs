import pygame as pg
import chess_classes as cc

pg.init()

CUBE_SIZE = 90
CUBE_NUM = 8
WIDTH = CUBE_SIZE*CUBE_NUM


BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
Black = (84, 84, 84)
Gray = (224, 224, 224)


screen = pg.display.set_mode((WIDTH, WIDTH))
screen.fill(WHITE)
pg.display.update()


def draw_cube(x, y, color):
    position = (x*CUBE_SIZE, y*CUBE_SIZE, CUBE_SIZE, CUBE_SIZE)
    pg.draw.rect(screen, color, position)
    pg.display.update()

for i in range(0, 8, 2):
    for j in range(0, 7, 2):
        draw_cube(i, j, Gray)
        draw_cube(i, j+1, Black)
        draw_cube(i+1, j, Black)
        draw_cube(i+1, j+1, Gray)


black_pawn = pg.image.load('C:/Users/pawko/OneDrive/Pulpit/python/Main/black_pawn.png')
white_pawn = pg.image.load('C:/Users/pawko/OneDrive/Pulpit/python/Main/white_pawn.png')

scaled_black_pawn = pg.transform.scale(black_pawn, (CUBE_SIZE/2, CUBE_SIZE/1.5))
scaled_white_pawn = pg.transform.scale(white_pawn, (CUBE_SIZE/2, CUBE_SIZE/1.5))

for i in range(0,8):
    screen.blit(scaled_black_pawn, ((1/4 + i)* CUBE_SIZE,(5/4)* CUBE_SIZE))
    screen.blit(scaled_white_pawn, ((1/4 + i)* CUBE_SIZE,(1/4 + 6)* CUBE_SIZE))
    pg.display.update()





lista = ['rook', 'knight', 'bishop']
for i in lista:
    result = '''
black_{0} = pg.image.load('C:/Users/pawko/OneDrive/Pulpit/python/Main/black_{0}.png')
white_{0} = pg.image.load('C:/Users/pawko/OneDrive/Pulpit/python/Main/white_{0}.png')

scaled_black_{0} = pg.transform.scale(black_{0}, (CUBE_SIZE, CUBE_SIZE))
scaled_white_{0} = pg.transform.scale(white_{0}, (CUBE_SIZE, CUBE_SIZE))

screen.blit(scaled_black_{0}, ({1}*CUBE_SIZE, 0))
screen.blit(scaled_white_{0}, ({1}*CUBE_SIZE,(7)* CUBE_SIZE))
screen.blit(scaled_black_{0}, ((7 - {1})* CUBE_SIZE, 0))
screen.blit(scaled_white_{0}, ((7 - {1})* CUBE_SIZE,(7)* CUBE_SIZE))
pg.display.update()'''.format(i, lista.index(i))
    exec(result)



lista = ['king', 'queen']
for i in lista:
    result = '''
black_{0} = pg.image.load('C:/Users/pawko/OneDrive/Pulpit/python/Main/black_{0}.png')
white_{0} = pg.image.load('C:/Users/pawko/OneDrive/Pulpit/python/Main/white_{0}.png')

scaled_black_{0} = pg.transform.scale(black_{0}, (CUBE_SIZE, CUBE_SIZE))
scaled_white_{0} = pg.transform.scale(white_{0}, (CUBE_SIZE, CUBE_SIZE))

screen.blit(scaled_black_{0}, ((4 - {1})*CUBE_SIZE, 0))
screen.blit(scaled_white_{0}, ((4 - {1})*CUBE_SIZE,(7)* CUBE_SIZE))
pg.display.update()'''.format(i, lista.index(i))
    exec(result)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()