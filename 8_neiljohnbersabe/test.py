import rhino3dm as rg

rangeX = 10
stepX = 2
bPointsList = [(0,0,0)]
x = 0
for i in range(rangeX):
    x += stepX

    bPoints = (x,0,0)

    bPointsList.append(bPoints)

print(bPointsList)
print(tyoe(bPointsList))


    # basePointsList = [(0,0,0)]
    # x = 0
    # for i in range(count):
    #     x += step

    # basePoints = rg.Point3d(x,0,0)
    # basePointsList.append(bPoints)
    
    # return basePointsList
