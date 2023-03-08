import math

def distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2

    dist = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    return dist


point1 = (10,60)
point2 = (100,333)

print(distance(point1,point2))