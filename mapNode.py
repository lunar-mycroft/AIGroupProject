from pointUtils import boundingCircle, pointDistance, normalizePoint, linesAdjacent, lines, perpLine,linesCross
from svgStrings import dot as svgDot, polygon as svgPolygon, line as svgLine
from itertools import product as cartProd

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

    def isAdjacent(self,other,tolerance=0.01,supressDeepCheck=False):
        if other is self or not isinstance(other,MapNode):
            return False
        if other in self.neighbors:
            return True

        if other in self.notNeighbors or (self in other.notNeighbors) or supressDeepCheck:
            return False

        circle=boundingCircle(self.poly)
        otherCircle=boundingCircle(other.poly)
        maxDistance=(circle[1]+otherCircle[1])*(1+2*tolerance)

        normLen=circle[1]*tolerance

        if pointDistance(circle[0],otherCircle[0])>maxDistance:
            return False

        for line in lines(self.poly):
            normals=[perpLine(line,normLen,0),perpLine(line,-normLen,0),
                     perpLine(line, normLen, 1), perpLine(line, -normLen, 1)]
            for norm,otherLine in cartProd(normals,lines(other.poly)):
                if linesCross(norm,otherLine):
                    self.connectTo(other)
                    return True

        #for line,otherLine in cartProd(lines(self.poly),lines(other.poly)):
        #    if linesAdjacent(line,otherLine,tolerance,tolerance*(circle[1]+otherCircle[1])):
        #        self.connectTo(other)
        #        return True

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

    def boundingCircle(self):
        try:
            return self._boundingCircle_
        except:
            self._boundingCircle_=boundingCircle(self.poly)
            return self._boundingCircle_

    def center(self):
        return self.boundingCircle()[0]

    def __str__(self): #This should return the SVG of the mape node, except not colored according to color.
        res= svgPolygon(self.id,self.poly,"fill:#"+("aaaaaa" if self.color is None else self.color)+";stroke:#ffffff;stroke-width:1")+"\n"#+svgDot(self.boundingCircle()[0],"ff0000")+"\n"
        return res

    def __gt__(self, other):
        return self.id>other.id #Placeholder