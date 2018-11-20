import PointsFromCSV
import DrawPoints

def main():
    counties = PointsFromCSV.GetPointsFromCSV('OhioCounties.csv')
    DrawPoints.DrawPoints(counties)



main()