import math

def get_circle_area(radius):
    return math.pi * radius**2

def get_cylinder_volume(radius, height):
    return round(math.pi * radius **2 * height, 4)

def get_circular_con_volume(radius, height):
    return round((math.pi * radius**2 * height)/3, 4)