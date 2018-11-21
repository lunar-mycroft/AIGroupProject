def polygon(idNum,points,style):
    res = "<polygon id=\"" + str(idNum) + "\" " + "points=\""
    for point in points:
        res += str(point[0]) + ',' + str(point[1]) + ' '
    return res+ "\" style=\"" + style +"\"/>"

def dot(point,color):
    return "<circle cx=\"" + str(point[0]) + "\" cy=\"" + str(point[1]) + "\" r=\"10\" fill=\"#"+color+"\" />"

def line(line,style):
    return "<line x1=\""+str(line[0])+"\" y1=\""+str(line[1])+"\" x2=\""+str(line[2])+"\" y2=\""+str(line[3])+"\" style=\""+style+"\" />"
