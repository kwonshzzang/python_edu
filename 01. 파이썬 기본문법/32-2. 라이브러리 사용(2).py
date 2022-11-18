# import circlelib
#
# print('원의 넓이 :', circlelib.get_circle_area(3))
# print('원기둥의 부피 :', circlelib.get_cylinder_volume(3, 10))
# print('원뿔의 부피 :', circlelib.get_circular_con_volume(3, 10))

##################################

# import circlelib as c
#
# print('원의 넓이 :', c.get_circle_area(3))
# print('원기둥 부피 :', c.get_cylinder_volume(3, 10))
# print('원뿔 부피 :', c.get_circular_con_volume(3, 10))

##################################

from circlelib import *
import sys

print(sys.path) # python path

# 1. 내장함수(print, input, round) 임포트가 필요없음
# 2. import가 필요한 라이브러리
# 3. 써드파티 라이브러리(pip install)
# /anaconda/lib/site-packages

print('원의 넓이 :', get_circle_area(3))
print('원기둥의 부피 :', get_cylinder_volume(3, 10))
print('원뿔의 부피 :', get_circular_con_volume(3, 10))