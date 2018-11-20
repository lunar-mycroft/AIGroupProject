svgWidth = 200
svgHeight = 200
# list (string countyname , list( (x,y) ) )

def DrawPoints(points):
    points = PointsIntoRange(points)

    


def PointsIntoRange(points):
    
    #[xmin,ymin,xmax,ymax]
    minMaxXY = MinMaxXY(points)
    minX = minMaxXY[0]
    minY = minMaxXY[1]
    maxX = minMaxXY[2]
    maxY = minMaxXY[3]
    mapRatio = (maxY - minY)/(maxX - minX)
    svgHeight = svgWidth * mapRatio

    for tupleNamePointsIndex in range(0, len(points)): #tupleNamePoints = tuple of name and list of points
        for tupleXYIndex in range(0,len(points[tupleNamePointsIndex][1])) : # tupleXYIndex = list of tuples of x and y
            pointX = points[tupleNamePointsIndex][1][tupleXYIndex][0]
            pointY = points[tupleNamePointsIndex][1][tupleXYIndex][1]
            points[tupleNamePointsIndex][1][tupleXYIndex] = (NormalizeRangeX(pointX,minX,maxX,svgWidth), NormalizeRangeY(pointY,minY,maxY,svgHeight))

    return points

def NormalizeRangeX(input, inputMin, inputMax,svgWidth):
    return ((svgWidth)*(input - inputMin))/(inputMax - inputMin)
def NormalizeRangeY(input, inputMin, inputMax,svgHeight):
    return ((svgHeight)*(input - inputMin))/(inputMax - inputMin)

def MinMaxXY(points):
    maxX = points[0][1][0][0]
    maxY = points[0][1][0][1]
    minX = points[0][1][0][0]
    minY = points[0][1][0][1]

    for tupleNamePoints in points: #tupleNamePoints = tuple of name and list of points
        for tupleXY in tupleNamePoints[1]: # tupleXYIndex = list of tuples of x and y
            if tupleXY[0] > maxX:
                maxX = tupleXY[0]
            if tupleXY[1] > maxY:
                maxY = tupleXY[1]
            if tupleXY[0] < minX:
                minX = tupleXY[0]
            if tupleXY[1] < minY:
                minY = tupleXY[1]

    return (minX,minY,maxX,maxY)


