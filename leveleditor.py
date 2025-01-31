import pygame as pg
from levelexporter import*


def drawgrid(n, fillmatrix):
    d = h/(n)
    for i in range(n):
        pg.draw.line(screen, (0,0,0), (d*(i), 0), (d*(i), h))
    for i in range(n):
        pg.draw.line(screen, (0,0,0), (0, d*(i)), (w, d*(i)))
    for i in range(n):
        for j in range(n):
            if fillmatrix[i][j] == 1:
                pg.draw.rect(screen, (0, 0, 0), (i*d, j*d, d+1, d+1))
            elif fillmatrix[i][j] == 2:
                pg.draw.rect(screen, (255, 0, 0), (i*d, j*d, d+1, d+1))
            elif fillmatrix[i][j] == 3:
                pg.draw.rect(screen, (0, 255, 0), (i*d, j*d, d+1, d+1))
            elif fillmatrix[i][j] == 4:
                pg.draw.rect(screen, (255, 255, 0), (i*d, j*d, d+1, d+1))

def getgridpos(mousepos, n):
    return (max(0,min(int((n)*(mousepos[0]/h)),n-1)), max(0,min(int((n)*(mousepos[1]/h)),n-1)))
pg.init()

w = pg.display.Info().current_w
h = pg.display.Info().current_h

screen = pg.display.set_mode((w, h), pg.FULLSCREEN)

fps = 144
clock = pg.time.Clock()
dt = 1 / fps

font = pg.font.SysFont(None, 50)

n = 32
fillmatrix = [[0 for i in range(n)] for j in range(n)]

drawing = False
erasing = False

save = False

running = True
while running:
    screen.fill((255, 255, 255))

    mousepos = pg.mouse.get_pos()
    keystates = pg.key.get_pressed()
    currentfps = clock.get_fps()

    mouseingrid = getgridpos(mousepos, n)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_c:
                for i in range(n):
                    for j in range(n):
                        if fillmatrix[i][j] == 3:
                            fillmatrix[i][j] = 0
                fillmatrix[mouseingrid[0]][mouseingrid[1]] = 3
            if event.key == pg.K_l:
                fillmatrix[mouseingrid[0]][mouseingrid[1]] = 4
            if keystates[pg.K_LCTRL] and event.key == pg.K_e:
                running = False
                save = True
            if keystates[pg.K_LCTRL] and event.key == pg.K_r:
                fillmatrix = [[0 for i in range(n)] for j in range(n)]

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
            elif event.button == 2:
                fillmatrix[mouseingrid[0]][mouseingrid[1]] = 2
            elif event.button == 3:
                erasing = True

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
            elif event.button == 3:
                erasing = False

    if drawing:
        fillmatrix[mouseingrid[0]][mouseingrid[1]] = 1
    if erasing:
        fillmatrix[mouseingrid[0]][mouseingrid[1]] = 0

    drawgrid(n, fillmatrix)

    pg.draw.rect(screen, (60, 60, 60), (h, 0, w-h, h))

    dt = clock.tick(fps) / 1000
    pg.display.flip()

if save:
    export("glmrenderer\ByteBlast\maps\map1.txt", fillmatrix)

pg.quit()
