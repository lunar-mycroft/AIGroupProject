import PointsFromCSV
import DrawPoints

def main():
    #counties = list of mapNodes with empty colors
    counties = PointsFromCSV.GetPointsFromCSV('OhioCounties.csv')
    DrawPoints.PointsIntoRange(counties)
    DrawPoints.DrawPoints(counties)



main()