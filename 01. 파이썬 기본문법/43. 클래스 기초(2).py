class Test:
	# 생성자 함수
	def __init__(self, a, b):
		self.a = a
		self.b = b
		
	# 소멸자 함수 : 객체 소멸전에 자동 호출 함수
	def __del__(self):
		print('del call')
		
	def setData(self, a, b):
		self.a = a
		self.b = b
		
	def show(self):
		print(self.a, self.b)
		
obj = Test(100, 200)
obj.show()

my = obj
obj = 'abc'
print('hello')

my.show() # my.show(my)

# RC(Reference Count)로 메모리 자동관리

print('========================================')

def fn():
	obj = Test(100, 200)
	obj.show()
	return obj
	
rst = fn()
print('hello')
rst.show()
