# 연산자 우선순위로서의 괄호 ()
# 튜플에서의 괄호 ( , )
# 튜플의 예

# (10, 20, 30)

rst = 10 + 2 * 3
print(rst)

rst = (10 + 2) * 3
print(rst)

t = (100)
print(t, type(t))

t = (100,)
print(t, type(t))

# 대입연산자

a = 5
# a = a + 2
# a += 2
# a -= 2
# a **= 2

a += 1 # 다른 언어 a++ => 파이썬은 지원하지 않음
print(a)