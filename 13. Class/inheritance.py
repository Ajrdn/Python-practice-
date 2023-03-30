class Animal:
    def walk(self):
        print('걷습니다.')

    def eat(self):
        print('먹습니다.')

class Human(Animal):
    def wave(self):
        print('손을 흔듭니다.')

class Dog(Animal):
    def wag(self):
        print('꼬리를 흔듭니다.')

person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()
