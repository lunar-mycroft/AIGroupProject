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