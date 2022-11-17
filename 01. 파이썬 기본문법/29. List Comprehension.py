my = [10, 20, 30, 40, 50]

# make list
com = [n for n in my]
print(com)

com = [n*2 for n in range(1, 6)]
print(com)

# 연습문제
salary = [1000, 2000, 3000, 4000, 500]

# 세금 3.3%를 제외한 실수령액 리스트를 구하시오.
real_amount = [m - m*0.033 for m in salary]
print(real_amount)

com = [n for n in range(1, 6) if n % 2 == 0]
print(com)

# 연습문제
names = ['홍길동', '이순신', '이황', '정도전']
# 에서 '이' 글자가 있는 이름으로 구성된 리스트를 만드시오.

names = [name for name in names if '이' in name]
print(names)
