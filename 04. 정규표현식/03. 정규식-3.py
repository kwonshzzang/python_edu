import re

s = 'apple kiwi banana'
s1 = '서울시 은평구'

try:
	# match = re.search(r'ki[vwx]i', s)
	# match = re.search(r'ki[vwx]+i', s)
	# match = re.search(r'ki[a-z]i', s)
	# match = re.search(r'ki[a-z]+i', s)
	# match = re.search(r'서울[시은가]', s1)
	
	match = re.search(r'서울[가-힣]', s1) # 모든 한글
	
	print(match.group())
except Exception as err:
	print('not found')
