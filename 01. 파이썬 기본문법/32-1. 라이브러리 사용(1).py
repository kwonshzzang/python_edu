# 특정 기능을 가지고 있는 함수를 모아 놓은 것 => 라이브러리

# import mylib
#
# print(mylib.hap(2, 3))
# print(mylib.gop(7, 1))
# print(mylib.absHap(-6, -3))
# print(mylib.make_circle(3))


##################################

# import mylib as m
#
# print(m.hap(3, 5))
# print(m.gop(3, 5))

##################################

from mylib import hap, make_circle

print(hap(7, 8))
print(make_circle(3))

# 원의 면적을 구하는 함수
# 원뿔의 부피를 구하는 함수
# 를 circlelib에 만들고
# userlib에서 사용