# 전역변수: 함수밖에 선언된 변수
# 지역변수: 함수내에 선언된 변수

# __name__ = __main__
# __doc__ = None
# 파이썬이 만들어 전역변수

g = 10

def fn():
    g = 100
    print(locals()) # 지역변수 보기

fn()

print('g=', g)
print(__file__)
print(globals()) # 전역변수 보기
print(id(g)) # 변수 주소 보기
