class MapNode:
    def __init__(self,svg): #Constructor.  svg is a string containing the svg info for the map node being created
        self.neighbors=[]
        self.color=None
        self.image=svg


    def connectTo(self,other):
        if not isinstance(other,MapNode):
            return False

        if not self in other.neighbors:
            other.neighbors.append(self)
        if not other in self.neighbors:
            self.neighbors.append(other)

        return True

    def __str__(self): #This should return the SVG of the mape node, except not colored according to color.
        return "placeholder"

    def possibleColors(self,colorOptions):#returns a list of the possible colors the node could take out of colorOptions
        return [] #placeholder

