# 연산, 처리 => static
# 데이터용 => instance

import math

class Circle:
	
	@staticmethod
	def circleArea(r):
		return math.pi*r**2
		
	@staticmethod
	def cylinder(r, h):
		return math.pi*r**2*h
		
class Student:
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def show(self):
		print(self.name, self.age)
		
		
	
print(Circle.circleArea(3))
print(Circle.cylinder(3, 10))

student1 = Student('홍길동', 20)
student2 = Student('임꺽정', 40)

mydata = []
mydata.append(student1)
mydata.append(student2)

for std in mydata:
	std.show()
