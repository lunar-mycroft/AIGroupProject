import csv
from mapNode import MapNode

# list (string nodeName , list( (x,y) ) )
def GetPointsFromCSV(CSVNAME):
    
    #'GroupMapColoring/OhioCounties.csv'
    nodesCSV = list()
    with open(CSVNAME,'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            nodesCSV.append((row['County Name'],row["geometry"]))
    
    nodes = list() 
    id = 0
    for id,nodeCSV in enumerate(nodesCSV):
        newGeometry = nodeCSV[1].replace("<Polygon><outerBoundaryIs><LinearRing><coordinates>",'')
        newGeometry = newGeometry.replace("</coordinates></LinearRing></outerBoundaryIs></Polygon>",'')
        nodeCSV = (nodeCSV[0],newGeometry)

        xyList = nodeCSV[1].split(' ')
        xyTupleList = list()
        for coordinate in xyList:
            split = coordinate.split(',')
            xyTupleList.append((float(split[0]),-float(split[1])))
        newCounty = MapNode(nodeCSV[0],id,xyTupleList,["ff0000","00ff00","0000ff","ff00ff","00ffff"])
        nodes.append(newCounty)

        
    
    #print(len(points))
    #print(points[0])
    #print(points[1])

    return nodes


