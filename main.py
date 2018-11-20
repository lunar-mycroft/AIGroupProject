import PointsFromCSV
import DrawPoints

def main():
    points = PointsFromCSV.GetPointsFromCSV('OhioCounties.csv')
    DrawPoints.DrawPoints(points)



main()