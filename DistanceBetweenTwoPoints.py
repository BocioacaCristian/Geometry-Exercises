import math

def distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2

    dist = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    return dist



#Testing the code

def test_distance():
    assert distance((10,20),(100,333)) == 325.68236059080635
    assert distance((60, 100), (100, 97)) == 40.11234224026316


if __name__ == "__main__":
    test_distance()
    print("Everything passed")