from math import sqrt,acos,pi

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

def slopeIntercept(line):
    point1, point2 = line
    DeltaX = point1[0] - point2[0]
    DeltaY = point1[1] - point2[1]
    if abs(DeltaY) > abs(DeltaX):
        m = DeltaX / DeltaY
        b = point1[0] - point1[1] * m
        return True, m, b
    else:
        m = DeltaY / DeltaX
        b = point1[1] - point1[0] * m
        return False, m, b

def colinear(line1, line2, slopeTolerance, distTolerance):
    s1, m1, b1 = slopeIntercept(line1)
    s2, m2, b2 = slopeIntercept(line2)

    if s1 != s2:
        return False

    if abs(m1 - m2) > slopeTolerance:
        return False

    DeltaB = abs(b1 - b2)
    return DeltaB / sqrt(DeltaB ** 2 + 1) <= distTolerance

def angleBetween(line1,line2):
    vec1=line1[1][0]-line1[0][0],line1[1][1]-line1[0][1]
    vec2=line2[1][0]-line2[0][0],line2[1][1]-line2[0][1]
    len1=pointDistance(line1[0],line1[1])
    len2=pointDistance(line2[0],line2[1])
    normalizedDotProd=abs(vec1[0]*vec2[1]+vec1[1]*vec2[1])/(len1*len2)
    if normalizedDotProd>1:
        return pi/2
    return acos(normalizedDotProd)

def linesOverlap(line1, line2):
    i = 1 if slopeIntercept(line1)[0] else 0
    min1 = min(line1, key=lambda p: p[i])[i]
    min2 = min(line2, key=lambda p: p[i])[i]
    max1 = max(line1, key=lambda p: p[i])[i]
    max2 = max(line2, key=lambda p: p[i])[i]

    return min2 > max1 or min1 > max2

def linesAdjacent(line1, line2, slopeTolerance, distTolerance):
    return colinear(line1, line2, slopeTolerance, distTolerance) and linesOverlap(line1, line2)

def lines(poly):
    res = []
    for i, vert in enumerate(poly):
        res.append((poly[i - 1], vert))
    return res

def pointOrient(P,Q,R): #Returns 0 if all three points are in the same line,
    val=(Q[1]-P[1])*(R[0]-Q[0])-(Q[0]-P[0])*(R[1]-Q[1])
    return 0 if val==0 else (1 if val>0 else -1)

def linesCross(L1,L2):
    return pointOrient(L1[0],L1[1],L2[0])!=pointOrient(L1[0],L1[1],L2[1]) and pointOrient(L2[0],L2[1],L1[0])!=pointOrient(L2[0],L2[1],L1[1])

def perpLine(line,length=1,place=0):
    length/=pointDistance(line[0],line[1])
    X_0=(line[1][0]-line[0][0])*place+line[0][0]
    Y_0=(line[1][1]-line[0][1])*place+line[0][1]
    DeltaX=(line[1][0]-line[0][0])*length
    DeltaY=(line[1][1]-line[0][1])*length
    return (X_0,Y_0),(X_0+DeltaX,Y_0+DeltaY)