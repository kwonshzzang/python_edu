# 리턴값이 여러개 일 수 있음(튜플)

def fn():
    return 10, 20

rst = fn()
print(rst)

a, b = fn()
print(a, b)

import math

def shape(r, w, h):
    return math.pi * r**2, w * h

print(shape(3, 10, 20))

def myfn(a = 10, b = 20): # Default Argument
    print(a, b)

myfn()
myfn(100)
myfn(100, 200)
myfn(b=10000) # 명시적 호출