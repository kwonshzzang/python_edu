# 문자열 연산:
# + (문자열 연결)
# * (문자열 반복)
# % (문자열 포맷)

s = 'hello'
print(s + ' korea')

print(s*3)

a = 10
b = 3.141592
c = 'python'

s1 = 'a=%5d b=%.2f c=%10s' % (a, b, c)
print(s1)

s2 = f'a={a:5} b={b:.2f} c={c:>10}' # python 3.5이상
print(s2)