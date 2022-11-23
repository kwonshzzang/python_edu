class Test:
	st = 100 # 정적 맴버데이터 Test.st로 글로벌 영역에 로딩(객체 생성과 무관)
	nCnt = 0
	
	def __init__(self):
		Test.nCnt += 1
		self.a = 10
		self.b = 20
		
		
	def setData(self, a, b): 
		self.a = a # 인스턴스 변수(반드시 객체 생성후 사용, 객체당 메모리(힙) 별도)
		self.b = b
		
	def show(self):
		print(self.a, self.b)
		
	
	@staticmethod
	def stfn(a): # 클래스 함수(클래스 이름으로 접근, 인스턴스 변수 사용 불가)
		Test.st = a
		
	@staticmethod
	def getCount():
		return Test.nCnt
		

print(Test.st)	
Test.st = 10000
print(Test.st)	

Test.stfn(20)
print(Test.st)

# obj = Test() # 객체 맴버데이터는 힙 영역에 객체 생성시 로딩

# 동일한 클래스에서 여러개의 클래스 객체를 생성한 경우 생성된 객체의 수를 구하시오
o1 = Test()
o2 = Test()
o3 = Test()
print(Test.getCount())
