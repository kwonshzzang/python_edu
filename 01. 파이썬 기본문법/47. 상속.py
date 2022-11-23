class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

class Student(People):
    def __init__(self, name, age, stdNum):
        super().__init__(name, age)
        self.stdNum = stdNum

    def show(self):
        print(self.name, self.age, self.stdNum)


std = Student('홍길동', 20, 20220301)
std.show()

std.setName('이순신')
std.show()