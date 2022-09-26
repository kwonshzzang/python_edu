
class Test:
	
	def __init__(self): # 생성자 함수(객체 생성시 자동 호출)
		print('init call')
		print('init self :', id(self))
		self.a = 10
		self.b = 20
		
	def setData(self, a, b):
		print('setData self :', id(self))
		self.a = a
		self.b = b
		
	def show(self):
		print('show self :', id(self))
		print(self.a, self.b)
		
		
# 객체생성 : 해당 클래스의 맴버 데이터의 메모리 할당이 완료된 상태
obj = Test()          # 다른언어 Test obj = new Test()
print('obj 주소 :', id(obj))
# obj.__init__(obj)   # 컴파일러가 추가
obj.show()            # obj.show(self)
obj.setData(100, 200) # obj.setData(obj, 100, 200)
obj.show()


print('==============================================')
obj1 = Test()
print('obj1 주소 :', id(obj1))
# obj1.__init__(obj1)
obj1.setData(11, 22)  # obj1.setData(obj1, 11, 22)
obj1.show()           # obj1.show(obj1)


# 동일한 클래스에서 여러개의 객체가 발생하면
# 맴버데이터는 메모리(힙영역)에 할당됨

# 맴버함수는 공유(코드영역 텍스트 영역)에 할당
# 그런데 어떻게 각각의 맴버데이터 값을 R/W 할 수 있는가?
# 정답 : self
# 다른 언어는 컴파일러가 self 변수(this)를 자동 추가함

