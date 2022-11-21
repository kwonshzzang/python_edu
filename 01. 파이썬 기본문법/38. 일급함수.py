# 일급함수: 함수할당, 리턴, 인자로 사용할 수 있는 함수

def fn():
    print('fn call')

def tfn(aa):
    print(id(aa))
    aa()

def rfn():
    return fn

# 함수할당
# afn = fn
# print(id(afn), id(fn))
# fn()
# afn()

# 함수를 인자로
# print(id(fn))
# tfn(fn)

# 함수를 리턴값으로
rst= rfn()
rst()
