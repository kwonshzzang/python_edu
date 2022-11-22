# def myfilter(data):
#     return [n for n in data if n <=3]
#
# def myfilter1(data):
#     return [n for n in data if n >= 3]
#
# rst = myfilter([1, 2, 3, 4, 5])
# print(rst)
#
# rst = myfilter1([1, 2, 3, 4, 5])
# print(rst)

def fn(n):
    return n >= 3

def fn1(n):
    return n <= 3

def myfilter(data, key):
    return [n for n in data if key(n)]

rst = myfilter([1, 2, 3, 4, 5], fn)
print(rst)

rst = myfilter([1, 2, 3, 4, 5], fn1)
print(rst)

rst = myfilter([1, 2, 3, 4, 5], lambda a: a <= 3)
print(rst)

rst = myfilter([1, 2, 3, 4, 5], lambda a : a >= 3)
print(rst)