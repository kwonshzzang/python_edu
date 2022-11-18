def hap(a, b):
    return a + b

def gop(a , b):
    return a * b

import math

def make_circle(radius):
    return math.pi * radius**2

def absHap(a, b):
    a = -a if a < 0 else a
    b = -b if b < 0 else b
    return a + b