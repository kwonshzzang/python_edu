class Test:
    def __init__(self):
        self.d = {} # dict()
        self.a = 10
        self.b = 20

    def setData(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(self.a, self.b)

    def __repr__(self):
        return f'a={self.a} b={self.b}'

    def __add__(self, other):
        print('add call')
        return self.a + other

    def __setitem__(self, key, value):
        print('setitem call')
        self.d[key] = value

    def __getitem__(self, item):
        print('getitem call')
        return self.d[item]

tt = Test()
print(tt)        # tt.__repr__()
print(tt + 10)   # tt.__add__(10)

tt['aa'] = 100   # tt.__setitem__('aa', 100)
tt['bb'] = 200

print(tt['bb'])  # tt.__getitem__('bb')

my = [10, 20, 30] # list(10, 20, 30)
print(my)

myd = {}
myd['aa'] = 10
myd['bb'] = 20
print(myd)
