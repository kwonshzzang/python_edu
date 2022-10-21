t = (10, 20, 30)

# 변경 불가이기 때문에 insert, delete가 없음

# t[0] = 100 # 에러

print(t.count(20))  # 리스트에도 사용할 수 있다.
print(len(t))       # 전체사이즈(목합 데이터 타입 다 사용할 수 있음)

print(t.index(30))  # 특정값의 인덱스, 리스트에도 사용할 수 있음

# packing, unpacking
a = 10; b = 20; c = 30
print(a, b, c)

a, b, c = 10, 20, 30
print(a, b, c)

tt = 11, 22, 33 # 자동으로 튜플로 변환(패킹)
print(tt, type(tt))

e, f, g = (100, 200, 300) # 괄호를 없애고 각각의 변수에 할당(언패킹)
print(e, f, g)




