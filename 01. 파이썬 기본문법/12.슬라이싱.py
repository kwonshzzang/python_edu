# 슬라이싱
# [시작인덱스:끝인덱스:증가치]
# 시작인덱스 <= index < 끝인덱스

my = [10, 20, 30, 40, 50]
s = 'abcdefg'

print(my[1:4:1])  # 1<= index < 4 => 1, 2, 3
print(my[1:4:2])  # 1<= index < 4 => 1, 3
print(my[1:4])    # 증가치 기본은 1

print()

print(my[0:4])  # 0 <= index <4 => 0, 1, 2, 3
print(my[:4])   # 시작인덱스 기본은 0
print(my[2:])   # 2 <= index < 끝까지

print()

print(my[:])   # 처음부터 끝까지

print()

print(my[2:4])
print(my[-3:-1])
print(my[-1::-1])

print()

# 맨마지막 데이터를 제외하고 추출하시오
print(my[:-1]) # 0 <= index < -1

# 시작 인덱스가 -이면 반드시 증가치도 -
print(my[-1:-4:-1])
print(my[:-4:-1]) # 증가치가 -이면 시작값은 -1

print()
print(s[1:4])