pizza_slice = -9
person = 3

try:
    if pizza_slice <= 0:
        raise Exception('마이너스가 입력됨')

    per_slice = pizza_slice / person
    print(per_slice)

except ZeroDivisionError as err:
    print(err, '0으로 나누면 안됨')
except Exception as err:
    print(err)
finally:
    print('무조건 실행')

# if person == 0:
#     print('사람수를 0으로 입력하면 안됨')
#
# if ...
#
# else:
#     per_slice = pizza_slice / person
#     print(per_slice)