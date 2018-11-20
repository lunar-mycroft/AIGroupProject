svgWidth = 1000

# list (string countyname , list( (x,y) ) )

def DrawPoints(counties,htmlPath):
    htmlPath = open(htmlPath,'w')
    WidthHeightTuple = __PointsIntoRange__(counties)
    
    htmlPath.write("<svg height = \""+ str(WidthHeightTuple[1]) +"\" width = \"" + str(WidthHeightTuple[0]) + "\">\n")

    for county in counties:
        htmlPath.write("<polygon points=\"")
        for point in county.poly:
            htmlPath.write(str(point[0]) + ',' + str(point[1]) + ' ')
        htmlPath.write("\" style=\"stroke:purple;stroke-width:1\" />\n")

    htmlPath.write("</svg>")
    htmlPath.close()






def __PointsIntoRange__(counties):
    
    #[xmin,ymin,xmax,ymax]
    minMaxXY = MinMaxXY(counties)
    minX = minMaxXY[0]
    minY = minMaxXY[1]
    maxX = minMaxXY[2]
    maxY = minMaxXY[3]
    mapRatio = (maxY - minY)/(maxX - minX)
    svgHeight = svgWidth * mapRatio

    for countyIndex in range(0, len(counties)): #tupleNamePoints = tuple of name and list of points
        for tupleXYIndex in range(0,len(counties[countyIndex].poly)) : # tupleXYIndex = list of tuples of x and y
            pointX = counties[countyIndex].poly[tupleXYIndex][0]
            pointY = counties[countyIndex].poly[tupleXYIndex][1]
            counties[countyIndex].poly[tupleXYIndex] = (NormalizeRangeX(pointX,minX,maxX,svgWidth), NormalizeRangeY(pointY,minY,maxY,svgHeight))

    return (svgWidth,svgHeight)

def NormalizeRangeX(input, inputMin, inputMax,svgWidth):
    return ((svgWidth)*(input - inputMin))/(inputMax - inputMin)
def NormalizeRangeY(input, inputMin, inputMax,svgHeight):
    return ((svgHeight)*(input - inputMin))/(inputMax - inputMin)

def MinMaxXY(counties):
    maxX = counties[0].poly[0][0]
    maxY = counties[0].poly[0][1]
    minX = counties[0].poly[0][0]
    minY = counties[0].poly[0][1]

    for county in counties: #tupleNamePoints = tuple of name and list of poly
        for tupleXY in county.poly: # tupleXYIndex = list of tuples of x and y
            if tupleXY[0] > maxX:
                maxX = tupleXY[0]
            if tupleXY[1] > maxY:
                maxY = tupleXY[1]
            if tupleXY[0] < minX:
                minX = tupleXY[0]
            if tupleXY[1] < minY:
                minY = tupleXY[1]

    return (minX,minY,maxX,maxY)


