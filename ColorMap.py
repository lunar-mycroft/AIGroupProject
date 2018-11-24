from copy import deepcopy as clone
from random import sample

def colorMap(nodes):
    nodes=sorted(nodes)
    for node in nodes:
        if node.color is not None:
            break
        colors=sample(node.colors,k=len(node.colors))
        node.updatePossibleColors()
        for color in colors:
            node.setColor(color)
            res=colorMap(clone(nodes))
            if res is not None:
                return res
            node.color=None
    return None

def colorNodes(nodes):
    for node in nodes:
        if node.color is not None:
            break
        #colors = sample(node.colors, k=len(node.colors))
        node.updatePossibleColors()
        colors = list(node.colors)
        #print(colors)
        if len(colors) is not 0:
            node.setColor(colors[0])
        else:
            return False

    return True