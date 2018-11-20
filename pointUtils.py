from math import sqrt

def pointDistance(point1,point2):
    return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def centroid(points):
    n=len(points)
    xBar=sum(map(lambda p:p[0],points))/n
    yBar=sum(map(lambda p:p[1],points))/n
    return (xBar,yBar)

def boundingCircle(points):
    center=centroid(points)

    return center, max(map(lambda p:pointDistance(center,p),points))

def boundingBox(points):

    xMin=min(points,key=lambda p:p[0])[0]
    yMin=min(points,key=lambda p:p[1])[1]
    xMax=max(points,key=lambda p:p[0])[0]
    yMax=max(points,key=lambda p:p[1])[1]

    return (xMin,yMin,xMax,yMax)

def boundingBoxSize(box):
    return (box[2]-box[0],box[3]-box[1])

def superBoundingBox(boxes):
    if not isinstance(boxes,list):
        boxes=list(boxes)
    xMin=min(boxes,key=lambda b:b[0])[0]
    yMin=min(boxes,key=lambda b:b[1])[1]
    xMax=max(boxes,key=lambda b:b[2])[2]
    yMax=max(boxes,key=lambda b:b[3])[3]

    return(xMin,yMin,xMax,yMax)

def boxCenter(box):
    return((box[2]+box[0])/2,(box[3]+box[1])/2)

def normalizePoint(point,oldBox,newSize):
    oldSize=boundingBoxSize(oldBox)
    return (newSize[0]*(point[0]-oldBox[0])/oldSize[0],newSize[1]*(point[1]-oldBox[1])/oldSize[1])

