import csv
from mapNode import MapNode

# list (string countyname , list( (x,y) ) )
def GetPointsFromCSV(CSVNAME):
    
    #'GroupMapColoring/OhioCounties.csv'
    countiesCSV = list()
    with open(CSVNAME,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            countiesCSV.append((row['County Name'],row["geometry"]))
    
    counties = list() 
    id = 0
    for countyCSV in countiesCSV:
        newGeometry = countyCSV[1].replace("<Polygon><outerBoundaryIs><LinearRing><coordinates>",'')
        newGeometry = newGeometry.replace("</coordinates></LinearRing></outerBoundaryIs></Polygon>",'')
        countyCSV = (countyCSV[0],newGeometry)

        xyList = countyCSV[1].split(' ')
        xyTupleList = list()
        for coordinate in xyList:
            split = coordinate.split(',')
            xyTupleList.append((float(split[0]),-float(split[1])))
        newCounty = MapNode(countyCSV[0],id,xyTupleList,['empty','empty'])
        id = id+1
        counties.append(newCounty)

        
    
    #print(len(points))
    #print(points[0])
    #print(points[1])

    return counties


