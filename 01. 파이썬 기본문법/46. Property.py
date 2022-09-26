class Calendar:
	
	def __init__(self):
		self.__month__ = 0
		
		
	@property
	def month(self):
		print('getter call')
		return self.__month__
		
	@month.setter
	def month(self, month):
		print('setter call')
		if month < 1 or month > 12:
			print('잘못된 개월입니다.')
		else:
			self.__month__=month
			
			
cal = Calendar()
cal.month = 11  # cal.month(cal, 11)

print(cal.month) # cal.month()

