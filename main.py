#Radius of a circle
import math
def area_circle(radius):
    area = math.pi * (radius ** 2)
    format_area = "{:.2f}".format(area)
    float_area = float(format_area)
    return float_area

print(area_circle(5))
print(area_circle(10))

def test_area_of_circle():
    assert (area_circle(5)) == 78.54
    assert (area_circle(10)) == 314.16

test_area_of_circle()

if __name__ == "__main__":
    test_area_of_circle()
    print("Everything passed")