class Animal:
    def walk(self):
        print('걷습니다.')

    def eat(self):
        print('먹습니다.')

    def greet(self):
        print('인사합니다.')

class Human(Animal):
    def wave(self):
        print('손을 흔듭니다.')

    def greet(self):
        self.wave()

class Dog(Animal):
    def wag(self):
        print('꼬리를 흔듭니다.')

    def greet(self):
        self.wag()

class Cow(Animal):
    '''소'''

person = Human()
person.greet()

dog = Dog()
dog.greet()

cow = Cow()
cow.greet()
