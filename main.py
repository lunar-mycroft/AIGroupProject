import PointsFromCSV
import DrawPoints
from time import time

def main():
    nodes = PointsFromCSV.GetPointsFromCSV('OhioCounties.csv')
    startTime=time()
    oldTime=time()
    for node in nodes:
        for otherNode in nodes:
            if node.isAdjacent(otherNode,tolerance=0.0001):
                anyTrue=True
        t=time()
        print(t-oldTime)
        oldTime=t
    print(time()-startTime)

    DrawPoints.DrawPoints(nodes, "home.html")


main()