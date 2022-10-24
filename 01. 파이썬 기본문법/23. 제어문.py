# if 문, switch 문은 없음

a = 10
if a > 0:
    print('크다')
    print('test')
else:
    print('아니다')

a = -5

if a > 10:
    print('10보다 크다.')
elif a > 5:
    print('5보다 크다.')
elif a == 0:
    print('같다.')
else:
    print('나머지')

print('hello')


# 90~100 'A'
# 80~89  'B'
# 70~79  'C'
# 60~69  'D'
# 나머지 'F'
# 점수가 83점인 경우 학점을 구하시오.

jumsu = 83
if 90 <= jumsu <= 100:
    print('A')
elif 80 <= jumsu < 90:
    print('B')
elif 70 <= jumsu < 80:
    print('C')
elif 60 <= jumsu < 70:
    print('D')
else:
    print('F')

