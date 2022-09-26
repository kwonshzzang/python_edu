# my = list([10, 20, 30])
# s = str('abc')
# s = 'abc'

my = [10, 20, 30]
my1 = my  # shallow copy(얕은 복사 :주소만 복사)

my1 = [10, 20, 30]
my1 = my.copy() # deep copy

print(id(my), id(my1))
print(my)
print(my1)


print('=============================')

my = [10, 20, 30]
my1 = my
my = 'abc'
print(my1)

print('=============================')

def fn():
	myList = [10, 20, 30]
	print(myList)
	return myList
	
rst = fn()
print('hello')
print(rst)

print('=============================')

def fn1(aa):
	aa[0] = 100
	aa.append(200)
	
my = [10, 20, 30]
fn1(my)
print(my)
	
