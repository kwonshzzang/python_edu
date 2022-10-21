# 1. 중복데이터 자동 제거
# 2. 순서없음(인덱싱, 슬라이싱) 안됨
# 3. 집합연산

s = {10, 20, 30, 40, 40}

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print(s)

s.remove(20) # 삭제
print(s)

print(s1 & s2) # 교집합
print(s1 | s2) # 합집합
print(s1 -s2)  # 차집합
print(s1 ^ s2) # 대상 차집합

print(s1.intersection(s2))
print(s1.union(s2))