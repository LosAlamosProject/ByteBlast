import glm

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
