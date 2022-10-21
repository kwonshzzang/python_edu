d = {'aa':10, 'bb':20, 'cc':30}

d['aa'] = 100 # 수정
print(d)

d['dd'] = 200 # 추가
print(d)

# 순서가 없어서 중간 추가는 없음

d.pop('bb') # 키로 삭제
print(d)

print(d.keys())
print(d.values())
print(d.items())

print(d.get('aa', 1000))
print(d.get('ff', 1000)) # 없으면 default값 리턴
print(d.get('ff')) # 없으면 None