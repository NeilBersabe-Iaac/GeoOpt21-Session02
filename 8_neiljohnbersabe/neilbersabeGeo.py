from pickle import LIST
import flask as Flask
import ghhops_server as hs
import geometry as geo
import random as r
import rhino3dm as rg
import Numpy as np

app=Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/neil_practice",
    name = "neilpractice",
    inputs=[
        hs.HopsNumber("Width","W","Width of the Rectangle",hs.HopsParamAccess.ITEM,default=50.0)
        hs.HopsNumber("Length","L","Length of the Rectangle",hs.HopsParamAccess.ITEM,default=80.0)
        hs.HopsInteger("Population","P","Population Count",hs.HopsParamAccess.ITEM,default=20)
        hs.HopsInteger("Seed","S","Seed",hs.HopsParamAccess.ITEM,default=3)
        hs.HopsNumber("Building_Scale","Bs","Building Scale",hs.HopsParamAccess.ITEM,default=0.815)
        hs.HopsNumber("Reduction_Factor","Rf","Percentage Reduction",hs.HopsParamAccess.ITEM,default=0.15)
        hs.HopsNumber("Min_Height","minHeight","Minimum Building Height",hs.HopsParamAccess.ITEM,default=3)
        hs.HopsNumber("Max_Height","maxHeight","Maximum Building Height",hs.HopsParamAccess.ITEM,default=28)
    ],
    outputs=[
    hs.HopsGeometry("Building","Bldg","Building Geometries",hs.HopsParamAccess.LIST)
    
    ]
)

def createBuildings(width,length,population,seed,bldgScale,reducF,minH,maxH):
    rg.voronoi
    return

