from pointUtils import superBoundingBox, boundingBox, boundingBoxSize, boxCenter


# list (string countyname , list( (x,y) ) )

def DrawPoints(counties, path):
    box = superBoundingBox(map(lambda c: boundingBox(c.poly), counties))
    width, height = drawingSize(box,width=1000)
    normalize(counties,box,(width,height))

    with open(path,'w') as file:
        file.write("<svg height = \"" + str(height) + "\" width = \"" + str(width) + "\">\n")

        for county in counties:
            file.write(str(county))

        file.write("</svg>")



def drawingSize(box, width):
    size = boundingBoxSize(box)
    mapRatio = size[1] / size[0]
    height = width * mapRatio
    return (width, height)


def normalize(counties, box, size):
    for county in counties:
        county.normalizePoly(box, size)



