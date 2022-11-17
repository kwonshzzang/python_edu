def fn():
    print('hello')
    print('korea')

def hap(a, b):
    return a + b

fn()
fn()
fn()

print(hap(10, 20))
print(hap(100, 200))

# 연습문제

# 반지름을 인자로 받아 원의 면적을 구하는 함수를 만드시오.
import math

def make_circle_area(radius):
    return math.pi*radius**2

print(make_circle_area(3))

# cm을 인자로 받아 인치를 구하는 함수를 만드시오.
def get_inch(cm):
    return round(cm * 0.393701, 2)

print(get_inch(10))

# km를 인자로 받아 마일을 구하는 함수를 만드시오.
def get_mile(km):
    return round(km * 0.621371, 2)

print(get_mile(10))

# 함수를 인자로 받아 70점 이상이면 합격, 아니면 불합격을 반환하는 함수를 만드시오.
def decision_pass_or_fail(mark):
    return '합격' if mark >= 70 else '불합격'

print(decision_pass_or_fail(69))
print(decision_pass_or_fail(70))

# 2개의 숫자를 인자로 받아 절대값의 합을 구하는 함수를 만드시오.
def abs_hap(a, b):
    a = -a if a < 0 else a
    b = -b if b < 0 else b
    return a + b

print(abs_hap(-3, -9))
print(abs_hap(-7, 7))