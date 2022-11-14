# 내장함수(리스트를 만드는 함수)
# range(시작값, 끝값, 증가치)
# 시작값 <= 리스트 < 끝값

r = range(1, 5, 1)  # 1 <= 리스트 <5
print(list(r))

r = range(1, 5, 2) # 1 <= 리스트 < 5
print(list(r))

r = range(1, 5) # 1 <= 리스트 < 5
print(list(r))

r = range(0, 5)
print(list(r))

r = range(5) # range(0, 5)
print(list(r))

print()

for n in range(1, 11):
    if n == 3:
        break
    print(n)

print()

for n in range(1, 11):
    if n == 3:
        continue
    print(n)

print()

# 1 ~10까지 숫자 중 3의 배수를 제외하고 출력
for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n)

print()

for n in range(1, 4):
    for m in range(1, 4):
        print(n, m)