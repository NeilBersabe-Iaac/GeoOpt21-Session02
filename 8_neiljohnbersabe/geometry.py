import rhino3dm as rg
import networkx as nx
import numpy as np

def createBasePoints(step,count):
    #Set the Start point
    basePointsList = [(rg.Point3d(0,0,0))]
    xBp = 0
    for i in range(count):
        xBp += step

        basePoints = rg.Point3d(xBp,0,0)
        basePointsList.append(basePoints)
    
    return basePointsList



def createMidPoints1(step,count,offset,period,shift,amplitude):
    #Set the Start point
    midPointsList = [(rg.Point3d(0,np.sin(shift)*amplitude,offset))]
    xBp = 0
    yBp = 0
    for i in range(count):
        xBp += step
        yBp = (np.sin(((i+step)*period)+shift))*amplitude
   
        midPoints1 = rg.Point3d(xBp,yBp,offset)
        midPointsList.append(midPoints1)
    
    return midPointsList


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


def createTopPoints(step,count,offset):
    #Set the Start point
    topPointsList = [(rg.Point3d(0,0,offset))]
    xBp = 0
    
    for i in range(count):
        xBp += step
       
        topPoints = rg.Point3d(xBp,0,offset)
        topPointsList.append(topPoints)
    
    return topPointsList

# def createNodes(0000,)
#     G = nx.Graph(G)

#     nodes = []



# def createFloors(Plane,Radius):
#     # for i in basePointsList:
#     #     floorRec = rg.Rectangle3d(i,Width,Length)
        
#     floorR = rg.Circle(Plane, Radius)
#     return floorR
