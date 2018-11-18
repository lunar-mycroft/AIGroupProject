class MapNode:
    def __init__(self,polygons,colors): #Constructor.  svg is a string containing the svg info for the map node being created
        self.neighbors=[]
        self.color=None
        self.poly=polygons
        self.colors=colors


    def connectTo(self,other):
        if not isinstance(other,MapNode):
            return False

        if not self in other.neighbors:
            other.neighbors.append(self)
        if not other in self.neighbors:
            self.neighbors.append(other)

        return True

    def getLines(self):
        res=[]
        for i, vert in enumerate(self.poly):
            res.append((self.poly[i-1],vert))
        return res

    def isAdjacent(self,other,tolerance=0.001):
        if not isinstance(other,MapNode):
            return False

        if other in self.neighbors:
            return True

        #todo: add a check for already confirmed false-connections?

        for line in self.getLines():
            steepSlope=abs(line[0][0]-line[1][0])>abs(line[0][1]-line[1][1])
            m1 = (line[0][1]-line[1][1])/(line[0][0]-line[1][0]) if steepSlope else (line[0][0]-line[1][0]) / (line[0][1]-line[1][1])
            b1 = line[0][1]-m1*line[0][0]
            for otherLine in other.getLines():
                #do pretty much the same thing to get 


    def __str__(self): #This should return the SVG of the mape node, except not colored according to color.
        return "placeholder"

    def possibleColors(self):#returns a list of the possible colors the node could take out of colorOptions
        return [] #placeholder

    def numConnections(self):