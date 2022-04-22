import rhino3dm as rg
import networkx as nx
import numpy as np




#########These Functions are similar to the series component of grasshopper
#########################################################################
#This is the list of Points for the Base
def createBasePoints(step,count):
    #Set the Start point
    basePointsList = [(rg.Point3d(0,0,0))]
    xBp = 0
    for i in range(count):
        xBp += step

        basePoints = rg.Point3d(xBp,0,0)
        basePointsList.append(basePoints)
    
    return basePointsList
# print(createBasePoints)
# print(basePointsList)

#This is the list of Points for the first Middle thirds
def createMidPoints1(step,count,offset,period,shift,amplitude):
    #Set the Start point
    midPointsList1 = [(rg.Point3d(0,np.sin(shift)*amplitude,offset))]
    xBp = 0
    yBp = 0
    for i in range(count):
        xBp += step
        yBp = (np.sin(((i+step)*period)+shift))*amplitude
   
        midPoints1 = rg.Point3d(xBp,yBp,offset)
        midPointsList1.append(midPoints1)
    
    return midPointsList1


#This is the list of Points for the second Middle thirds
def createMidPoints2(step,count,offset,period,shift,amplitude):
    #Set the Start point
    midPointsList2 = [(rg.Point3d(0,np.sin(shift)*amplitude,offset))]
    xBp = 0
    yBp = 0

    for i in range(count):
        xBp += step
        yBp = (np.sin(((i+step)*period)+shift))*amplitude

        midPoints2 = rg.Point3d(xBp,yBp,offset)
        midPointsList2.append(midPoints2)
    
    return midPointsList2


#This is the list of Points for the Top Points
def createTopPoints(step,count,offset):
    #Set the Start point
    topPointsList = [(rg.Point3d(0,0,offset))]
    xBp = 0
    
    for i in range(count):
        xBp += step
       
        topPoints = rg.Point3d(xBp,0,offset)
        topPointsList.append(topPoints)
    
    return topPointsList
#########################################################################


#IM STUMPPED!!
# I need to create a tree data structure that holds the 4 lists separately and map each index to one another to create edges from them
#ex. [[1a,2a,3a,4a],[1b,2b,3b,4b],[1c,2c,3c,4c],[1d,2d,3c,4c]]
#something like this then i need to map each index and create edges like edge[1a][1b],edge[2a],[2b]


# def createNodes(0000,)
#     G = nx.Graph(G)

#     nodes = []



# def createFloors(Plane,Radius):
#     # for i in basePointsList:
#     #     floorRec = rg.Rectangle3d(i,Width,Length)
        
#     floorR = rg.Circle(Plane, Radius)
#     return floorR
