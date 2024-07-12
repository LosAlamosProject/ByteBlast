from renderclasses import*

def nthvn(n: int, l):
    counter = 0
    for i in l:
        if i[1] == "n":
            counter += 1
        if counter == n:
            return i


def getvec3fromstr(string: str):
    digitsandminus = [".", "-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "e"]
    returnvectorvalues = ["", "", ""]
    counter = -1
    for i in string:
        if i == " ":
            counter += 1
        if i in digitsandminus:
            returnvectorvalues[counter] += i
    if "e-" in returnvectorvalues[0]:
        returnvectorvalues[0] = 0
    if "e-" in returnvectorvalues[1]:
        returnvectorvalues[1] = 0
    if "e-" in returnvectorvalues[2]:
        returnvectorvalues[2] = 0
    return glm.vec3(
        float(returnvectorvalues[0]),
        float(returnvectorvalues[1]),
        float(returnvectorvalues[2]),
    )


def importfile(
    path: str, rotation=glm.vec3(0, 0, 0), pos=glm.vec3(0, 0, 0), triangles=None, refl=32, screen = pg.surface.Surface, w=int, h=int
):
    errors = False
    if triangles == None:
        print("please forward triangles to the importfile function")
        errors = True
    if errors:
        return None
    f = open(path, "r")
    l = f.readlines()
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    counter = 0
    total = len(l)

    vertexnormals = []

    for i in l:
        if i[1] == "n":
            vertexnormals.append(getvec3fromstr(i[:-1]))
        if i[0] == "f":
            nums = ["" for k in range(9)]
            ind = 0
            for j in i[2:]:
                if j in digits:
                    nums[ind] += j
                elif j == "/" or j == " ":
                    if nums[ind] == '':
                        nums[ind] = 0
                    nums[ind] = int(nums[ind])
                    ind += 1
            nums[8] = int(nums[8])
            for j in range(3):
                nums[3 * j] = getvec3fromstr(l[nums[3 * j] + 3][0:-1])
                nums[3 * j + 2] = vertexnormals[nums[3 * j + 2] - 1]
            trianglenormal = glm.vec3(
                (nums[2].x + nums[5].x + nums[8].x) / 3,
                (nums[2].y + nums[5].y + nums[8].y) / 3,
                (nums[2].z + nums[5].z + nums[8].z) / 3,
            )
            triangles.append(
                triangle(
                    nums[0] + pos,
                    nums[3] + pos,
                    nums[6] + pos,
                    trianglenormal,
                    glm.vec3(1, 1, 1),
                    refl,
                )
            )
        if counter % (total / 100) < 2:
            screen.fill((0, 0, 0))
            pg.draw.rect(screen, (255, 255, 255), (w / 2 - 210, h - 110, 400, 50), 5)
            pg.draw.rect(
                screen,
                (255, 255, 255),
                (w / 2 - 203, h - 103, 386 * counter / total, 36),
            )
            font = pg.font.SysFont(None, 35)
            text = font.render(
                "Loading "
                + path
                + ": "
                + str(int(counter / total * 100))
                + r"% complete",
                True,
                (255, 255, 255),
            )
            wid = text.get_size()[0]
            screen.blit(text, (w / 2 - wid / 2, h - 150))
            pg.display.update()
        counter += 1
    f.close()