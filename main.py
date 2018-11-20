import PointsFromCSV
import DrawPoints

def main():
    #counties = list of mapNodes with empty colors
    nodes = PointsFromCSV.GetPointsFromCSV('OhioCounties.csv')
    

    
    DrawPoints.DrawPoints(nodes, "home.html")



main()