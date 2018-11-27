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
    for i, node in enumerate(nodes):
        if node.color is not None:
            break
        node.updatePossibleColors()
        colors = list(node.colors)
        print(colors)
        if len(colors) is not 0:
            node.setColor(colors[0])
        else:

            return False

    return True

def colorNode(nodes, place=0, tb=set(), reset=False):
    if place == len(nodes):
        print("Done coloring nodes")
        return True
    if place < 0:
        print("Failed. Index went negative")
        return False

    node = nodes[place]
    node.updatePossibleColors()
    colors = list(node.colors)
    print(place, node.id, colors)
    print(tb)
    if reset:
        if len(colors) == 1:
            node.color = None
            colorNode(nodes, place-1, tb, True)
        elif node.id in tb:
            colorNode(nodes, place-1, tb, True)
        else:
            node.setColor(colors[1])
            tb.add(node.id)
            colorNode(nodes, place+1, tb)

    elif node.color is not None:
        colorNode(nodes, place+1, tb)

    elif len(colors) != 0:
        node.setColor(colors[0])
        colorNode(nodes, place+1, tb)
    else:
        colorNode(nodes, place-1, tb, True)
