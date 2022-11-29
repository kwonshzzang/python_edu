# 1. 풀이

def myMax(a, b, c):
    max = a

    if max < b:
        max = b

    if max < c:
        max = c

    return max

print(f'1. 가장 큰 값을 구하는 함수 : {myMax(9, 20, 33)}')
print(f'1. 가장 큰 값을 구하는 함수 : {myMax(19, 78, 33)}')

print()

# 2. 풀이

def divisor(n):
    div = []
    for number in range(1, n+1):
        if n % number == 0:
            div.append(number)
    return div

print(f'2. 약수 구하기 : {divisor(72)}')
print(f'2. 약수 구하기 : {divisor(11)}')
print(f'2. 약수 구하기 : {divisor(10)}')

print()

# 3. 풀이

def is_leapYear(year):
    if((year % 4 ==0) and (year % 100 != 0)) or (year % 400 ==0):
        return True
    return False

print(f'3. 윤년 구하기(1990) : {is_leapYear(1990)}')
print(f'3. 윤년 구하기(1991) : {is_leapYear(1991)}')
print(f'3. 윤년 구하기(1992) : {is_leapYear(1992)}')
print(f'3. 윤년 구하기(2000) : {is_leapYear(2000)}')
print(f'3. 윤년 구하기(2003) : {is_leapYear(2003)}')
print(f'3. 윤년 구하기(2004) : {is_leapYear(2004)}')
print(f'3. 윤년 구하기(2016) : {is_leapYear(2016)}')

print()

# 4. 풀이
def return_change(price, paid_money):
    coin_type = [500, 100, 50, 10]
    coin_counts = []

    change_money = paid_money - price

    if change_money > 0:
        for coin in coin_type:
            count = change_money // coin
            coin_counts.append(count)
            change_money %= coin

    return coin_counts

print(f'4. 거스름돈(2160, 3000) : {return_change(2160, 3000)}')
print(f'4. 거스름돈(1200, 1210) : {return_change(1200, 1210)}')
print(f'4. 거스름돈(1320, 2000) : {return_change(1320, 2000)}')
print(f'4. 거스름돈(1320, 1320) : {return_change(1320, 1320)}')

print()

# 5. 풀이
def over_weight(weight, height):
    standard_weight = (height - 100) * 0.85
    over_weight_rate = (weight / standard_weight) * 100
    result = ""

    if over_weight_rate > 120:
        result = '비만'
    elif 110 < over_weight_rate <= 120:
        result = '과체중'
    elif 90 < over_weight_rate <= 110:
        result = '정상'
    else:
        result = '저체중'

    return result

print(f'5. 비만도 : {over_weight(85, 168)}')
print(f'5. 비만도 : {over_weight(60, 168)}')

print()

# 6. 풀이

print('******** 구구단 출력 ********')
for x in range(2, 10):
    for y in range(1, 10):
        print(f'{x}x{y}={x*y}')
    print()