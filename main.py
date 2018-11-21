from PointsFromCSV import GetPointsFromCSV
from DrawPoints import DrawPoints
from ColorMap import colorMap
from time import time
from itertools import product as cartProd

def main():
    startTime=time()
    print("Starting")
    nodes = GetPointsFromCSV('OhioCounties.csv')
    print("Finished importing in "+str(time()-startTime)+" seconds")

    print("Checking Adjacency")
    startTime=time()
    for node,otherNode in cartProd(nodes,repeat=2):
        node.isAdjacent(otherNode,tolerance=0.001)
    print("Finished checking in "+str(time()-startTime)+" seconds")

    print("Attempting to solve")
    startTime=time()
    res=colorMap(nodes)
    if res is None:
        print("failed!")
        exit()
    print("Finished solving in"+str(time()-startTime)+" seconds")


    print("Drawing points")
    startTime = time()
    DrawPoints(nodes, "home.html")
    print("Finished drawing in " + str(time() - startTime) + " seconds")

main()