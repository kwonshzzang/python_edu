def fn(*args): # 가변인자
    print(args)

fn(20, 20, 30)
fn(1, 2, 3, 4, 5)
fn(1.1, 1.2, 1.3)

import math

def circles(*rs): # 튜플
    for r in rs:
        print(math.pi * r**2)

circles(1, 2, 3, 4, 5)

print()

#def fn1(*args, a, b): # error
#def fn1(a, b, * args): # 일반인자 앞으로
def fn1(*args, a=11, b=22): #일반인자 명시
    print(args)
    print(a)
    print(b)

fn1(10, 20, 30, 40, 50)
fn1(10, 20, 30, a=40, b=50)

#def print(*values, sep = ' ', end = '\n')

print(11, 22, 33, sep='-') # ctrl + Q
print('hello', 'korea', end = ' ')
print()

