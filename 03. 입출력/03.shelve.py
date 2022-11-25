import shelve
# sqlite db engine 사용

sh = shelve.open('mysh')
sh['name'] = '홍길동'
sh['age'] = 20
sh['data'] = [10, 20, 30, 40]
sh.close()

sh = shelve.open('mysh')
print(sh['name'])
print(sh['age'])
print(sh['data'])

for n in sh.keys():
    print(n)

#sh.pop('name')
sh.close()