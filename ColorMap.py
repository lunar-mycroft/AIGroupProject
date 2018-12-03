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

def colorIndex(color):
    staticColors = list(["ff0000","00ff00","0000ff","ff00ff"])

    for r in range(0,len(staticColors)):
        if color == staticColors[r]:
            return r
    
    return None


def colorNode(nodes, place=0, tb=set(), count=0, reset=False):
    while True:
        if place == len(nodes):
            print("Done coloring nodes")
            print("count = ",count)
            return True
        if place < 0:
            print("Failed. Index went negative")
            print("count = ",count)
            return False
        if count == 88**5:
            print("Exceeded limit")
            print("count = ",count)
            return False
        # Presentation Use Only
        if count > 15150:
            print("break", count)
            return False

        node = nodes[place]
        node.updatePossibleColors()
        colors = list(node.colors)

        # if reset == True:
        #     if len(colors) != 0:
        #         node.color = colors[0]
        #         place = place + 1
        #         #reset = True
        #         continue
        #     else:
        #         place = place -1
        #         reset = False
        #         continue
        # else:
        #     continues = False
        #     for color in colors:
        #         if colorIndex(node.color) < colorIndex(color):
        #             continues = True
        #             node.color = color
        #             place = place + 1
        #             reset = True
        #             break
        #     if continues == True:
        #         continue
        #     place = place - 1
        #     node.color = None
        #     reset = False
        #     continue


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
        #print(count, place, colors, node.color)#, place, colors)
        #print(count)
        if reset:
            if len(colors) == 1:
                node.color = None
                place = place-1
                continue
                #colorNode(nodes, place-1, tb, count, True)
            elif (place, 2) in tb or (place, 3) in tb or (place, 4) in tb:
                if len(colors) >= 3 and (place, 2) in tb:
                    tb.remove((place, 2))
                    tb.add((place, 3))
                    node.setColor(colors[2])
                    place = place + 1
                    reset = False
                    continue
                    #colorNode(nodes, place+1, tb, count)
                elif len(colors) == 4 and (place, 3) in tb:
                    tb.remove((place, 3))
                    tb.add((place, 4))
                    node.setColor(colors[3])
                    place = place + 1
                    reset = False
                    continue
                    #colorNode(nodes, place+1, tb, count)
                else:
                    node.color = None
                    place = place - 1
                    reset = True
                    continue
                    #colorNode(nodes, place-1, tb, count, True)
            else:
                node.setColor(colors[1])
                tb.add((place, 2))
                place = place + 1
                reset = False
                continue
                #colorNode(nodes, place+1, tb, count, False)

        elif len(colors) != 0:
            node.setColor(colors[0])
            place = place + 1
            reset = False
            continue
            #colorNode(nodes, place+1, tb, count)
        else:
            node.color = None
            place = place - 1
            reset = True
            continue
            #colorNode(nodes, place-1, tb, count, True)
