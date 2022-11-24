class MyIter:
    def __init__(self):
        self.myList = [10, 20, 30]
        self.nCnt = -1

    def __iter__(self):
        print('iter call')
        self.nCnt = -1
        return self

    def __next__(self):
        print('next call')
        self.nCnt += 1
        if self.nCnt == 3:
            raise StopIteration
        return self.myList[self.nCnt]


it = MyIter()
# print(next(it)) # it.__next__()
# print(next(it))
# print(next(it))

print()

for n in it:
    print(n)
