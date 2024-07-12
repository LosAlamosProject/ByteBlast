import pygame as pg
import numpy as np
import math as mt
import time as time
import glm
from renderclasses import *
from objfiles import *
from levelexporter import *

near = 0.1

plr = player(
    glm.vec3(0, 5, 15), glm.vec2(0, 0), 15
)

pg.init()

w = pg.display.Info().current_w
h = pg.display.Info().current_h

screen = pg.display.set_mode((w, h))

fps = 1440
clock = pg.time.Clock()


pg.mouse.set_visible(False)


objects = []

lightsources = []

starttime = time.time()
"""importfile(
    "C:\\Users\\User\\Downloads\\glmrenderer\\models\\player.txt",
    glm.vec3(0, mt.pi / 2, 0),
    glm.vec3(0, -15, 0),
    objects,
    32,
    screen,
    w,
    h
)"""

importmap("C:\\Users\\User\\Downloads\\glmrenderer\\maps\\map1.txt", 5, objects, plr, lightsources)

print(time.time() - starttime)

ambient = light(glm.vec3(0, 0, 0), 0, glm.vec3(1, 1, 1))

for i in lightsources:
    objects.append(
        triangle(
            glm.vec3(-0.5, -0.5, 0.5) + i.pos,
            glm.vec3(0.5, -0.5, 0.5) + i.pos,
            glm.vec3(-0.5, -0.5, -0.5) + i.pos,
            glm.vec3(0, 1, 0),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(0.5, -0.5, -0.5) + i.pos,
            glm.vec3(0.5, -0.5, 0.5) + i.pos,
            glm.vec3(-0.5, -0.5, -0.5) + i.pos,
            glm.vec3(0, 1, 0),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(-0.5, 0.5, 0.5) + i.pos,
            glm.vec3(0.5, 0.5, 0.5) + i.pos,
            glm.vec3(-0.5, 0.5, -0.5) + i.pos,
            glm.vec3(0, -1, 0),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(0.5, 0.5, -0.5) + i.pos,
            glm.vec3(0.5, 0.5, 0.5) + i.pos,
            glm.vec3(-0.5, 0.5, -0.5) + i.pos,
            glm.vec3(0, -1, 0),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(-0.5, 0.5, -0.5) + i.pos,
            glm.vec3(0.5, 0.5, -0.5) + i.pos,
            glm.vec3(-0.5, -0.5, -0.5) + i.pos,
            glm.vec3(0, 0, 1),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(0.5, -0.5, -0.5) + i.pos,
            glm.vec3(0.5, 0.5, -0.5) + i.pos,
            glm.vec3(-0.5, -0.5, -0.5) + i.pos,
            glm.vec3(0, 0, 1),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(-0.5, 0.5, 0.5) + i.pos,
            glm.vec3(0.5, 0.5, 0.5) + i.pos,
            glm.vec3(-0.5, -0.5, 0.5) + i.pos,
            glm.vec3(0, 0, -1),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(0.5, -0.5, 0.5) + i.pos,
            glm.vec3(0.5, 0.5, 0.5) + i.pos,
            glm.vec3(-0.5, -0.5, 0.5) + i.pos,
            glm.vec3(0, 0, -1),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(-0.5, 0.5, -0.5) + i.pos,
            glm.vec3(-0.5, -0.5, -0.5) + i.pos,
            glm.vec3(-0.5, 0.5, 0.5) + i.pos,
            glm.vec3(1, 0, 0),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(-0.5, -0.5, 0.5) + i.pos,
            glm.vec3(-0.5, -0.5, -0.5) + i.pos,
            glm.vec3(-0.5, 0.5, 0.5) + i.pos,
            glm.vec3(1, 0, 0),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(0.5, 0.5, -0.5) + i.pos,
            glm.vec3(0.5, -0.5, -0.5) + i.pos,
            glm.vec3(0.5, 0.5, 0.5) + i.pos,
            glm.vec3(-1, 0, 0),
            glm.vec3(1, 1, 1),
            2,
        )
    )
    objects.append(
        triangle(
            glm.vec3(0.5, -0.5, 0.5) + i.pos,
            glm.vec3(0.5, -0.5, -0.5) + i.pos,
            glm.vec3(0.5, 0.5, 0.5) + i.pos,
            glm.vec3(-1, 0, 0),
            glm.vec3(1, 1, 1),
            2,
        )
    )

objects.append(enemy(glm.vec3(0, -5, 10), 3, 1)) #the og

fov = 90
distance = 1 / mt.tan(fov / 360 * mt.pi)

pg.mouse.set_pos(w / 2, h / 2)

dt = 1 / fps

renderedtrianglecount = 0

font = pg.font.SysFont(None, 50)

running = True
while running:
    screen.fill((124, 41, 42))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keystates = pg.key.get_pressed()
    currentfps = clock.get_fps()

    renderedtrianglecount = 0

    plr.update(dt)

    plr.v.x = 0
    plr.v.y = 0
    plr.v.z = 0
    if keystates[pg.K_w]:
        plr.v.z -= plr.cosrot.y * plr.speed
        plr.v.x += plr.sinrot.y * plr.speed
    if keystates[pg.K_s]:
        plr.v.z += plr.cosrot.y * plr.speed
        plr.v.x -= plr.sinrot.y * plr.speed
    if keystates[pg.K_a]:
        plr.v.x -= plr.cosrot.y * plr.speed
        plr.v.z -= plr.sinrot.y * plr.speed
    if keystates[pg.K_d]:
        plr.v.x += plr.cosrot.y * plr.speed
        plr.v.z += plr.sinrot.y * plr.speed
    if keystates[pg.K_UP]:
        plr.v.z -= plr.cosrot.y * plr.speed
        plr.v.x += plr.sinrot.y * plr.speed
    if keystates[pg.K_DOWN]:
        plr.v.z += plr.cosrot.y * plr.speed
        plr.v.x -= plr.sinrot.y * plr.speed
    if keystates[pg.K_LEFT]:
        plr.orientation.x += 0.02
    if keystates[pg.K_RIGHT]:
        plr.orientation.x -= 0.02
    if keystates[pg.K_SPACE]:
        plr.v.y += plr.speed
    if keystates[pg.K_LSHIFT]:
        plr.v.y -= plr.speed

    mousepos = pg.mouse.get_pos()
    plr.orientation.x += (w / 2 - mousepos[0]) * 0.01
    plr.orientation.y += (mousepos[1] - h / 2) * 0.01
    pg.mouse.set_pos(w / 2, h / 2)

    objects.sort()

    for i in objects:
        renderedtrianglecount += i.draw(
            screen, plr, distance, w, h, lightsources, ambient, near
        )
        # i.update(dt, plr)

    text = font.render(str(round(currentfps, 2)) + " fps", True, (255, 255, 255))
    screen.blit(text, (0, 0))
    text = font.render(str(round(currentfps * 60, 2)) + " fpm", True, (255, 255, 255))
    screen.blit(text, (0, 50))
    text = font.render(str(round(currentfps * 3600, 2)) + " fph", True, (255, 255, 255))
    screen.blit(text, (0, 100))
    text = font.render("Total objects: " + str(len(objects)), True, (255, 255, 255))
    screen.blit(text, (0, 150))
    text = font.render(
        "Rendered objects: " + str(renderedtrianglecount), True, (255, 255, 255)
    )
    screen.blit(text, (0, 200))

    dt = clock.tick(fps) / 1000
    pg.display.flip()
pg.quit()
