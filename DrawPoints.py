svgWidth = 200
svgHeight = 200
# list (string countyname , list( (x,y) ) )

def DrawPoints(counties):
    counties = PointsIntoRange(counties)

    




def PointsIntoRange(counties):
    
    #[xmin,ymin,xmax,ymax]
    minMaxXY = MinMaxXY(counties)
    minX = minMaxXY[0]
    minY = minMaxXY[1]
    maxX = minMaxXY[2]
    maxY = minMaxXY[3]
    mapRatio = (maxY - minY)/(maxX - minX)
    svgHeight = svgWidth * mapRatio

    for countyIndex in range(0, len(counties)): #tupleNamePoints = tuple of name and list of points
        for tupleXYIndex in range(0,len(counties[countyIndex].points)) : # tupleXYIndex = list of tuples of x and y
            pointX = counties[countyIndex].points[tupleXYIndex][0]
            pointY = counties[countyIndex].points[tupleXYIndex][1]
            counties[countyIndex].points[tupleXYIndex] = (NormalizeRangeX(pointX,minX,maxX,svgWidth), NormalizeRangeY(pointY,minY,maxY,svgHeight))

    return counties

def NormalizeRangeX(input, inputMin, inputMax,svgWidth):
    return ((svgWidth)*(input - inputMin))/(inputMax - inputMin)
def NormalizeRangeY(input, inputMin, inputMax,svgHeight):
    return ((svgHeight)*(input - inputMin))/(inputMax - inputMin)

def MinMaxXY(counties):
    maxX = counties[0].points[0][0]
    maxY = counties[0].points[0][1]
    minX = counties[0].points[0][0]
    minY = counties[0].points[0][1]

    for county in counties: #tupleNamePoints = tuple of name and list of points
        for tupleXY in county.points: # tupleXYIndex = list of tuples of x and y
            if tupleXY[0] > maxX:
                maxX = tupleXY[0]
            if tupleXY[1] > maxY:
                maxY = tupleXY[1]
            if tupleXY[0] < minX:
                minX = tupleXY[0]
            if tupleXY[1] < minY:
                minY = tupleXY[1]

    return (minX,minY,maxX,maxY)


