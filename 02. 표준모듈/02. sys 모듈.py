import sys

# print('hello')
# sys.exit(1)  # 강제종료
# print()

print(sys.argv) # 명령행 인자

my = [10, 20, 30, 40]
my1 = my

print(sys.getsizeof(my)) # 객체의 크기
print(sys.getrefcount(my) - 1)
print(sys.version) # python 버젼