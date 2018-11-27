from PointsFromCSV import GetPointsFromCSV
from DrawPoints import DrawPoints
from ColorMap import colorMap, colorNodes, colorNode
from time import time
from itertools import product as cartProd
from Order import Next
import pickle
import sys

def main():
    startTime=time()
    print("Starting")
    nodes = GetPointsFromCSV('OhioCounties.csv')
    print("Finished importing in "+str(time()-startTime)+" seconds")

    sys.setrecursionlimit(10000)

    print("Checking Adjacency")
    startTime=time()
    for node,otherNode in cartProd(nodes,repeat=2):
        node.isAdjacent(otherNode,tolerance=0.001)
    print("Finished checking in "+str(time()-startTime)+" seconds")

    pickle.dump(nodes, open("test.p", "wb"))
    # nodes = pickle.load(open("test.p", "rb"))
    
    path = list()
    Next(nodes[0], path, 2, len(nodes))

    # for step in path:
    # 	print(step.id, step.numConnections())
    # 	# for neighbor in step.neighbors:
    # 	# 	print(neighbor.id)
    # print("Path Length:",len(path))

    # print("Attempting to solve")
    # startTime=time()
    #res=colorMap(path)
    # if res is None:
    #     print("failed!")
    #     exit()
    # print("Finished solving in"+str(time()-startTime)+" seconds")

    # index = 0
    res = colorNode(path)

    print("Drawing points")
    startTime = time()
    DrawPoints(nodes, "home.html")
    print("Finished drawing in " + str(time() - startTime) + " seconds")

main()