import glm

<<<<<<< HEAD
def badtrianglefrustum(a, b, c, fovdistance, w, h):
    hdivw = h / w
    ratex = 1 / fovdistance
    ratey = ratex*hdivw
    if (-a.z * ratex < a.x) and (-b.z * ratex < b.x) and (-c.z * ratex < c.x):
        return False
    if (a.z * ratex > a.x) and (b.z * ratex > b.x) and (c.z * ratex > c.x):
        return False
    if (-a.z * ratey < a.y) and (-b.z * ratey < b.y) and (-c.z * ratey < c.y):
        return False
    if (a.z * ratey > a.y) and (b.z * ratey > b.y) and (c.z * ratey > c.y):
        return False
    return True

=======

def badtrianglefrustum(a, b, c, fovdistance, w, h, near):
    wdivh = w / h
    ratey = 1 / fovdistance
    ratex = ratey
    tf = [1, 1, 1]
    if not (
        (
            (a.z * ratex < a.x < -a.z * ratex)
            and (a.z * ratey < a.y * wdivh < -a.z * ratey)
        )
        and not a.z > -near
    ):
        tf[0] = 0
    if not (
        (
            (b.z * ratex < b.x < -b.z * ratex)
            and (b.z * ratey < b.y * wdivh < -b.z * ratey)
        )
        and not b.z > -near
    ):
        tf[1] = 0
    if not (
        (
            (c.z * ratex < c.x < -c.z * ratex)
            and (c.z * ratey < c.y * wdivh < -c.z * ratey)
        )
        and not c.z > -near
    ):
        tf[2] = 0
    if sum(tf) == 0:
        return False
    return True


def getkn(a, b):
    dx = a.x - b.x
    if dx == 0:
        return (None, a.x)
    dy = b.y - a.y
    k = dy / dx
    n = a.y - k * a.x
    return (k, n)


def inrect(a, w, h):
    if abs(a.x - w / 2) > w / 2 or abs(a.y - h / 2) > h / 2:
        return False
    return True


def getyintersect(equation, y):
    if equation[0] == None:
        return equation[1]
    if equation[0] == 0 and equation[1 == y]:
        return 0
    if equation[0] == 0:
        return None
    return (y - equation[1]) / equation[0]


def getxintersect(equation, x):
    if equation[0] == None and equation[1] == x:
        return 0
    elif equation[0] == None:
        return None
    return equation[0] * x + equation[1]


>>>>>>> 57d0a272380c60773a3547b75e817f15ddb3737c
def trianglefrustum(a, b, c, w, h):
    return True
    if a.x>w and b.x>w and c.x>w:
        return False
    if a.x<0 and b.x<0 and c.x<0:
        return False
    if a.y>h and b.y>h and c.y>h:
        return False
    if a.y<0 and b.y<0 and c.y<0:
        return False
    return True
<<<<<<< HEAD
    
=======
    equationab = getkn(a, b)
    equationbc = getkn(b, c)
    equationca = getkn(c, a)
    nxh = getyintersect(equationab, -h / 2)
    if nxh != None and w / 2 <= nxh <= w / 2:
        return True
    pxh = getyintersect(equationab, h / 2)
    if pxh != None and w / 2 <= pxh <= w / 2:
        return True
    nyw = getyintersect(equationab, -w / 2)
    if nyw != None and w / 2 <= nyw <= w / 2:
        return True
    pyw = getyintersect(equationab, w / 2)
    if pyw != None and w / 2 <= pyw <= w / 2:
        return True

    nxh = getyintersect(equationbc, -h / 2)
    if nxh != None and w / 2 <= nxh <= w / 2:
        return True
    pxh = getyintersect(equationbc, h / 2)
    if pxh != None and w / 2 <= pxh <= w / 2:
        return True
    nyw = getyintersect(equationbc, -w / 2)
    if nyw != None and w / 2 <= nyw <= w / 2:
        return True
    pyw = getyintersect(equationbc, w / 2)
    if pyw != None and w / 2 <= pyw <= w / 2:
        return True

    nxh = getyintersect(equationca, -h / 2)
    if nxh != None and w / 2 <= nxh <= w / 2:
        return True
    pxh = getyintersect(equationca, h / 2)
    if pxh != None and w / 2 <= pxh <= w / 2:
        return True
    nyw = getyintersect(equationca, -w / 2)
    if nyw != None and w / 2 <= nyw <= w / 2:
        return True
    pyw = getyintersect(equationca, w / 2)
    if pyw != None and w / 2 <= pyw <= w / 2:
        return True

    return False
>>>>>>> 57d0a272380c60773a3547b75e817f15ddb3737c


def infrustum(point, fovdistance, w, h, near):
    hdivw = h / w
    ratex = 1 / fovdistance
    ratey = ratex * hdivw
    if point.z > -near:
        return False
    if (point.z * ratex < point.x < -point.z * ratex) and (
        point.z * ratey < point.y < -point.z * ratey
    ):
        return True
    return False
