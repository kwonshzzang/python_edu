# type(변수명)  출력결과 변수의 형을 출력

a ='100'
print(a, type(a))

a = int(a) # 정수형 타입 형변환
print(a, type(a))

b = '3.14'
b = float(b)
print(b, type(b))

c = 200
c = str(c)
print(c, type(c))

d = (10, 20, 30)
d = list(d)
print(d, type(d))

e = {'aa':10, 'bb':20}
e = list(e)
print(e, type(e))

f = [100, 200, 300]
f = tuple(f)
print(f, type(f))