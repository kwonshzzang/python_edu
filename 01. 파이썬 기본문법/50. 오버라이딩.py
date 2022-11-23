class Pet:
    def sleep(self):
        print('zzzzzz')

    def eat(self): # 추상함수
        pass


class Dog(Pet):
    def speak(self):
        print('bow now')

    def eat(self): # 재정의(overriding)
        print('bone')

class Cat(Pet):
    def speak(self):
        print('meow')

    def eat(self):
        print('fish')

dog = Dog()
dog.speak()
dog.eat()
dog.sleep()