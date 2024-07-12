def trianglefrustum(a, b, c, fovdistance, w, h, near):
    wdivh = w / h
    ratey = 1 / fovdistance
    ratex = ratey
    tf = [1, 1, 1]
    if not (
        ((a.z * ratex < a.x < -a.z * ratex)
        and (a.z * ratey < a.y * wdivh < -a.z * ratey)) and not a.z>-near
    ):
        tf[0] = 0
    if not (
        ((b.z * ratex < b.x < -b.z * ratex)
        and (b.z * ratey < b.y * wdivh < -b.z * ratey)) and not b.z>-near
    ):
        tf[1] = 0
    if not (
        ((c.z * ratex < c.x < -c.z * ratex)
        and (c.z * ratey < c.y * wdivh < -c.z * ratey)) and not c.z>-near
    ):
        tf[2] = 0
    if sum(tf) == 0:
        return False
    return True

def infrustum(point, fovdistance, w, h, near):
    hdivw = h / w
    ratex = 1 / fovdistance
    ratey = ratex*hdivw
    if point.z>-near:
        return False
    if (point.z * ratex < point.x < -point.z * ratex) and (point.z * ratey < point.y < -point.z * ratey):
        return True
    return False