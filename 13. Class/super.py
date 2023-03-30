class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('걷습니다.')

    def eat(self):
        print('먹습니다.')

    def greet(self):
        print(f'{self.name}이/가 인사합니다.')

class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand

    def wave(self):
        print(f'{self.hand}을 흔들면서')

    def greet(self):
        self.wave()
        super().greet()

person = Human('사람', '오른손')
person.greet()
