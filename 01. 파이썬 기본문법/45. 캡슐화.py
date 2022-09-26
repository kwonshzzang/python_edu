# 캡슐화 : 맴버데이터를 맴버함수로만 R/W해서 데이터의 무결성을 보장하는 것
class Calendar:
	def __init__(self):
		self.month = 0
		
	def setMonth(self, month):
		if month < 1 or month > 12:
			print('잘못된 개월입니다.')
		else:
			self.month = month
			
	
	def getMonth(self):
		return self.month
		
		
cal = Calendar()

# cal.month = 13 # 맴버데이터 무결성 깨짐
cal.setMonth(13)

print(cal.getMonth())
			
