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

def colorNode(nodes, place=0, tb=set(), count=1, reset=False):
    if place == len(nodes):
        print("Done coloring nodes")
        return True
    if place < 0:
        print("Failed. Index went negative")
        return False
    # if count == 2800:
    #     print("Exceeded limit")
    #     return False

    node = nodes[place]
    node.updatePossibleColors()
    colors = list(node.colors)
    remove = set()
    for index, n in tb:
        if place < index:
            remove.add((index, n))
            if len(tb) == 1 and n == 4:
                print("Failed, nothing in tb")
                return False
    for index, n in remove:
        tb.remove((index, n))
    count += 1
    print(count, place, colors)
    print(tb)
    if reset:
        if len(colors) == 1:
            node.color = None
            colorNode(nodes, place-1, tb, count, True)
        elif (place, 2) in tb or (place, 3) in tb or (place, 4) in tb:
            if len(colors) == 3 and (place, 2) in tb:
                tb.remove((place, 2))
                tb.add((place, 3))
                node.setColor(colors[2])
                colorNode(nodes, place+1, tb, count)
            elif len(colors) == 4 and (place, 3) in tb:
                tb.remove((place, 3))
                tb.add((place, 4))
                node.setColor(colors[3])
                colorNode(nodes, place+1, tb, count)
            else:
                node.color = None
                colorNode(nodes, place-1, tb, count, True)
        else:
            node.setColor(colors[1])
            tb.add((place, 2))
            colorNode(nodes, place+1, tb, count, False)

    elif node.color is not None:
        colorNode(nodes, place+1, tb, count)

    elif len(colors) != 0:
        node.setColor(colors[0])
        colorNode(nodes, place+1, tb, count)
    else:
        colorNode(nodes, place-1, tb, count, True)
