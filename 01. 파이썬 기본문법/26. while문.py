# while, for, do~while(x)

a = 1
while a<= 5:
    if a == 3:
        print('3임')
        break # 반복문 강제 탈출

    print('a=', a)
    a += 1
else:
    print('else......')
print('hello')

# 1~10까지 숫자 중 짝수만 출력하시오.

print()
a = 1
while a <= 10:
    if a % 2 == 0:
        print('a=', a)
    a += 1