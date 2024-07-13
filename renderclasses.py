import glm
import math as mt
import pygame as pg
from frustum import *


class light:
    __slots__ = ("pos", "brightness", "color")

    def __init__(self, pos: glm.vec3, brightness: float, color: glm.vec3):
        self.pos = pos
        self.brightness = brightness
        self.color = color


class player:
    __slots__ = ("pos", "orientation", "speed", "v", "a", "sinrot", "cosrot", "rmat")

    def __init__(self, pos: glm.vec3, orientation: glm.vec2, speed: float):
        self.pos = pos
        self.orientation = orientation
        self.speed = speed
        self.v = glm.vec3(0, 0, 0)
        self.a = glm.vec3(0, 0, 0)
        sin_b = mt.sin(self.orientation.y)
        sin_a = mt.sin(self.orientation.x)
        cos_b = mt.cos(self.orientation.y)
        cos_a = mt.cos(self.orientation.x)
        self.sinrot = glm.vec2(sin_b, -sin_a)
        self.cosrot = glm.vec2(cos_b, cos_a)
        self.rmat = glm.mat3x3(
            [cos_a, 0, -sin_a],
            [-sin_a * sin_b, cos_b, -cos_a * sin_b],
            [sin_a * cos_b, sin_b, cos_a * cos_b],
        )

    def update(self, dt):
        self.v += self.a * dt / 2
        self.pos += self.v * dt
        self.v += self.a * dt / 2
        self.orientation.y = max(
            -mt.pi / 2 + 0.05, min(mt.pi / 2 - 0.05, self.orientation.y)
        )
        sin_b = mt.sin(self.orientation.y)
        sin_a = mt.sin(self.orientation.x)
        cos_b = mt.cos(self.orientation.y)
        cos_a = mt.cos(self.orientation.x)
        self.sinrot = glm.vec2(sin_b, -sin_a)
        self.cosrot = glm.vec2(cos_b, cos_a)
        self.rmat = glm.mat3x3(
            [cos_a, 0, -sin_a],
            [-sin_a * sin_b, cos_b, -cos_a * sin_b],
            [sin_a * cos_b, sin_b, cos_a * cos_b],
        )


class enemy:
    __slots__ = (
        "pos",
        "speed",
        "type",
        "facing",
        "texture",
        "texsize",
        "center",
        "maxsize",
    )

    def __init__(self, pos: glm.vec3, speed: float, type: int):
        self.pos = pos
        self.speed = speed
        self.type = type
        self.facing = glm.vec3(1, 0, 0)
        self.texture = pg.image.load("glmrenderer\ByteBlast\images\demon.png")
        self.texture = pg.transform.scale(self.texture, (500, 500))
        self.texsize = glm.vec2(500, 500)
        self.center = pos.z

    def draw(
        self,
        screen,
        plr,
        fovdistance,
        w,
        h,
        lightsources: list[light],
        ambient: light,
        near: float,
    ):
        rpos = self.pos - plr.pos
        rpos = rpos @ plr.rmat
        self.center = rpos.z
        if infrustum(rpos, fovdistance, w, h, near):
            imagescale = 5 / mt.sqrt(
                glm.dot((self.pos - plr.pos), (self.pos - plr.pos))
            )
            if (
                self.texsize.x * imagescale < 4
                or self.texsize.y * imagescale < 4
                or imagescale > 3
            ):
                return 0
            newtexture = self.texture
            newtexture = pg.transform.scale_by(newtexture, imagescale)
            blitpos = proj(rpos, fovdistance, w, h) - self.texsize * imagescale / 2
            screen.blit(newtexture, blitpos)
            return 1
        return 0

    def update(self, dt, plr):
        self.facing = glm.normalize(
            plr.pos - self.pos - 2 * glm.normalize(plr.pos - self.pos)
        )
        self.pos += self.facing * self.speed * dt

    def mintest(self):
        return self.center

    def __lt__(self, other):
        return self.mintest() < other.mintest()


class triangle:
    __slots__ = (
        "a",
        "b",
        "c",
        "n",
        "rota",
        "rotb",
        "rotc",
        "center",
        "clr",
        "refl",
        "objectfrustumcheck",
    )

    def __init__(
        self,
        a: glm.vec3,
        b: glm.vec3,
        c: glm.vec3,
        n: glm.vec3,
        clr: glm.vec3,
        reflectance: float,
    ):
        self.a = a
        self.b = b
        self.c = c
        self.n = glm.normalize(n)
        self.rota = a
        self.rotb = b
        self.rotc = c
        self.center = (self.rota.z + self.rotb.z + self.rotc.z) / 3
        self.clr = clr
        self.refl = reflectance

    def draw(
        self,
        screen: pg.surface.Surface,
        plr: player,
        distance: float,
        w: int,
        h: int,
        lightsources,
        ambient: light,
        near: float,
    ):
        checkdir = glm.dot((plr.pos - self.a), self.n)
        if checkdir < 0:
            return 0
        self.rota = self.a - plr.pos
        self.rota = self.rota @ plr.rmat

        self.rotb = self.b - plr.pos
        self.rotb = self.rotb @ plr.rmat

        self.rotc = self.c - plr.pos
        self.rotc = self.rotc @ plr.rmat

        self.center = (
            max(self.rota.z, self.rotb.z, self.rotc.z)
            + min(self.rota.z, self.rotb.z, self.rotc.z)
        ) / 2

        avgpos = glm.vec3(
            (self.a.x + self.b.x + self.c.x) / 3,
            (self.a.y + self.b.y + self.c.y) / 3,
            (self.a.z + self.b.z + self.c.z) / 3,
        )

<<<<<<< HEAD
        if badtrianglefrustum(self.rota, self.rotb, self.rotc, distance, w, h):
            return self.frustumdraw(screen, self.rota, self.rotb, self.rotc, distance, near, w, h, avgpos, lightsources, ambient, plr)
        return 0
    
=======
        return self.frustumdraw(
            screen,
            self.rota,
            self.rotb,
            self.rotc,
            distance,
            near,
            w,
            h,
            avgpos,
            lightsources,
            ambient,
            plr,
        )

>>>>>>> 57d0a272380c60773a3547b75e817f15ddb3737c
    def shade(self, avgpos, lightsources, ambient, plr):
        color = self.clr * ambient.color * ambient.brightness

        for i in lightsources:
            lightminusself = i.pos - avgpos
            inversesquarelawmultiplier = 1 / glm.dot(lightminusself, lightminusself)

            ldir = glm.normalize(i.pos - avgpos)
            diff = max(0, glm.dot(ldir, self.n))
            diffuse = i.color * diff
            color += diffuse * inversesquarelawmultiplier * i.brightness

            if self.refl != -1:
                vdir = glm.normalize(plr.pos - avgpos)
                hdir = glm.normalize(vdir + ldir)
                spec = max(0, glm.dot(hdir, self.n), 0) ** self.refl
                specular = i.color * spec
                color += specular * inversesquarelawmultiplier * i.brightness

        color.x = min(1, max(0, color.x))
        color.y = min(1, max(0, color.y))
        color.z = min(1, max(0, color.z))

        return color

    def frustumdraw(
        self, screen, a, b, c, distance, near, w, h, avgpos, lightsources, ambient, plr
    ):
        if a.z <= -near and b.z <= -near and c.z <= -near:
            pos1 = proj(a, distance, w, h)
            pos2 = proj(b, distance, w, h)
            pos3 = proj(c, distance, w, h)
<<<<<<< HEAD
            color = self.shade(avgpos, lightsources, ambient, plr)
            pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3))
            return 1
        
        if a.z<=-near and b.z>-near and c.z>-near:
            abdir = (b-a)
            abdir = abdir/abdir.z
            abintensity = -near-a.z
            binterpoint = a + abdir*abintensity
=======
            if trianglefrustum(pos1, pos2, pos3, w, h):
                color = self.shade(avgpos, lightsources, ambient, plr)
                pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3))
                return 1
>>>>>>> 57d0a272380c60773a3547b75e817f15ddb3737c

        if a.z <= -near and b.z > -near and c.z > -near:
            abdir = b - a
            abdir = abdir / abdir.z
            abintensity = -near - a.z
            binterpoint = a + abdir * abintensity

            acdir = c - a
            acdir = acdir / acdir.z
            acintensity = -near - a.z
            cinterpoint = a + acdir * acintensity
            pos1 = proj(a, distance, w, h)
            pos2 = proj(binterpoint, distance, w, h)
            pos3 = proj(cinterpoint, distance, w, h)
<<<<<<< HEAD
            color = self.shade(avgpos, lightsources, ambient, plr)
            pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3)) 
            return 1
        
        if a.z>-near and b.z<=-near and c.z>-near:
            badir = (a-b)
            badir = badir/badir.z
            baintensity = -near-b.z
            ainterpoint = b + badir*baintensity
=======
            if trianglefrustum(pos1, pos2, pos3, w, h):
                color = self.shade(avgpos, lightsources, ambient, plr)
                pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3))
                return 1
>>>>>>> 57d0a272380c60773a3547b75e817f15ddb3737c

        if a.z > -near and b.z <= -near and c.z > -near:
            badir = a - b
            badir = badir / badir.z
            baintensity = -near - b.z
            ainterpoint = b + badir * baintensity

            bcdir = c - b
            bcdir = bcdir / bcdir.z
            bcintensity = -near - b.z
            cinterpoint = b + bcdir * bcintensity
            pos1 = proj(ainterpoint, distance, w, h)
            pos2 = proj(b, distance, w, h)
            pos3 = proj(cinterpoint, distance, w, h)
<<<<<<< HEAD
            color = self.shade(avgpos, lightsources, ambient, plr)
            pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3))
            return 1
        
        if a.z>-near and b.z>-near and c.z<=-near:
            cadir = (a-c)
            cadir = cadir/cadir.z
            caintensity = -near-c.z
            ainterpoint = c + cadir*caintensity
=======
            if trianglefrustum(pos1, pos2, pos3, w, h):
                color = self.shade(avgpos, lightsources, ambient, plr)
                pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3))
                return 1
>>>>>>> 57d0a272380c60773a3547b75e817f15ddb3737c

        if a.z > -near and b.z > -near and c.z <= -near:
            cadir = a - c
            cadir = cadir / cadir.z
            caintensity = -near - c.z
            ainterpoint = c + cadir * caintensity

            cbdir = c - b
            cbdir = cbdir / cbdir.z
            cbintensity = -near - c.z
            binterpoint = c + cbdir * cbintensity
            pos1 = proj(ainterpoint, distance, w, h)
            pos2 = proj(binterpoint, distance, w, h)
            pos3 = proj(c, distance, w, h)
<<<<<<< HEAD
            color = self.shade(avgpos, lightsources, ambient, plr)
            pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3))
            return 1
        
        if a.z<=-near and b.z<=-near and c.z>-near:
            acdir = (c-a)
            acdir = acdir/acdir.z
            acintensity = -near-a.z
            acinterpoint = a + acdir*acintensity
=======
            if trianglefrustum(pos1, pos2, pos3, w, h):
                color = self.shade(avgpos, lightsources, ambient, plr)
                pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3))
                return 1
>>>>>>> 57d0a272380c60773a3547b75e817f15ddb3737c

        if a.z <= -near and b.z <= -near and c.z > -near:
            acdir = c - a
            acdir = acdir / acdir.z
            acintensity = -near - a.z
            acinterpoint = a + acdir * acintensity

            bcdir = c - b
            bcdir = bcdir / bcdir.z
            bcintensity = -near - b.z
            bcinterpoint = b + bcdir * bcintensity
            pos1 = proj(a, distance, w, h)
            pos2 = proj(b, distance, w, h)
            pos3 = proj(bcinterpoint, distance, w, h)
            pos4 = proj(acinterpoint, distance, w, h)
<<<<<<< HEAD
            color = self.shade(avgpos, lightsources, ambient, plr)
            pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3, pos4))
            return 2
        
        if a.z>-near and b.z<=-near and c.z<=-near:
            cadir = (a-c)
            cadir = cadir/cadir.z
            caintensity = -near-c.z
            cainterpoint = c + cadir*caintensity
=======
            if trianglefrustum(pos1, pos2, pos3, w, h) or trianglefrustum(
                pos2, pos3, pos4, w, h
            ):
                color = self.shade(avgpos, lightsources, ambient, plr)
                pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3, pos4))
                return 2
>>>>>>> 57d0a272380c60773a3547b75e817f15ddb3737c

        if a.z > -near and b.z <= -near and c.z <= -near:
            cadir = a - c
            cadir = cadir / cadir.z
            caintensity = -near - c.z
            cainterpoint = c + cadir * caintensity

            badir = a - b
            badir = badir / badir.z
            baintensity = -near - b.z
            bainterpoint = b + badir * baintensity
            pos1 = proj(bainterpoint, distance, w, h)
            pos2 = proj(b, distance, w, h)
            pos3 = proj(c, distance, w, h)
            pos4 = proj(cainterpoint, distance, w, h)
<<<<<<< HEAD
            color = self.shade(avgpos, lightsources, ambient, plr)
            pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3, pos4))
            return 2
        
        if a.z<=-near and b.z>-near and c.z<=-near:
            abdir = (b-a)
            abdir = abdir/abdir.z
            abintensity = -near-a.z
            abinterpoint = a + abdir*abintensity
=======
            if trianglefrustum(pos1, pos2, pos3, w, h) or trianglefrustum(
                pos2, pos3, pos4, w, h
            ):
                color = self.shade(avgpos, lightsources, ambient, plr)
                pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3, pos4))
                return 2
>>>>>>> 57d0a272380c60773a3547b75e817f15ddb3737c

        if a.z <= -near and b.z > -near and c.z <= -near:
            abdir = b - a
            abdir = abdir / abdir.z
            abintensity = -near - a.z
            abinterpoint = a + abdir * abintensity

            cbdir = b - c
            cbdir = cbdir / cbdir.z
            cbintensity = -near - c.z
            cbinterpoint = c + cbdir * cbintensity
            pos1 = proj(a, distance, w, h)
            pos2 = proj(abinterpoint, distance, w, h)
            pos3 = proj(cbinterpoint, distance, w, h)
            pos4 = proj(c, distance, w, h)
<<<<<<< HEAD
            color = self.shade(avgpos, lightsources, ambient, plr)
            pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3, pos4))
            return 2
=======
            if trianglefrustum(pos1, pos2, pos3, w, h) or trianglefrustum(
                pos2, pos3, pos4, w, h
            ):
                color = self.shade(avgpos, lightsources, ambient, plr)
                pg.draw.polygon(screen, color * 255, (pos1, pos2, pos3, pos4))
                return 2

>>>>>>> 57d0a272380c60773a3547b75e817f15ddb3737c
        return 0

    def update(self, dt, plr):
        pass

    def mintest(self):
        return self.center

    def __lt__(self, other):
        return self.mintest() < other.mintest()


def proj(point: glm.vec3, distance: float, w: int, h: int):
    if point.z == 0:
        return (1000000, 1000000)

    projectedx = -point.x / point.z * distance * w * 0.5 + w / 2
    projectedy = point.y / point.z * distance * w * 0.5 + h / 2
    return glm.vec2(projectedx, projectedy)
