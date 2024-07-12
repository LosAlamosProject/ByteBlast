from renderclasses import*

def export(path, fillmatrix):
    with open(path, "w") as f:
        n = len(fillmatrix)
        for i in range(n):
            line = ""
            for j in range(n):
                line+=str(fillmatrix[j][i])
            f.write(line + "\n")
        f.close()

def importmap(path, scale, objects, plr, lightsources):
    with open(path, "r") as f:
        l = f.readlines()
        if f==[]:
            raise Exception("Map at file location is empty")
        n = len(l[0])-1
        offset = -scale*n/2
        for i in range(n):
            for j in range(n):
                if l[i][j]=='0':
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(0, 1, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(0, 1, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                
                if l[i][j]=='4':
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(0, 1, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(0, 1, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )

                    lightsources.append(light(glm.vec3(offset+i*scale, scale+0.5, offset+j*scale), 100, glm.vec3(1, 1, 1)))

                if l[i][j]=='2':
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(0, 1, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(0, 1, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                    objects.append(enemy(glm.vec3(offset+i*scale, 2, offset+j*scale), 4, 1))
                
                if l[i][j]=='3':
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(0, 1, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(0, 1, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                    plr.pos = glm.vec3(offset+i*scale, 2, offset+j*scale)
                
                if l[i][j]=='1':
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale+scale/2, scale, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, scale, offset+j*scale-scale/2),
                            glm.vec3(1, 0, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, scale, offset+j*scale-scale/2),
                            glm.vec3(1, 0, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )

                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale-scale/2, scale, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale-scale/2, scale, offset+j*scale-scale/2),
                            glm.vec3(-1, 0, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale-scale/2, scale, offset+j*scale-scale/2),
                            glm.vec3(-1, 0, 0),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )

                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale+scale/2, scale, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale-scale/2, scale, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(0, 0, 1),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale-scale/2, scale, offset+j*scale+scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale+scale/2),
                            glm.vec3(0, 0, 1),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )

                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale+scale/2, scale, offset+j*scale-scale/2),
                            glm.vec3(offset+i*scale-scale/2, scale, offset+j*scale-scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(0, 0, -1),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
                    objects.append(
                        triangle(
                            glm.vec3(offset+i*scale-scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(offset+i*scale-scale/2, scale, offset+j*scale-scale/2),
                            glm.vec3(offset+i*scale+scale/2, 0, offset+j*scale-scale/2),
                            glm.vec3(0, 0, -1),
                            glm.vec3(1, 1, 1),
                            -1,
                        )
                    )
        f.close()