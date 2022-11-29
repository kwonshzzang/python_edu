# 1. 풀이
current_total_amount = 298
current_amount = 50000
PER = 15.79

# 2. 풀이
month_amount = 48584
month = 36
print(f'총금액 = {month_amount * month: ,}')

# 3. 풀이
string = '홀짝홀짝홀짝'
print(string[::2])
print(string[0:1], string[2:3], string[4:5])

# 4. 풀이
phone_number = '010-1111-2222'
print(phone_number.replace('-', ''))

# 5. 풀이
movie_rank = ['탁터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.remove('럭키')
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

# 6. 풀이
import math

radius = 3
height = 10

print(f'원기동의 부피 : {math.pi * radius**2 * height}')
print(f'원뿔의 부피 : {(math.pi * radius**2 * height)/3}')

# 7. 풀이
celsius = 30

print(f'섭씨 30도에 대한 화씨 온도는? {(9*celsius)/5 + 32}도 입니다.')

# 8. 풀이
cm = 30
print(f'10cm의 인치는? {cm * 0.393701}인치 입니다.')

# 9. 풀이
km = 4
print(f'거리 4km의 마일수는 ? {km * 0.62137}마일 입니다.')

# 10. 풀이
a = -3
b = -6
a = -a if a < 0 else a
b = -b if b < 0 else b

print(f'-3과 -6의 절대값의 합은?  {a + b} 입니다.')
print(abs(-3) + abs(-6))

# 11. 풀이
a = ['원숭이', '닭', '개', '돼지', '쥐', '소', '호랑이', '토끼', '용', '뱀', '말', '양']

print(f'띠 : {a[2012 % 12]}')
print(f'띠 : {a[2022 % 12]}')

