#from copy import deepcopy as clone
from pickle import loads,dumps
from random import sample

def clone(thing):
    return loads(dumps(thing))

def colorMap(nodes,depth=0):
    nodes=sorted(nodes,reverse=True)
    for node in nodes:
        if node.color is not None:
            print("ran out of uncolored nodes",depth)
            break

        node.updatePossibleColors()
        colors=sample(node.colors,k=len(node.colors))
        if len(colors)==0:
            continue
        print(colors)
        for color in colors:
            print("Attempting to color "+node.name+" "+color)
            node.setColor(color)
            res=colorMap(clone(nodes),depth+1)
            if res is not None:
                return True,res
            node.color=None
    return None, nodes
