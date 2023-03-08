#Area of a triangle
def area_of_triangle(base,height):
    area = (base * height) / 2

    return area

def test_area():
    passed = True

    #First check if we get the same result

    try:
        assert area_of_triangle(20,20) == 200
        print("Test 1 passed!")
    except AssertionError:
        print("Test 1 failed")
        passed = False
    #Check what happens when we put a string instead of integer

    try:
        assert area_of_triangle("20",20) == 200
        print("Test 2 passed!")
    except TypeError:
        print("Test 2 failed!")
        passed = False
    #Check what happens when we put a wrong result

    try:
        assert area_of_triangle(20,20) == 100
        print("Test 3 passed!")
    except AssertionError:
        print("Test 3 failed!")
        passed = False

    if passed:
        print("Everything passed!")
    else:
        print("Not everything passed! Go back and check why!")

test_area()
