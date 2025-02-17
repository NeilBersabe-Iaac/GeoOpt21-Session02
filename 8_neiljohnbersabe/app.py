from tkinter.tix import Tree
from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo
import numpy as np
# import pandas as pd

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/neilbersabe_Hops",
    name = "neilbersabe Hops",
    inputs=[
         hs.HopsNumber("Step","S","Number of Steps",hs.HopsParamAccess.ITEM,default=1),
        hs.HopsInteger("Count","C","Number of Points",hs.HopsParamAccess.ITEM,default=15),
        hs.HopsNumber("Offset","Of","Offset distance",hs.HopsParamAccess.ITEM,default=7.5),
        hs.HopsNumber("Period","Per","Period",hs.HopsParamAccess.ITEM,default=0.4),
        hs.HopsNumber("Shift","Shft","Phase Shift",hs.HopsParamAccess.ITEM,default=0),
        hs.HopsNumber("Amplitude","Amp","Amplitutde",hs.HopsParamAccess.ITEM,default=5)
        #  ,hs.HopsNumber("Radius","R","Floor Radius",hs.HopsParamAccess.LIST,default=20)
        #  ,hs.HopsNumber("Width","W","Floor Width",hs.HopsParamAccess.ITEM,default=20),
        #  hs.HopsNumber("Length","L","Floor Length",hs.HopsParamAccess.ITEM,default=40)
        # hs.HopsInteger("Population","P",pulation Count",hs.HopsParamAccess.ITEM,default=20)
    
    ],
    outputs=[
    hs.HopsPoint("BasePoints","B","Base Points",hs.HopsParamAccess.LIST),
    hs.HopsPoint("MidPoints1","M1","Mid Points 1",hs.HopsParamAccess.LIST),
    hs.HopsPoint("MidPoints2","M2","Mid Points 2",hs.HopsParamAccess.LIST),
    hs.HopsPoint("TopPoints","T","Top Points",hs.HopsParamAccess.LIST)
    ,hs.HopsPoint("PointsList","000","Combined Clean Tree",hs.HopsParamAccess.TREE)

    # ,hs.HopsCurve("BasePole","bCrv","Base Curve",hs.HopsParamAccess.LIST)
    # ,hs.HopsCurve("MidPole","mCrv","Mid Curve",hs.HopsParamAccess.LIST)
    # ,hs.HopsCurve("TopPole","tCrv","Top Curve",hs.HopsParamAccess.LIST)
    
    ]
)
def createPoles(step,count,offset,period,shift,amplitude):
    #Set the Start point
    basePoints = geo.createBasePoints(step,count)
    midPoints1 = geo.createMidPoints1(step,count,offset,period,shift,amplitude)
    midPoints2 = geo.createMidPoints2(step,count,offset*2,period,shift+3,amplitude)
    topPoints = geo.createTopPoints(step,count,offset*3)
    pointsTree = basePoints+midPoints1+midPoints2+topPoints
    # floorR = geo.createFloors(seriesPoints,radius)

    # basePole = rg.Line(basePoints,midPoints1)
    # midPole = rg.Line(midPoints1,midPoints2)
    # topPole = rg.Line(midPoints2,topPoints)


    # floor = rg.Circle(rg.Point3d(0,0,0),5)
    return basePoints, midPoints1, midPoints2, topPoints, pointsTree
    print(pointsTree)

#####
#IM STUMPPED--!!__ by Neil John Bersabe XD
####
# I need to create a TREE data structure that holds the 4 lists separately and map each index to one another to create edges from them
#ex. [[1a,2a,3a,4a],[1b,2b,3b,4b],[1c,2c,3c,4c],[1d,2d,3c,4c]]
#something like this then i need to map each index and create edges like edge[1a][1b],edge[2a],[2b]


if __name__== "__main__":
    app.run(debug=True)