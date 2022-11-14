# 다른언어 for(초기화;판단;증가치)
# 파이썬 for 변수 in 복합데이터타입:
for n in [11, 22, 33]:
    print('n =', n)

print()

for c in 'abc':
    print('c =', c)

print()

for t in (10, 20, 30):
    print('t =', t)

print()

d = {'aa':10, 'bb':20, 'cc':30}
for k in d: # d.keys()와 같다.
    print('k =', k)

print()

for v in d.values():
    print('v =', v)

print()

for k, v in d.items():
    print('k =', k, ', v =', v)