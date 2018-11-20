import csv


# list (string county name , list( (x,y) ) )
def GetPointsFromCSV(CSVNAME):
    points = list()
    #'GroupMapColoring/OhioCounties.csv'
    counties = list()
    with open(CSVNAME,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            counties.append((row['County Name'],row["geometry"]))
    
    
    for index in range(0,len(counties)):
        newGeometry = counties[index][1].replace("<Polygon><outerBoundaryIs><LinearRing><coordinates>",'')
        newGeometry = newGeometry.replace("</coordinates></LinearRing></outerBoundaryIs></Polygon>",'')
        counties[index] = (counties[index][0],newGeometry)
        
    for county in counties:
        xyList = county[1].split(' ')
        xyTupleList = list()
        for coordinate in xyList:
            split = coordinate.split(',')
            xyTupleList.append((float(split[0]),float(split[1])))
        points.append((county[0],xyTupleList))
    
    print(len(points))
    print(points[0])
    #print(points[1])

    return points


