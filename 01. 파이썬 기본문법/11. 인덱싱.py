# 순서있음 : str, list, tuple
# 인덱싱 : [인덱스 넘버]
# 0, 1, 2, .......
# -1, -2, -3, ......


my = [10, 20, 30, 40, 50]
s = 'abcdef'
t = (10, 20, 30, 40, 50)

a = {10, 20, 30, 40, 50}
d = {'aa':10, 'bb':20, 'cc':30}


print(my[0])
print(my[2])
print(my[4])
print(my[-1])
print(my[-3])

print()

print(s[0])
print(s[-1])

print()

print(t[0])
print(t[-1])

print()

print(t[0])
print(t[-1])

print()

# print(a[0])   # 에러 set 순서가 없음
print(d['aa'])  # d[키]