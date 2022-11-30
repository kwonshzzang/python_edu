# 로또 정답 숫자를 출력하시요.
#
# 1) 로또번호:1~45 의 숫자중 임의 6개의 숫자를 선택
# 랜덤: 1,5,20,23,41,42
#
# 2) 키보드로 6개의 숫자를 입력 (중복되지 않게)
# 숫자입력: 1 6 20 30 31 40
#
# 출력: 2개, 1,20

import random

lotto_numbers = range(1, 46)
answer_number = random.sample(lotto_numbers, 6)

print(answer_number)

input_number = input('숫자입력 :')
print(input_number.split())

myResult = [n for n in input_number.split() if int(n) in answer_number]
print(f'정답 갯수 : {len(myResult)}, 번호 : {myResult}')
