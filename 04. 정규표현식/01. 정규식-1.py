# 정규표현식: 문자열 패턴을 이용하여 분석

import re

s = 'apple kiwi banana'

try:
	
	# re.search(r'패턴', '대상문자')
	# match = re.search(r'apple', s)
	# match = re.search(r'straw', s)
	# match = re.search(r'ap*le', s)
	# match = re.search(r'ap+le', s)
	# match = re.search(r'ap?le', s)
	# match = re.search(r'ap{2}le', s)
	match = re.search(r'ap{2,4}le', s)
	
	
	# print(match)
	print(match.group())
	# print(match.span())
	
except Exception as err:
	print('not found')
