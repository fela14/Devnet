from math import pi

def area_of_circle(r):
    if r < 0:
        raise ValueError
    return pi * (r ** 2)

print(area_of_circle(1))
