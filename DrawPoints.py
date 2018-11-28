from pointUtils import superBoundingBox, boundingBox, boundingBoxSize, boxCenter
from svgStrings import line


def DrawPoints(counties, path,debugLines=False):
    box = superBoundingBox(map(lambda c: boundingBox(c.poly), counties))
    width, height = drawingSize(box,width=5000)
    normalize(counties,box,(width,height))

    with open(path,'w') as file:
        file.write("<svg height = \"" + str(height) + "\" width = \"" + str(width) + "\">\n")
        for county in counties:
            file.write(str(county))

        if debugLines:
            for county in counties:
                c1=county.center(True)
                for neighbor in county.neighbors:
                    c2=neighbor.center(True)
                    file.write(line((c1[0],c1[1],c2[0],c2[1]),"stroke:rgb(255,0,0);stroke-width:2"))

        file.write("</svg>")

def drawingSize(box, width):
    size = boundingBoxSize(box)
    mapRatio = size[1] / size[0]
    height = width * mapRatio
    return (width, height)

def normalize(counties, box, size):
    for county in counties:
        county.normalizePoly(box, size)



