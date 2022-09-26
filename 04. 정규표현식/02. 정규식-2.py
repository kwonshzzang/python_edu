import re

s = 'apple kiwi banana'

try:
	# match = re.search(r'ki.i', s)
	# match = re.search(r'ki\.i', s)
	
	match = re.search(r'^app', s)
	
	print(match.group())
	
except Exception as err:
	print('not found')
