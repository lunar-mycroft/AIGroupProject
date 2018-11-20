from pointUtils import boundingCircle, pointDistance, normalizePoint

class MapNode:
    def __init__(self,inName,inID,polygons,colors): #Constructor.
        self.name = inName
        self.id = inID
        self.neighbors=set({})
        self.notNeighbors=set({})
        self.color=None
        self.poly=polygons
        self.colors=set(colors)

    def connectTo(self, other): #Forces a connection.  Don't use if you don't have to.
        if not isinstance(other, MapNode):
            return False

        if self in other.notNeighbors:
            other.notNeighbors.remove(self)
        if other in self.notNeighbors:
            self.notNeighbors.remove(other)

        if not self in other.neighbors:
            other.neighbors.add(self)
        if not other in self.neighbors:
            self.neighbors.add(other)

        return True

    def disconnectFrom(self,other):
        if not isinstance(other,MapNode):
            return False
        if not self.isAdjacent(other,supressDeepCheck=True):
            return True

        if self in other.neighbors:
            other.neighbors.remove(self)
        if other in self.neighbors:
            self.neighbors.remove(other)

        if not self in other.notNeighbors:
            other.notNeighbors.add(self)
        if not other in self.notNeighbors:
            self.notNeighbors.remove(other)
        return True

    def getLines(self):
        res=[]
        for i, vert in enumerate(self.poly):
            res.append((self.poly[i-1],vert))
        return res

    def isAdjacent(self,other,tolerance=0.001,supressDeepCheck=False):
        if other==self:
            return False
        if not isinstance(other,MapNode):
            return False
        if other in self.neighbors:
            return True

        if other in self.notNeighbors:
            return False

        if supressDeepCheck:
            return False

        circle=boundingCircle(self.poly)
        otherCircle=boundingCircle(other.poly)
        maxDistance=(circle[1]+otherCircle[1])+2*tolerance

        if pointDistance(circle[0],otherCircle[0])>maxDistance:
            return False

        lines=self.getLines()
        otherLines=other.getLines()

        for line in lines:
            steepSlope=abs(line[0][0]-line[1][0])<abs(line[0][1]-line[1][1])
            deltaX=line[0][0]-line[1][0]
            deltaY=line[0][1]-line[1][1]
            m1 = deltaX/deltaY if steepSlope else deltaY/deltaX
            b1 = line[0][0]-m1*line[0][1] if steepSlope else line[0][1]-m1*line[0][0]
            for otherLine in otherLines():
                if abs(otherLine[0][0]-otherLine[1][0])<abs(otherLine[0][1]-otherLine[1][1])!=steepSlope:
                    continue
                deltaX=otherLine[0][0]-otherLine[1][0]
                deltaY=otherLine[0][1]-otherLine[1][1]
                m2 = deltaX/deltaY if steepSlope else deltaY/deltaX
                b2 = otherLine[0][1]-m2*otherLine[0][1]

                if abs(m1-m2)>tolerance or abs(b1-b2)>tolerance:
                    continue
                if steepSlope:
                    if line[0][1] > otherLine[0][1] and line[1][1] > otherLine[0][1] and line[1][1] > otherLine[1][1]:
                        continue
                    if line[0][1] < otherLine[0][1] and line[1][1] < otherLine[0][1] and line[1][1] < otherLine[1][1]:
                        continue
                else:
                    if line[0][0] > otherLine[0][0] and line[1][0] > otherLine[0][0] and line[1][0] > otherLine[1][0]:
                        continue
                    if line[0][0] < otherLine[0][0] and line[1][0] < otherLine[0][0] and line[1][0] < otherLine[1][0]:
                        continue
                self.connectTo(other)
                return True

        self.notNeighbors.add(other)
        return False

    def updatePossibleColors(self):
        for neighbor in self.neighbors:
            if neighbor.color!=None:
                if neighbor.color in self.colors:
                    self.colors.remove(neighbor.color)

    def setColor(self,color):
        if not color in self.colors: #If we _can_ avoid calling updatePossibleColors, do so.
            return False
        self.updatePossibleColors()
        if not color in self.colors:
            return False

        self.colors=set({color})
        self.color=color
        return True

    def numConnections(self,possibleNeighbors=None):
        if possibleNeighbors is not None:
            for node in possibleNeighbors:
                self.isAdjacent(node)

        return len(self.neighbors)

    def numValues(self):
        if self.color is not None:
            if len(self.colors)>1:
                self.colors=set({self.color})
            return 1
        return len(self.colors)

    def normalizePoly(self,oldBox,newSize):
        self.poly=list(map(lambda p:normalizePoint(p,oldBox,newSize),self.poly))

    def __str__(self): #This should return the SVG of the mape node, except not colored according to color.
        res="<polygon id=\"" + str(self.id) + "\" " + "points=\""
        for point in self.poly:
            res+=str(point[0])+','+str(point[1])+' '
        return res+"\" style=\"fill:#"+(str(self.color) if self.color is not None else "aaaaaa")+";stroke:#ffffff;stroke-width:1\"/>"