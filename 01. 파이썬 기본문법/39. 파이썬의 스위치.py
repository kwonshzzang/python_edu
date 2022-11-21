def fn1():
    print('fn1 call')

def fn2():
    print('fn2 call')

def defaultFn():
    print('나머지')

dd = {0:fn1, 1:fn2}

# while True:
#     n = int(input('선택'))
#     if n == 3:
#         break
#     dd[n]()

dd.get(2, defaultFn())