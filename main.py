import PointsFromCSV
import DrawPoints
from time import time
from itertools import product as cartProd

def main():
    nodes = PointsFromCSV.GetPointsFromCSV('OhioCounties.csv')
    startTime=time()
    for node,otherNode in cartProd(nodes,repeat=2):
        node.isAdjacent(otherNode,tolerance=0.001)

    print(time()-startTime)

    DrawPoints.DrawPoints(nodes, "home.html")


main()