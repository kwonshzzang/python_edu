my = [10, 20, 30]

my.append(40)     # 맨 마지막 추가
print(my)

my.insert(1, 100)  # 중간에 추가
print(my)

my[0] = 11 # 수정
print(my)

my.remove(20) # 값을 통한 삭제
print(my)

my.pop(0) # 인덱스를 통한 삭제
print(my)

my.clear() # 모두 삭제
print(my)